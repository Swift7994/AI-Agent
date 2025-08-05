import pathlib
import subprocess
from config import subprocess_timeout


def run_python_file(working_directory, file_path, args=[]):
    try:
        base_path = pathlib.Path(working_directory).resolve()
        target_path = (base_path / pathlib.Path(file_path)).resolve()

        is_outside = not target_path.is_relative_to(base_path)
        if is_outside:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        exists = target_path.exists()
        if not exists:
            return f'Error: File "{file_path}" not found.'
        if target_path.suffix != '.py':
            return f'Error: "{file_path}" is not a Python file.'
        
        command = ['python3', str(target_path)] + args
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            cwd=base_path,
            timeout=subprocess_timeout,
        )

        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        if not stdout and not stderr:
            return "No output produced."
        
        output = []
        if stdout:
            output.append(f"STDOUT:\n{stdout}")
        if stderr:
            output.append(f"STDERR:\n{stderr}")
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        return "\n".join(output)
    
    except Exception as e:
        return f"Error: executing Python file: {e}"