import win32serviceutil
import ctypes
import sys


def adminperms():
    if ctypes.windll.shell32.IsUserAnAdmin():
        return  # Already admin, continue with the rest of the script.
    
    params = " ".join(f'"{arg}"' for arg in sys.argv)
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
    sys.exit()  # Exit to restart with elevated privileges.

if not ctypes.windll.shell32.IsUserAnAdmin():
    adminperms()

OVR = "OVRService"
try:
    win32serviceutil.StopService(OVR)
except:
    print("Error stopping OVRService, the service might have stopped already or doesn't exist.")
    response = input("start service again? y/n")
    if (response.lower() == "y"):
        win32serviceutil.StartService(OVR)
    else:
        print("service stopped.")