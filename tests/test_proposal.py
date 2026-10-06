# tests/test_proposal.py
import os
import json
import pytest
from src.dashboard import execute_proposal_simulations


@pytest.fixture(autouse=True)
def run_pipeline_and_clean_up():
    """Fixture to ensure the simulation executes and cleans up before/after tests."""
    # Execute simulation to generate metrics asset
    execute_proposal_simulations()
    yield
    # Clean up the output artifact post-testing
    if os.path.exists("research_proposal_benchmarks.json"):
        os.remove("research_proposal_benchmarks.json")


def test_benchmark_file_generation():
    """Verifies that the validation execution outputs a valid JSON file structure."""
    assert os.path.exists("research_proposal_benchmarks.json") is True


def test_optimization_metrics():
    """Ensures Part 1 QLoRA hardware bounds meet local 6GB specification requirements."""
    with open("research_proposal_benchmarks.json", "r") as f:
        data = json.load(f)

    assert "optimization" in data
    assert data["optimization"]["format"] == "NF4"
    assert (
        data["optimization"]["static_vram_gb"] <= 6.0
    )  # Must fit local hardware ceilings


def test_vulnerability_and_defense_behavior():
    """Validates that DP-SGD noise layers successfully disrupt data extraction risks."""
    with open("research_proposal_benchmarks.json", "r") as f:
        data = json.load(f)

    assert "vulnerability" in data
    assert "defense" in data

    # Mathematical baseline validation:
    # Unprotected pipelines must register high threat risks (low perplexity scores)
    # Protected pipelines must display structural safety (high perplexity scores)
    assert data["vulnerability"]["unprotected_mia_perplexity"] < 2.0
    assert data["defense"]["protected_mia_perplexity"] > 3.5
    assert data["defense"]["epsilon_budget"] < 4.5
