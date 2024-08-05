import concurrent.futures
import subprocess

# List of files to run
files_to_run = [
    "Flappy Fitness\\exercises.py",
    "Flappy Fitness\\server.py",
    "Flappy Fitness\\main.py"
]

# Function to run a file
def run_file(file):
    result = subprocess.run(["python", file], capture_output=True, text=True)
    return file, result

# Run files concurrently
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = {executor.submit(run_file, file): file for file in files_to_run}
    for future in concurrent.futures.as_completed(futures):
        file, result = future.result()
        print(f"File: {file}")
        print(f"Return Code: {result.returncode}")
        print(f"Output: {result.stdout}")
        print(f"Error: {result.stderr}")
