
import os
from google.genai import types


def write_file(working_directory, file_path, content):
        try: 
            working_dir_abs = os.path.abspath(working_directory)
            target_path = os.path.abspath(os.path.join(working_directory, file_path))

            is_outside = os.path.commonpath([working_dir_abs, target_path]) != working_dir_abs
            if is_outside:
                return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
            
            if os.path.isdir(target_path):
                return f'Error: Cannot write to "{file_path}" as it is a directory'
        
            with open(target_path, 'w') as f:
                f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        except Exception as e:
            return f'Error: {str(e)}'



schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes text content to a file path relative to a pre-defined working directory. Prevents writing outside the permitted directory and disallows writing to directories.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Relative path of the file to write within the permitted working directory."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Text content to write into the file."
            )
        },
        required=["file_path", "content"]
    )
)
