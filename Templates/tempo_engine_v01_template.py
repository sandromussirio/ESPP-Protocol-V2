# ============================================================
# TEMPO ENGINE — PROTOCOLO OFICIAL DE TESTE v0.1
# FONTE ÚNICA DA VERDADE
# OBJETIVO: ESTABILIDADE, INVARIÂNCIA, ZERO INFERÊNCIA
# NÃO É PLUGIN — NÃO É PRODUTO
# ============================================================

"""
CONTRATO JSON — TEMPO ENGINE v0.1

ESTRUTURA OBRIGATÓRIA:

{
  "objects": [
    {
      "name": str,
      "role": "BASE" | "CUT",

      # GEOMETRIA 2D (CAD)
      "points": [(x, y), ...],

      # VALORES DE Z (FORNECIDOS PELO USUÁRIO)
      "base_z": float,
      "extrude": float
    }
  ]
}

REGRAS ABSOLUTAS:
- CAD SEMPRE FORNECE GEOMETRIA 2D (x, y)
- NENHUM PONTO POSSUI Z
- Z É SEMPRE DEFINIDO PELO USUÁRIO (base_z, extrude)
- NENHUMA INFERÊNCIA AUTOMÁTICA
- QUALQUER VIOLAÇÃO GERA ERRO
"""

# ============================================================
# IMPORTS
# ============================================================

import bpy
import bmesh
from math import radians
from mathutils import Vector, Matrix

# ============================================================
# ERRO DE PROTOCOLO (NUNCA SILENCIOSO)
# ============================================================

class TempoProtocolError(Exception):
    pass

# ============================================================
# JSON CANÔNICO — CASO QUE DEVE SEMPRE FUNCIONAR
# ============================================================

JSON_CANONICO = {
    "objects": [
        {
            "name": "BASE_TEST",
            "role": "BASE",
            "points": [
                (0, 0),
                (4, 0),
                (4, 3),
                (0, 3)
            ],
            "base_z": 0.0,
            "extrude": 3.0
        },
        {
            "name": "CUT_TEST",
            "role": "CUT",
            "points": [
                (1, 1),
                (2, 1),
                (2, 2),
                (1, 2)
            ],
            "base_z": 0.0,
            "extrude": 3.0
        }
    ]
}

# ============================================================
# VALIDADOR DE JSON (OBRIGATÓRIO)
# ============================================================

def validar_json(data):

    if not isinstance(data, dict):
        raise TempoProtocolError("JSON raiz deve ser um dicionário.")

    if "objects" not in data:
        raise TempoProtocolError("JSON deve conter 'objects'.")

    if not isinstance(data["objects"], list):
        raise TempoProtocolError("'objects' deve ser uma lista.")

    for o in data["objects"]:

        if not isinstance(o, dict):
            raise TempoProtocolError("Cada objeto deve ser um dicionário.")

        if "name" not in o:
            raise TempoProtocolError("Objeto sem 'name'.")

        if o.get("role") not in ("BASE", "CUT"):
            raise TempoProtocolError(
                f"Role inválido em '{o.get('name')}'."
            )

        pts = o.get("points")
        if not isinstance(pts, list):
            raise TempoProtocolError(
                f"'points' deve ser lista em '{o.get('name')}'."
            )

        for p in pts:
            if (
                not isinstance(p, (list, tuple)) or
                len(p) != 2 or
                not all(isinstance(v, (int, float)) for v in p)
            ):
                raise TempoProtocolError(
                    f"Ponto inválido em '{o.get('name')}'. "
                    "CAD fornece apenas (x, y)."
                )

        if len(set(pts)) < 3:
            raise TempoProtocolError(
                f"Objeto '{o.get('name')}' precisa de ao menos 3 pontos únicos."
            )

        for k in ("base_z", "extrude"):
            if not isinstance(o.get(k), (int, float)):
                raise TempoProtocolError(
                    f"'{k}' deve ser numérico em '{o.get('name')}'."
                )

# ============================================================
# 1. SANITIZAÇÃO DE PONTOS (CONTRATO ASSUMIDO)
# ============================================================

def sanitize_points(points):
    """
    Remove duplicatas.
    Não altera ordem.
    Não fecha polígono.
    Não valida geometria.
    """
    clean = []
    for p in points:
        if p not in clean:
            clean.append(p)
    return clean

# ============================================================
# 2. MATERIAL — ALVENARIA (ESTÁVEL)
# ============================================================

def material_alvenaria():
    name = "MAT_ALVEN_0_46_61"
    mat = bpy.data.materials.get(name)

    r, g, b = 0/255, 46/255, 61/255

    if mat is None:
        mat = bpy.data.materials.new(name)
        mat.use_nodes = True
        bsdf = mat.node_tree.nodes["Principled BSDF"]
        bsdf.inputs["Base Color"].default_value = (r, g, b, 1)
        bsdf.inputs["Roughness"].default_value = 0.8

    mat.diffuse_color = (r, g, b, 1)
    return mat

# ============================================================
# 3. CRIAÇÃO DE SÓLIDO (FALHA EXPLÍCITA)
# ============================================================

def criar_solido(name, points_2d, base_z, extrude):

    pts = sanitize_points(points_2d)

    mesh = bpy.data.meshes.new(name)
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)

    bm = bmesh.new()

    try:
        verts = [bm.verts.new((x, y, base_z)) for x, y in pts]
        face = bm.faces.new(verts)
        bmesh.ops.recalc_face_normals(bm, faces=[face])
    except Exception:
        bm.free()
        raise TempoProtocolError(
            f"Falha ao criar face em '{name}'. Geometria inválida."
        )

    try:
        ext = bmesh.ops.extrude_face_region(bm, geom=[face])
        ev = [v for v in ext["geom"] if isinstance(v, bmesh.types.BMVert)]
        bmesh.ops.translate(bm, verts=ev, vec=(0, 0, extrude))
    except Exception:
        bm.free()
        raise TempoProtocolError(
            f"Falha na extrusão em '{name}'."
        )

    bm.to_mesh(mesh)
    bm.free()
    return obj

# ============================================================
# 4. BOOLEAN — SUBTRAÇÃO (DESTRUTIVO, VALIDADO)
# ============================================================

def boolean_subtract(base, cutter):

    if base == cutter:
        raise TempoProtocolError("Base e cutter não podem ser o mesmo objeto.")

    mats_backup = list(base.data.materials)

    mod = base.modifiers.new(
        name=f"BOOL_{cutter.name}",
        type='BOOLEAN'
    )
    mod.operation = 'DIFFERENCE'
    mod.object = cutter
    mod.solver = 'EXACT'

    bpy.context.view_layer.objects.active = base

    try:
        bpy.ops.object.modifier_apply(modifier=mod.name)
    except Exception:
        raise TempoProtocolError(
            f"Boolean falhou entre '{base.name}' e '{cutter.name}'."
        )

    base.data.materials.clear()
    for m in mats_backup:
        base.data.materials.append(m)

# ============================================================
# 5. OCULTAÇÃO DE SUBTRATOR
# ============================================================

def ocultar_subtrator(obj):
    obj.hide_set(True)
    obj.hide_render = True

# ============================================================
# 6. ROTAÇÃO GLOBAL (APÓS BOOLEAN)
# ============================================================

def aplicar_rotacao_global(obj, pivot_y, ang_x):
    pivot = Vector((0, pivot_y, 0))
    R = Matrix.Rotation(radians(ang_x), 4, 'X')

    obj.matrix_world = (
        Matrix.Translation(pivot) @
        R @
        Matrix.Translation(-pivot) @
        obj.matrix_world
    )

# ============================================================
# 7. EXECUÇÃO CONTROLADA (TESTE DE PROTOCOLO)
# ============================================================

def executar_tempo_engine(data):

    validar_json(data)

    bases = []
    cutters = []

    for o in data["objects"]:

        obj = criar_solido(
            o["name"],
            o["points"],
            o["base_z"],
            o["extrude"]
        )

        if o["role"] == "BASE":
            obj.data.materials.append(material_alvenaria())
            bases.append(obj)

        elif o["role"] == "CUT":
            ocultar_subtrator(obj)
            cutters.append(obj)

    for base in bases:
        for cut in cutters:
            boolean_subtract(base, cut)

    print("Tempo Engine — execução concluída (PROTOCOLO TESTE v0.1).")

# ============================================================
# EXECUÇÃO CANÔNICA (REGRESSÃO)
# ============================================================

if __name__ == "__main__":
    executar_tempo_engine(JSON_CANONICO)
