# ping_test.py - A simple script to ping 1.1.1.1
import subprocess
import platform

# Determine the ping flag based on OS (-n for Windows, -c for Linux/Mac)
flag = "-n" if platform.system().lower() == "windows" else "-c"

# Ping 1.1.1.1 four times
print("Pinging 1.1.1.1...")
result = subprocess.run(["ping", flag, "4", "1.1.1.1"], capture_output=True, text=True)

# Print the output
print(result.stdout)

if result.returncode == 0:
    print("Ping successful!")
else:
    print("Ping failed!")
