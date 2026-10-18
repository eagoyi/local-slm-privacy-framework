# tests/test_proposal.py
import os
import json
import pytest
from src.sweep_generator import execute_multi_model_sweep


@pytest.fixture(scope="module", autouse=True)
def run_pipeline_provisioning():
    """Fixture to ensure the multi-model sweep executes before tests run."""
    execute_multi_model_sweep()
    yield
    # Optional: Keep the file intact for the Streamlit dashboard app to read later
    pass


def test_benchmark_file_generation():
    """Verifies that the validation execution outputs a valid JSON file structure."""
    assert os.path.exists("research_proposal_benchmarks.json") is True


def test_optimization_metrics():
    """Ensures Part 1 QLoRA hardware bounds meet local 6GB specification requirements."""
    with open("research_proposal_benchmarks.json", "r") as f:
        data = json.load(f)

    assert "models_sweep" in data
    # Audit the dynamic targets for our models
    for model_name in ["TinyLlama-1.1B", "Qwen2.5-0.5B"]:
        assert model_name in data["models_sweep"]
        metrics = data["models_sweep"][model_name]
        assert metrics["optimization"]["format"] == "NF4"
        assert metrics["optimization"]["static_vram_gb"] <= 6.0


def test_vulnerability_and_defense_behavior():
    """Validates that DP-SGD noise layers successfully disrupt data extraction risks."""
    with open("research_proposal_benchmarks.json", "r") as f:
        data = json.load(f)

    for model_name in ["TinyLlama-1.1B", "Qwen2.5-0.5B"]:
        metrics = data["models_sweep"][model_name]
        assert "vulnerability" in metrics
        assert "defense" in metrics

        # Unprotected pipelines must register high threat risks (low perplexity scores)
        # Protected pipelines must display structural safety (high perplexity scores)
        assert metrics["vulnerability"]["unprotected_mia_perplexity"] < 2.0
        assert metrics["defense"]["protected_mia_perplexity"] > 3.5
        assert metrics["defense"]["epsilon_budget"] < 4.5
