<!-- .github/PULL_REQUEST_TEMPLATE.md -->
# Research Framework Pull Request Review

## 1. Core Contribution Type

*Please select the target development milestone this PR addresses (check all that apply):*

- [ ] **Part 1: Hardware Optimization** (QLoRA, Quantization configs, VRAM benchmarks)
- [ ] **Part 2: Adversarial Audit Suite** (MIA modeling, token log-prob extraction code)
- [ ] **Part 3: Privacy Engineering Defenses** (Meta Opacus, DP-SGD loops, Epsilon budgets)
- [ ] **CI/CD / Documentation** (Workflows, LaTeX, testing manifests)

## 2. Empirical Performance Metrics Verification

*If this PR alters or appends new benchmark execution logs, provide your system metrics profile below:*

| Runtime Framework Engine | Mean Step Compute Latency | Peak Monitored VRAM Footprint | Epsilon Budget (ε) Baseline |
| :--- | :--- | :--- | :--- |
| **PyTorch Layer** | `0.00 ms` | `0.00 MB` | ε = |
| **TensorFlow Layer** | `0.00 ms` | `0.00 MB` | ε = |

## 3. Mandatory Testing Affirmations

*Verify code integration health by checking the boxes below:*

- [ ] The full local unit test validation sequence passes cleanly without failure via `pytest tests/`.
- [ ] The local interface layer compiles and runs successfully under the automated wrapper `./run_all.sh`.
- [ ] Memory footprint metrics conform to the absolute 6GB target system constraints defined in the accepted spec profile.

## 4. Summary & Contextual Abstract

*Provide a high-level summary detailing how these alterations enhance or optimize the overall thesis project architecture:*
