# Operational Isolation and Privacy Preserving Paradigms for On-Premise SLMs

[![License: MIT](https://shields.io)](https://opensource.org)
[![Python 3.10+](https://shields.io)](https://python.org)
[![Framework: PyTorch](https://shields.io)](https://pytorch.org)

An open-source research proposal framework designed to validate **Meta's Llama-3-8B** deployment, quantization pathways, Membership Inference Attacks (MIA), and mathematical privacy preservation routines (**DP-SGD** via Meta's Opacus) under memory-constrained local enterprise environments.

---

## Architectural Research Core

This master's thesis research repository addresses the critical tension between local resource efficiency, data leakage vulnerabilities, and mathematical privacy protection. The framework is divided into three distinct functional segments:

### 1. Memory and Inference Optimization (QLoRA)

* **Objective:** Freeze base models inside \(4\text{-bit}\) NormalFloat (\(\text{NF4}\)) allocations via `bitsandbytes`, scaling parameter updates through injection of Low-Rank Adapters (`PEFT`/LoRA).
* **Hardware Target:** Sub-6GB dedicated VRAM compute constraints (e.g., standard workstation or laptop architecture baselines).

### 2. Adversarial Model Auditing (Membership Inference)

* **Objective:** Simulate a malicious corporate internal insider attempting text reconstruction attacks.
* **Mechanism:** Queries token cross-entropy structures and identifies target memorization layouts via sequence perplexity checks.

### 🛡️ 3. Privacy Engineering Execution (DP-SGD)

* **Objective:** Mitigate information exfiltration by intercepting backward passes using the `Opacus` framework.
* **Mechanism:** Enforces per-sample gradient clipping boundaries (\(C\)) and adds strategic Gaussian noise (\(\sigma\)) to safeguard the Privacy Budget (\(\epsilon\)).

---

## Repository Directory Layout

```text
├── src/
│   ├── models/       # Quantized execution layers & QLoRA setups
│   ├── attacks/      # Adversarial Membership Inference implementations
│   ├── defenses/     # Opacus privacy-preserving engine integration
│   └── dashboard.py  # Consolidated unified simulation trial pipeline
├── requirements.txt  # Explicit platform package declarations
└── README.md         # Academic presentation portfolio documentation
```

---

## ⚡ Setup & Local Execution Guide

1. **Clone and enter the repository environment:**

   ```bash
   git clone https://github.com
   cd local-slm-privacy-framework
   ```

2. **Provision isolated virtual environment dependencies:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Execute the validation pipeline simulation run:**

   ```bash
   python3 src/dashboard.py
   ```

---

## Reference Framework Benchmarks

| Evaluation Layer | Active Memory Footprint | Performance Metric Baseline | Primary Security Status |
| :--- | :--- | :--- | :--- |
| **Unprotected Base Pipeline** | ~5.5 GB VRAM Space | Mean Latency: `12.49 ms` | 🚨 CRITICAL DATA LEAKAGE (MIA Perplexity < 1.85) |
| **Opacus DP-SGD Protected** | ~6.2 GB VRAM Space | Privacy Budget: \(\epsilon = 3.8\) | MATHEMATICALLY SECURED AGAINST EXTRACTION |
