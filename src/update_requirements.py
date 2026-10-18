# update_requirements.py
import os
import re


def update_repository_requirements():
    print("=" * 65)
    print("      AUTOMATED COMPILER: REQUIREMENTS MANIFEST GENERATOR      ")
    print("=" * 65)

    # 1. Base dependency ecosystem map
    dependency_registry = {
        "torch": "torch>=2.2.0",
        "tensorflow": "tensorflow>=2.15.0",
        "transformers": "transformers>=4.38.0",
        "peft": "peft>=0.9.0",
        "bitsandbytes": "bitsandbytes>=0.42.0",
        "opacus": "opacus>=1.4.0",
        "numpy": "numpy>=1.24.0",
        "streamlit": "streamlit>=1.31.0",
        "pytest": "pytest>=8.0.0",
    }

    detected_packages = set()
    import_pattern = re.compile(r"^\s*(?:import|from)\s+([a-zA-Z0-9_]+)")

    # 2. Crawl files to isolate internal imports
    print("[+] Scanning repository source nodes...")
    for root, _, files in os.walk("."):
        # Exclude environment containers and hidden structures
        if any(p in root for p in ["venv", ".venv", ".git", ".github"]):
            continue

        for file in files:
            if file.endswith(".py") and file != "update_requirements.py":
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        for line in f:
                            match = import_pattern.match(line)
                            if match:
                                root_package = match.group(1)
                                if root_package in dependency_registry:
                                    detected_packages.add(root_package)
                except Exception as e:
                    print(f"    [!] Read breakdown on file {file_path}: {e}")

    # 3. Compile output file text map
    if detected_packages:
        lines_to_write = [dependency_registry[pkg] for pkg in sorted(detected_packages)]

        with open("requirements.txt", "w", encoding="utf-8") as req_file:
            for line in lines_to_write:
                req_file.write(f"{line}\n")

        print(f"[SUCCESS] Isolated {len(detected_packages)} external target libraries.")
        print("[+] Manifest written successfully to 'requirements.txt':")
        for line in lines_to_write:
            print(f"    » {line}")
    else:
        print("[WARN] No standard deep learning infrastructure dependencies detected.")

    print("=" * 65 + "\n")


if __name__ == "__main__":
    update_repository_requirements()
