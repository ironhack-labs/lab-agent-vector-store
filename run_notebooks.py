"""Execute both deliverables, preserving partial outputs on failure."""
import nbformat
from nbclient import NotebookClient
for path in ('demo-run.ipynb', 'solution.ipynb'):
    print('Executing', path, flush=True)
    notebook = nbformat.read(path, as_version=4)
    try:
        NotebookClient(notebook, timeout=240, kernel_name='python3').execute()
    finally:
        nbformat.write(notebook, path)
    print('Passed:', path, flush=True)
