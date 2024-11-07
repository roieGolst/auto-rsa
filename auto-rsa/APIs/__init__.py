import os
import importlib
import sys

globals_dict = globals()

# Add APIs directory to sys.path
current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_directory)

# Load all Python files in the current directory except __init__.py
modules = [
    f[:-3] for f in os.listdir(current_directory)
    if f.endswith(".py") and f != "__init__.py"
]

for module in modules:
    try:
        module_obj = importlib.import_module(f".{module}", package=__name__)
        globals_dict.update({name: getattr(module_obj, name) for name in dir(module_obj) if not name.startswith("_")})
    except Exception as e:
        raise Exception(f"Failed to load module: {module}. Error: {e}")

print("Successfully loaded all APIs")
