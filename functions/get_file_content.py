import pathlib
from config import file_character_limit

def get_file_content(working_directory, file_path):
    try:
        base_path = pathlib.Path(working_directory).resolve()
        target_path = (base_path / pathlib.Path(file_path)).resolve()
        is_outside = not target_path.is_relative_to(base_path)
        if is_outside:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not target_path.is_file():
            return f'Error: File not found or is not a regular file: "{file_path}"'
        file_contents = target_path.read_text()
        if len(file_contents) > file_character_limit:
            return file_contents[:file_character_limit] + f'[...File "{file_path}" truncated at {file_character_limit} characters]'
        return file_contents
    except Exception as e:
        return f"Error: {str(e)}"