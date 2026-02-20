1. OBJETIVO

Definir o contrato determinístico do Tempo Engine para Blender, garantindo:

Zero inferência geométrica

Execução determinística

Validação obrigatória antes da execução

Compatibilidade total com v0.1

Extensões controladas v0.2

2. CONTRATO JSON — v0.1 (OBRIGATÓRIO)

Estrutura mínima válida:

{
  "objects": [
    {
      "name": "string",
      "role": "BASE" | "CUT",
      "points": [[x, y], ...],
      "base_z": number,
      "extrude": number
    }
  ]
}
Regras Absolutas

points contém apenas coordenadas 2D (x, y)

Nenhum ponto pode conter Z

Z é definido exclusivamente por base_z e extrude

Mínimo de 3 pontos únicos

Qualquer violação gera erro e aborta execução

Nenhuma correção automática é permitida

3. EXECUÇÃO GEOMÉTRICA

Sólidos devem ser gerados com bmesh

Proibido usar bpy.ops para geração

Boolean deve ser aplicado sem bpy.ops

Ordem do JSON deve ser preservada

Todo CUT subtrai de todo BASE

CUT deve ser ocultado após aplicação

4. MATERIAL CANÔNICO

Todo objeto BASE deve receber material:

RGB (0, 46, 61)

Roughness = 0.8

Material não pode ser perdido após boolean

5. EXTENSÕES v0.2 (OPCIONAIS)

Se presentes no JSON raiz:

5.1 Rotação Global
"rotacao": {
  "pivot": [x, y, z],
  "angulo": number,
  "eixo": "X" | "Y" | "Z"
}

Regras:

Aplicada após boolean

Somente se explicitamente presente

Nenhuma rotação implícita

5.2 Instâncias LINKED
"instancias": [
  {
    "mode": "LINKED",
    "pivot": [x, y, z],
    "destinos": [[x, y, z], ...]
  }
]

Regras:

mode obrigatório e deve ser "LINKED"

Instâncias aplicadas somente aos objetos BASE finais

Instâncias devem compartilhar a mesma malha (linked data)

Ordem determinística conforme lista

Nenhuma cópia independente permitida

6. COMPATIBILIDADE

JSON contendo apenas "objects" é v0.1

JSON contendo "rotacao" e/ou "instancias" é v0.2

v0.2 nunca deve quebrar v0.1

7. PROIBIÇÕES ABSOLUTAS

Não fechar automaticamente polígonos

Não reordenar pontos

Não corrigir topologia

Não inferir valores ausentes

Não aplicar transformações implícitas