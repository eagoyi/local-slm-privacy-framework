#!/bin/bash

# --- Operational Isolation & Privacy Preserving Framework Launcher ---
# Fail immediately if any sequential command exits with a non-zero status
set -e

# Visual Anchors for Terminal output
INFO='\033[0;34m[INFO]\033[0m'
SUCCESS='\033[0;32m[SUCCESS]\033[0m'
WARN='\033[0;33m[WARN]\033[0m'

echo "=========================================================================="
  echo "    ORCHESTRATION PIPELINE: LOCAL SLM PRIVACY ENGINEERING FRAMEWORK"
echo "=========================================================================="

# 1. Verify Present Working Directory Infrastructure
if [ ! -d "src" ]; then
    echo -e "${WARN} Execution context mismatch. Relocating root scope..."
    cd "$(dirname "$0")"
fi

# 2. Virtual Environment Verification Sequence
if [ ! -d "venv" ]; then
    echo -e "${INFO} Local Python virtual environment ('venv') not detected."
    echo -e "${INFO} Spawning isolated platform sandbox using python3-venv..."
    python3 -m venv venv
fi

# 3. Activation & Dependency Check
echo -e "${INFO} Engaging virtual environment workspace..."
source venv/bin/activate

echo -e "${INFO} Auditing core packaging manager and pipeline requirements..."
pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet

# 4. Generate Core Metrics Log Data Maps
echo -e "${INFO} Parsing active cross-framework performance metrics..."
if [ -f "src/parse_logs.py" ]; then
    python3 src/parse_logs.py
else
    echo -e "${INFO} Falling back to core terminal data map generator..."
    python3 src/dashboard.py
fi

# 5. Launch Browser-Based Streamlit Interface Node
echo -e "${SUCCESS} Initialization baseline successfully validated."
echo -e "${INFO} Spin-up sequence engaging Streamlit web architecture..."
streamlit run src/app.py
