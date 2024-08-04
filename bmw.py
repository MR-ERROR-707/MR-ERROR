import os, platform, time, sys
bit = platform.architecture()[0]
if bit == '64bit':
 os.system("mv _req.cpython-311.so /data/data/com.termux/files/usr/lib/python3.11/_req.cpython-311.so")
 import error
elif bit == '32bit':
 exit(" 32 bit not work 😒")
