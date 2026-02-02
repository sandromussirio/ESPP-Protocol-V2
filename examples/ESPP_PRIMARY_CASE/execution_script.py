import bpy
import bmesh
from mathutils import Vector, Matrix
from math import radians

# ============================================================
# DM01 - ESTANTE LACAVE (COMPLETA)
# ============================================================

data = {
    "objects": [

        # ------------------------ FUNDO ------------------------
        {
            "name": "DM01_FUNDO",
            "layer": "DM01_FUND",
            "base_z": 0.0,
            "extrude": 0.05,
            "color": [173, 152, 122],
            "points": [
                [0.98, 6.15, 0.0],
                [2.11, 6.15, 0.0],
                [2.11, 3.88, 0.0],
                [0.98, 3.88, 0.0],
                [0.98, 6.15, 0.0]
            ]
        },

        # ------------------------ CORPO ------------------------
        {
            "name": "DM01_CORPO",
            "layer": "DM01_CORP",
            "base_z": 0.05,
            "extrude": 0.36,
            "color": [234,219,182],
            "points": [
                [0.98, 3.88, 0.0],
                [0.98, 6.15, 0.0],
                [2.11, 6.15, 0.0],
                [2.11, 3.88, 0.0],
                [2.08, 3.88, 0.0],
                [2.08, 6.12, 0.0],
                [1.01, 6.12, 0.0],
                [1.01, 3.88, 0.0],
                [0.98, 3.88, 0.0]
            ]
        },

        # ------------------------ PRATELEIRA FUNDO ------------------------
        {
            "name": "DM01_PRATEL_FUND",
            "layer": "DM01_PRATEL_FUND",
            "base_z": 0.05,
            "extrude": 0.32,
            "color": [234,219,182],
            "points": [
                [1.01, 3.98, 0.0],
                [2.08, 3.98, 0.0],
                [2.08, 3.95, 0.0],
                [1.01, 3.95, 0.0],
                [1.01, 3.98, 0.0]
            ]
        },

        # ------------------------ ILHARGA ------------------------
        {
            "name": "DM01_ILHARGA",
            "layer": "DM01_ILHARG",
            "base_z": 0.05,
            "extrude": 0.33,
            "color": [234,219,182],
            "points": [
                [1.53, 3.98, 0.0],
                [1.53, 4.59, 0.0],
                [1.56, 4.59, 0.0],
                [1.56, 3.98, 0.0],
                [1.53, 3.98, 0.0]
            ]
        },

        # ------------------------ SOCO ------------------------
        {
            "name": "DM01_SOCO",
            "layer": "DM01_SOC",
            "base_z": 0.26,
            "extrude": 0.25,
            "color": [173,153,11],
            "points": [
                [1.01, 3.88, 0.0],
                [1.01, 3.95, 0.0],
                [2.08, 3.95, 0.0],
                [2.08, 3.88, 0.0],
                [1.01, 3.88, 0.0]
            ]
        },

        # ------------------------ TOPO ACABAMENTO (1..4) ------------------------
        {
            "name": "DM01_TOPO_ACAB_01",
            "layer": "DM01_TOPO_ACAB_0",
            "base_z": 0.36,
            "extrude": 0.025,
            "color": [234,219,182],
            "points": [
                [1.01, 5.68, 0.0],
                [1.01, 5.73, 0.0],
                [2.08, 5.73, 0.0],
                [2.08, 5.68, 0.0],
                [1.01, 5.68, 0.0]
            ]
        },
        {
            "name": "DM01_TOPO_ACAB_02",
            "layer": "DM01_TOPO_ACAB_0",
            "base_z": 0.36,
            "extrude": 0.025,
            "color": [234,219,182],
            "points": [
                [1.01, 5.30, 0.0],
                [1.01, 5.36, 0.0],
                [2.08, 5.36, 0.0],
                [2.08, 5.30, 0.0],
                [1.01, 5.30, 0.0]
            ]
        },
        {
            "name": "DM01_TOPO_ACAB_03",
            "layer": "DM01_TOPO_ACAB_0",
            "base_z": 0.36,
            "extrude": 0.025,
            "color": [234,219,182],
            "points": [
                [1.01, 4.96, 0.0],
                [2.08, 4.96, 0.0],
                [2.08, 4.90, 0.0],
                [1.01, 4.90, 0.0],
                [1.01, 4.96, 0.0]
            ]
        },
        {
            "name": "DM01_TOPO_ACAB_04",
            "layer": "DM01_TOPO_ACAB_0",
            "base_z": 0.36,
            "extrude": 0.025,
            "color": [234,219,182],
            "points": [
                [1.01, 4.62, 0.0],
                [2.08, 4.62, 0.0],
                [2.08, 4.56, 0.0],
                [1.01, 4.56, 0.0],
                [1.01, 4.62, 0.0]
            ]
        },

        # ------------------------ PRATELEIRAS INCLINADAS (1..4) ------------------------
        {
            "name": "DM01_PRATEL_INCL_01",
            "layer": "DM01_PRATEL_INCL_0",
            "base_z": 0.05,
            "extrude": 0.33,
            "color": [234,219,182],
            "points": [
                [1.01, 5.72, 0.0],
                [1.03, 5.72, 0.0],
                [2.08, 5.72, 0.0],
                [2.08, 5.70, 0.0],
                [1.01, 5.70, 0.0],
                [1.01, 5.72, 0.0]
            ]
        },
        {
            "name": "DM01_PRATEL_INCL_02",
            "layer": "DM01_PRATEL_INCL_0",
            "base_z": 0.05,
            "extrude": 0.33,
            "color": [234,219,182],
            "points": [
                [1.01, 5.35, 0.0],
                [1.03, 5.35, 0.0],
                [2.08, 5.35, 0.0],
                [2.08, 5.32, 0.0],
                [1.01, 5.32, 0.0],
                [1.01, 5.35, 0.0]
            ]
        },
        {
            "name": "DM01_PRATEL_INCL_03",
            "layer": "DM01_PRATEL_INCL_0",
            "base_z": 0.05,
            "extrude": 0.33,
            "color": [234,219,182],
            "points": [
                [1.01, 4.95, 0.0],
                [2.08, 4.95, 0.0],
                [2.08, 4.93, 0.0],
                [1.01, 4.93, 0.0],
                [1.01, 4.95, 0.0]
            ]
        },
        {
            "name": "DM01_PRATEL_INCL_04",
            "layer": "DM01_PRATEL_INCL_0",
            "base_z": 0.05,
            "extrude": 0.33,
            "color": [234,219,182],
            "points": [
                [1.01, 4.61, 0.0],
                [2.08, 4.61, 0.0],
                [2.08, 4.59, 0.0],
                [1.01, 4.59, 0.0],
                [1.01, 4.61, 0.0]
            ]
        },

        # ------------------------ ADEGA (1..4) ------------------------
        {
            "name": "DM01_ADEGA_01",
            "layer": "DM01_ADEG",
            "base_z": 0.05,
            "extrude": 0.31,
            "color": [234,219,182],
            "points": [
                [1.56, 3.98, 0.0],
                [1.56, 4.00, 0.0],
                [2.06, 4.56, 0.0],
                [2.08, 4.56, 0.0],
                [2.08, 4.55, 0.0],
                [1.57, 3.98, 0.0],
                [1.56, 3.98, 0.0]
            ]
        },
        {
            "name": "DM01_ADEGA_02",
            "layer": "DM01_ADEG",
            "base_z": 0.05,
            "extrude": 0.31,
            "color": [234,219,182],
            "points": [
                [1.56, 4.55, 0.0],
                [1.56, 4.56, 0.0],
                [1.58, 4.56, 0.0],
                [2.08, 4.00, 0.0],
                [2.08, 3.98, 0.0],
                [2.06, 3.98, 0.0],
                [1.56, 4.55, 0.0]
            ]
        },
        {
            "name": "DM01_ADEGA_03",
            "layer": "DM01_ADEG",
            "base_z": 0.05,
            "extrude": 0.31,
            "color": [234,219,182],
            "points": [
                [1.01, 4.00, 0.0],
                [1.51, 4.56, 0.0],
                [1.53, 4.56, 0.0],
                [1.53, 4.55, 0.0],
                [1.03, 3.98, 0.0],
                [1.01, 3.98, 0.0],
                [1.01, 4.00, 0.0]
            ]
        },
        {
            "name": "DM01_ADEGA_04",
            "layer": "DM01_ADEG",
            "base_z": 0.05,
            "extrude": 0.31,
            "color": [234,219,182],
            "points": [
                [1.01, 4.55, 0.0],
                [1.01, 4.56, 0.0],
                [1.03, 4.56, 0.0],
                [1.53, 4.00, 0.0],
                [1.53, 3.98, 0.0],
                [1.52, 3.98, 0.0],
                [1.01, 4.55, 0.0]
            ]
        }
    ]
}

# ============================================================
# FUNÇÃO DE CRIAÇÃO DE MESH
# ============================================================

def create_mesh_from_points(name, pts, base_z, extrude, color):
    pts = list(pts)
    if len(pts) > 2 and pts[0] == pts[-1]:
        pts = pts[:-1]

    mesh = bpy.data.meshes.new(name)
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)

    bm = bmesh.new()
    verts = [bm.verts.new((p[0], p[1], base_z)) for p in pts]
    bm.faces.new(verts)
    bm.to_mesh(mesh)
    bm.free()

    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value": (0,0,extrude)})
    bpy.ops.object.mode_set(mode="OBJECT")

    mat = bpy.data.materials.new(name + "_MAT")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = (color[0]/255, color[1]/255, color[2]/255, 1)
    obj.data.materials.append(mat)

    return obj

# ============================================================
# CRIAR TODOS OS OBJETOS
# ============================================================

created = []
for o in data["objects"]:
    created.append(create_mesh_from_points(
        o["name"], o["points"], o["base_z"], o["extrude"], o["color"]
    ))

# ============================================================
# ROTAÇÃO 90° NO EIXO X (PIVOT 0.98, 3.88)
# ============================================================

pivot = Vector((0.98, 3.88, 0.0))
angle = radians(90)

R = Matrix.Rotation(angle, 4, 'X')
T1 = Matrix.Translation(-pivot)
T2 = Matrix.Translation(pivot)

for obj in created:
    obj.matrix_world = T2 @ R @ T1 @ obj.matrix_world

# ============================================================
# REPOUSAR NO Z=0
# ============================================================

min_z = min((obj.matrix_world @ v.co).z for obj in created for v in obj.data.vertices)

for obj in created:
    obj.location.z -= min_z

# ============================================================
# CÓPIA PARA OS 3 PONTOS (INSTÂNCIAS)
# ============================================================

origin = Vector((0.98, 3.88, 0.0))
targets = [
    Vector((2.11, 3.88, 0.0)),
    Vector((3.24, 3.88, 0.0)),
    Vector((4.37, 3.88, 0.0))
]

for target in targets:
    offset = target - origin
    for obj in created:
        clone = obj.copy()
        clone.data = obj.data.copy()
        bpy.context.collection.objects.link(clone)
        clone.location.x += offset.x
        clone.location.y += offset.y

print("DM01 COMPLETO GERADO COM SUCESSO.")