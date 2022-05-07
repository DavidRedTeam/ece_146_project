import os
import subprocess

os.system ("start /B start cmd.exe @cmd /k py server.py")
os.system ("start /B start cmd.exe @cmd /k py router3.py")
os.system ("start /B start cmd.exe @cmd /k py router2.py")
os.system ("start /B start cmd.exe @cmd /k py router1.py")
os.system ("start /B start cmd.exe @cmd /k py Client.py")
