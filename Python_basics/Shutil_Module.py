import shutil, os, time
if os.path.exists("Shutil_Module2.py"):
    os.remove("Shutil_Module2.py")
shutil.copy("Shutil_Module.py", "Shutil_Module2.py")
if os.path.exists("Cluttered Folder Copy"):
    shutil.rmtree("Cluttered Folder Copy")
shutil.copytree("Cluttered Folder", "Cluttered Folder Copy")
