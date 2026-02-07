
import os

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    try: 
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.abspath(os.path.join(working_directory, file_path))
        is_outside = os.path.commonpath([working_dir_abs, target_path]) != working_dir_abs
        if is_outside:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
    
        with open(target_path, 'r', encoding='utf-8') as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += "\n... (content truncated to 1000 characters)"
            return content
    
    except Exception as e:
        return f"Error: {e}"