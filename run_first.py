import subprocess
import sys
import time

def InstallModule(package):
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

print("Installing colorama & Requests")

InstallModule("colorama")
InstallModule("requests")



print("All files have been installed!")


time.sleep(100)
