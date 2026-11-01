import importlib
import os
import shutil

os.makedirs("vendor", exist_ok=True)
for name in ["pytest", "_pytest", "pluggy", "iniconfig", "packaging", "py"]:
    try:
        module = importlib.import_module(name)
    except ImportError:
        print("skipping", name)
        continue
    path = module.__file__
    if os.path.basename(path) == "__init__.py":
        shutil.copytree(os.path.dirname(path), os.path.join("vendor", name), dirs_exist_ok=True)
    else:
        shutil.copy(path, os.path.join("vendor", os.path.basename(path)))
    print("copied", name)
