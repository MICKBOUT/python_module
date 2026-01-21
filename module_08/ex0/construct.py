import sys
from site import getsitepackages


in_matrix = sys.prefix != sys.base_prefix

print("MATRIX STATUS:",
      "Welcome to the construct" if in_matrix else "You're still plugged in")
print()

print("Current Python:", sys.executable)
print("Virtual Environment:", sys.prefix if in_matrix else "None Detected")
print()

if in_matrix:
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")

    print("Package installation path:")
    print(getsitepackages()[0])

else:
    print("To enter the construct, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate", "# On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate", "# On Windows")
    print("\nThen run this program again.")
