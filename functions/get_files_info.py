import pathlib
from google.genai import types


def get_files_info(working_directory, directory="."):
    try:
        base_path = pathlib.Path(working_directory).resolve()
        target_path = (base_path / pathlib.Path(directory)).resolve()
        is_outside = not target_path.is_relative_to(base_path)
        if is_outside:
            return f'Error: Cannot read "{directory}" as it is outside the permitted working directory'
        if not target_path.is_dir():
            return f'Error: "{directory}" is not a directory'
        lines = []
        for child in target_path.iterdir():
            size = child.stat().st_size
            is_dir = child.is_dir()
            lines.append(f"- {child.name}: file_size={size} bytes, is_dir={is_dir}")
        info = "\n".join(lines)
        return info
    except Exception as e:
        return f"Error: {str(e)}"
    

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)