# src/parse_logs.py
import json
import os


def parse_and_merge_logs():
    print("[+] Initiating real log parser...")

    # Initialize from the existing dashboard, or create a fallback structure.
    if os.path.exists("research_proposal_benchmarks.json"):
        with open("research_proposal_benchmarks.json", "r") as f:
            dashboard_data = json.load(f)
    else:
        dashboard_data = {}
    dashboard_data.setdefault("real_runs", {})

    # 1. Parse Real PyTorch Baseline Logs
    if os.path.exists("pytorch_benchmark.json"):
        with open("pytorch_benchmark.json", "r") as f:
            pt_data = json.load(f)
        if pt_data:
            avg_time = sum(d["step_time_ms"] for d in pt_data) / len(pt_data)
            peak_vram = max(d["reserved_vram_mb"] for d in pt_data)
            dashboard_data["real_runs"]["PyTorch"] = {
                "avg_step_time_ms": round(avg_time, 2),
                "peak_vram_mb": round(peak_vram, 2),
                "final_loss": pt_data[-1]["loss"],
                "total_episodes": len(pt_data),
                "timeline_vram": [d["reserved_vram_mb"] for d in pt_data],
            }
            print("   -> Successfully parsed 'pytorch_benchmark.json'")

    # 2. Parse Real TensorFlow Baseline Logs
    if os.path.exists("tensorflow_benchmark.json"):
        with open("tensorflow_benchmark.json", "r") as f:
            tf_data = json.load(f)
        if tf_data:
            avg_time = sum(d["step_time_ms"] for d in tf_data) / len(tf_data)
            peak_vram = max(d["reserved_vram_mb"] for d in tf_data)
            dashboard_data["real_runs"]["TensorFlow"] = {
                "avg_step_time_ms": round(avg_time, 2),
                "peak_vram_mb": round(peak_vram, 2),
                "final_loss": tf_data[-1]["loss"],
                "total_episodes": len(tf_data),
                "timeline_vram": [d["reserved_vram_mb"] for d in tf_data],
            }
            print("   -> Successfully parsed 'tensorflow_benchmark.json'")

    # Save output back into the primary workspace dashboard JSON
    with open("research_proposal_benchmarks.json", "w") as f:
        json.dump(dashboard_data, f, indent=4)
    print("[+] Unified 'research_proposal_benchmarks.json' file updated.")


if __name__ == "__main__":
    parse_and_merge_logs()
