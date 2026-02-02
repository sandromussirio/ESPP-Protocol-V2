[ESPP_EXECUTIONS_RULES.md](https://github.com/user-attachments/files/25025414/ESPP_EXECUTIONS_RULES.md)
# ESPP Execution Rules

This document defines the **mandatory execution rules** of the ESPP – Efficient Spatial Prompt Protocol.

These rules form the **strict contract** between:
- those who describe space (architects, scripts, or language models)
- and those who execute the description (execution engines)

If any rule is violated, the description **must not be executed**.

---

## Rule 1 — No Inference

All spatial attributes, geometric and non-geometric, must be **explicitly declared**.


The system must not:
- infer geometry
- complete missing values by assumption
- automatically correct data

If a piece of information is not declared, it **does not exist**.

Explicit normalization rules defined by the protocol
(e.g. default Z = 0, default extrusion = 0)
are not considered inference.

---

## Rule 2 — Deterministic Execution

ESPP execution must be **deterministic**.

This means that:
- the same input file
- executed under the same conditions
- must always produce the same output

No randomness or probabilistic variation is allowed.

---

## Rule 3 — One Element, One Description

Each spatial element must be described **independently**.

- One element must not implicitly depend on another
- Changes to one element must not affect others

Context persistence is guaranteed by the separation of descriptions.

---

## Rule 4 — Explicit Vertical Definition

Every spatial element must define:
- vertical position (Z)
- extrusion value

The following are not allowed:
- implicit heights
- constructive assumptions
- inferred dimensions

---

## Rule 5 — Description ≠ Execution

ESPP **describes** space.  
The execution engine **executes** the description.

The protocol:
- does not generate design decisions
- does not alter spatial attributes
- does not optimize or infer geometry


The engine:
- does not interpret intent
- does not modify descriptions
- does not introduce variations

AI-assisted processes may be used strictly for parsing, validation,
or orchestration tasks, provided that no geometric inference
or modification is introduced.

---

## Rule 6 — Implicit Geometry Is Forbidden

All geometry must be defined explicitly.

The following are not allowed:
- automatic closures
- topological corrections
- precision adjustments
- inferred faces or volumes

---

## Rule 7 — Validation Before Execution

Every ESPP description must be validated before execution.

Invalid descriptions:
- must not be executed
- must return an error
- must not be automatically “fixed”

Validation ensures protocol integrity.

---

## Rule 8 — Software Independence

ESPP rules are **software-independent**.

Any execution engine:
- must fully respect these rules
- must not introduce proprietary behavior
- must not relax protocol constraints

The behavior of ESPP is defined **exclusively** by these rules.

The ESPP protocol may be implemented by different execution engines.

**Tempo Engine** is a reference implementation currently under development,
created to validate and demonstrate deterministic execution of the protocol.
The engine may be distributed as scripts, plugins, or adapters,
without defining or altering the protocol itself.

