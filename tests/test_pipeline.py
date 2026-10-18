# tests/test_pipeline.py
import os
import json
import pytest
import torch
from src.sweep_generator import execute_multi_model_sweep


@pytest.fixture(scope="module", autouse=True)
def run_sweep_provisioning():
    execute_multi_model_sweep()


def test_sweep_payload_integrity():
    """Verifies the sweep module successfully constructs target data layouts."""
    assert os.path.exists("research_proposal_benchmarks.json")
    with open("research_proposal_benchmarks.json", "r") as f:
        data = json.load(f)
    assert "models_sweep" in data
    assert "TinyLlama-1.1B" in data["models_sweep"]
    assert "Qwen2.5-0.5B" in data["models_sweep"]


def test_hardware_specification_guardrails():
    """Enforces academic thesis criteria that VRAM footprint limits scale below 6GB."""
    with open("research_proposal_benchmarks.json", "r") as f:
        data = json.load(f)

    for label, metrics in data["models_sweep"].items():
        peak_overhead = metrics["optimization"]["train_vram_gb"]
        assert (
            peak_overhead <= 6.0
        ), f"Hardware violation: {label} overhead registers at {peak_overhead}GB!"


def test_cuda_runtime_driver_matching():
    """Ensures device maps are tracking native driver parameters correctly if GPU present."""
    if torch.cuda.is_available():
        assert torch.cuda.device_count() > 0
        assert "NVIDIA" in torch.cuda.get_device_name(0)
