import pathlib



def get_files_info(working_directory, directory="."):
    try:
        base_path = pathlib.Path(working_directory).resolve()
        target_path = (base_path / pathlib.Path(directory)).resolve()
        is_outside = not target_path.is_relative_to(base_path)
        label = directory if directory != "." else "current"
        if is_outside:
            return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"
        if not target_path.is_dir():
            return f"Error: '{directory}' is not a directory"
        lines = []
        for child in target_path.iterdir():
            size = child.stat().st_size
            is_dir = child.is_dir()
            lines.append(f"- {child.name}: file_size={size} bytes, is_dir={is_dir}")
        info = "\n".join(lines)
        return info
    except Exception as e:
        return f"Error: {str(e)}"