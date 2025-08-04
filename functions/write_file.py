import pathlib

def write_file(working_directory, file_path, content):
    try:
        base_path = pathlib.Path(working_directory).resolve()
        target_path = (base_path / pathlib.Path(file_path)).resolve()
        is_outside = not target_path.is_relative_to(base_path)
        if is_outside:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        exists = target_path.exists()
        if not exists:
            target_path.parent.mkdir(parents=True, exist_ok=True)
            target_path.touch()
        target_path.write_text(content)
    except Exception as e:
        return f"Error: {str(e)}"
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'