[ESPP_GETTING_STARTED.v1.1.md](https://github.com/user-attachments/files/25025437/ESPP_GETTING_STARTED.v1.1.md)
# Getting Started — Using ESPP

This document describes the **minimal and correct way** to use the  
**ESPP — Efficient Spatial Prompt Protocol** to **validate a spatial idea**.

If you understand this document, you understand **how and when to use ESPP**.

---

## When to Use ESPP

ESPP should be used when you need to:

- Rapidly validate a spatial idea
- Verify proportions, relationships, and repetition of elements
- Confirm spatial coherence **before** traditional 3D modeling
- Avoid ambiguities commonly found in generative images
- Work with controlled instancing and repetition of elements

ESPP is especially useful during early design stages, such as  
**concept design** and **preliminary studies**.

---

## When NOT to Use ESPP

ESPP is **not** intended for:

- Construction detailing
- Executive or technical documentation
- Full BIM modeling
- Final rendering or marketing visualization
- Creative form generation by inference

It does not replace traditional tools — it **precedes** them.

---

## What You Need

To use ESPP, you only need:

- Explicit 2D geometry (X and Y coordinates), obtained from:
  - a simple CAD drawing (floor plan)
  - coordinate lists extracted from CAD
- Explicit height (Z) and extrusion values
- A JSON file structured according to the ESPP protocol
- A deterministic execution engine (e.g. Tempo Engine)

Execution engines may optionally use **AI-assisted processes for parsing or orchestration**,
provided that all spatial geometry remains explicitly declared and deterministic.

No manual 3D modeling is required.

---

## Fundamental Principle

In ESPP:

- Nothing is inferred
- Nothing is interpreted
- Nothing is automatically completed

All spatial information must be **explicitly declared**.

If something is not described, **it does not exist** for the system.

---

## Usage Flow (Summary)

The spatial idea must be fully conceived by the architect **before any execution**.

A typical ESPP workflow is:

1. The spatial idea is defined by the architect
2. Base geometry is drawn in 2D (simple plan)
3. Coordinates are converted into an ESPP description (JSON)
4. The description is executed deterministically
5. A visualization is generated to **validate the idea**
6. A decision is made: proceed, adjust, or discard

The goal is not to create a final model, but to **confirm spatial intent**.

---

## Simplified Conceptual Example

This example is intentionally simplified and conceptual.  
It illustrates the principles of ESPP, not a complete specification.

```json
{
  "element_id": "wall_01",
  "geometry": {
    "type": "polygon",
    "vertices": [
      [0.0, 0.0],
      [4.0, 0.0],
      [4.0, 0.2],
      [0.0, 0.2]
    ]
  },
  "z_position": 0.0,
  "extrusion": 3.0,
  "semantic_role": "WALL"
}
