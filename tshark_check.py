import subprocess
import os
import pyshark
# Option 1: Assuming tshark is in PATH
try:
    subprocess.run(["tshark", "--version"], check=True)
    print("TShark is accessible via PATH.")
except FileNotFoundError:
    print("TShark not found in PATH.")
# Option 2: Using the full path (adjust if your TShark path differs)
tshark_path = "/Applications/Wireshark.app/Contents/MacOS/tshark"
if os.path.exists(tshark_path):
    try:
        subprocess.run([tshark_path, "--version"], check=True)
        print(f"TShark is accessible at {tshark_path}.")
    except Exception as e:
        print(f"Error accessing TShark at {tshark_path}: {e}")
else:
    print(f"TShark not found at {tshark_path}.")