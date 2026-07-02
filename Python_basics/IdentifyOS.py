# This program just identifies which Operating System you are currently Working on.
import os
if os.name == 'nt':
    print("You are currently working on a Windows Operating System")
elif os.uname().sysname == 'Linux':
    print("You are currently working on a Linux Operating System")
elif os.uname().sysname == 'Darwin':
    print("You are currently working on a Mac Operating System")

