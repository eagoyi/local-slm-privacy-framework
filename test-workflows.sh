#!/bin/bash
set -e

echo "Step 1: Running fast syntax linting..."
pre-commit run actionlint --all-files

echo "Step 2: Running act dry-run (simulating execution)..."
act -n

echo "To run a full local execution, manually run: act"
