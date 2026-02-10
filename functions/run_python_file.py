import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try: 
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.abspath(os.path.join(working_directory, file_path))

        is_outside = os.path.commonpath([working_dir_abs, target_path]) != working_dir_abs
        if is_outside:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        

        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not target_path.endswith('.py'):
            return f'Error: Cannot execute "{file_path}" is not a Python file'

        command = ["python3", target_path]
        if args:
            command.extend(args)
        
        result = subprocess.run(command, capture_output=True, text=True, timeout=30)

        parts = []
        if result.returncode != 0: 
            parts.append(f"Process exited with code {result.returncode}")
        
        stdout_txt = result.stdout.strip() if result.stdout else ""
        stderr_txt = result.stderr.strip() if result.stderr else ""

        if not stdout_txt and not stderr_txt:
            parts.append("No output produced")
        else: 
            if stdout_txt:
                parts.append(f"STDOUT:\n{stdout_txt}")
            if stderr_txt:
                parts.append(f"STDERR:\n{stderr_txt}")

        return "\n".join(parts)
    except Exception as e:
        return f"Error: executing Python file: {e}"




schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file relative to a working directory with optional arguments. Performs security checks to prevent execution outside the working directory and only allows .py files.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Relative path to the Python (.py) file to execute within the working directory."
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional list of command-line arguments to pass to the Python script."
            )
        },
        required=["file_path"]
    )
)
