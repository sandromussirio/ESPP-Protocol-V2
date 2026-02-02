# Efficient Spatial Prompt Protocol (ESPP)

**Version:** v1.2  
**Author:** Sandro Resende Mussi  
**Status:** Deterministic spatial protocol validated through real architectural use cases  

---

## Overview

The **Efficient Spatial Prompt Protocol (ESPP)** is a **deterministic spatial description protocol**
designed to enable **rapid validation of architectural spatial ideas** without requiring
traditional 3D modeling workflows.

In ESPP, the term *prompt* refers to an **explicit, structured spatial instruction** —
not a natural language request — designed to be executed deterministically.

ESPP treats spatial description as **explicit, executable data**, allowing architectural intent
to be stabilized, validated, and executed **before** investing time in manual modeling,
detailed documentation, or physical construction.

Spatial descriptions may be executed by deterministic engines, with optional **AI-assisted
support strictly limited to non-geometric tasks**, preserving full spatial determinism.

ESPP is intentionally positioned **before traditional 3D modeling**, acting as a cognitive
and computational validation layer for spatial intent.

---

## Why ESPP Exists

Architectural projects frequently lose precision, intent, and consistency when transitioning
from 2D drawings to 3D models.

This gap is caused by manual modeling processes, software-specific behavior, and implicit
geometric assumptions introduced during interpretation.

**ESPP was created to eliminate this gap by treating spatial description as explicit,
machine-readable, and executable data.**

---

## Core Characteristics

- **Deterministic execution**  
  The same input always produces the same output.

- **Explicit spatial description**  
  All spatial attributes — including geometry, transformations, instancing, and semantics —
  are explicitly declared and never inferred.  
  This includes both spatial state and spatial operations applied during execution.

- **Declarative modeling**  
  Architecture is described as structured data, not manually constructed.

- **Software-agnostic design**  
  ESPP is independent of CAD, BIM, or rendering tools.

- **Auditable and reproducible**  
  All spatial results are traceable to explicit input data.

---

## What ESPP Is Not

- Not a generative design system  
- Not a probabilistic or AI-driven model  
- Not a CAD or BIM replacement  
- Not a visual modeling tool  

ESPP does not replace spatial reasoning.  
It assumes and reinforces the architect’s responsibility to conceive and validate space
**before** any computational execution.

---

## Execution Engines

ESPP itself is **not an execution engine**.

Execution engines may be implemented on top of the protocol to validate and execute
spatial descriptions according to ESPP rules.

**Tempo Engine** is a reference implementation built to demonstrate and validate
deterministic execution of the protocol.  
It may be distributed as scripts, plugins, or adapters, without defining or altering ESPP.

---

## Current Status

- Protocol formally defined  
- Core principles validated through real architectural use cases  
- JSON-based execution proven via scripting  
- Reference execution engine under consolidation  

For a detailed and honest description of the current state and future direction,
see **ESPP_STATUS_AND_VISION.md**.

---

## License

© 2025–2026 Sandro Resende Mussi  
All rights reserved.


