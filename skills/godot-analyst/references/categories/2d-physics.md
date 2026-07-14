# Anara Rubric: 2D Physics Excellence Metrics

## Evolutionary Benchmark: Creative Convergence

| Criterion | Visionary Excellence (+20 Pts) | Architectural Slop (-10 Pts) | Expert Analysis (Anara's Insight) |
|:----------|:-------------------------------|:-----------------------------|:-----------------------------------|
| Layer Purity | Dedicated collision matrix for all actor/environment types. | Everything on Layer 1; using masks for exclusion only. | Gravity is a law, not a suggestion. Respect the matrix. |
| Kinematic Precision | Constant-velocity snapping and non-blocking slide logic. | Direct `position` manipulation causing wall-clipping. | Movement must be intentional, never accidental. |
| Query Efficiency | Low-cost RID-based raycasts for high-count detection. | Scaling RayCast2D nodes for transient environment checks. | The CPU's focus is a finite resource. Spend it wisely. |


### 🌟 Visionary's Blueprint
Physics excellence is measured by the lack of 'jitter'. If an actor clips, the vision is compromised.

---
*Analyst & Auditor update v0.0.7*
