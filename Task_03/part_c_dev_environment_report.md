# Part C – Virtual Environments, Conda Environments & Dependency Isolation

## What is a Virtual Environment?
A virtual environment is an isolated, self-contained Python installation with
its own `site-packages` directory. It lets a project install exactly the
package versions it needs without touching the system-wide Python or any
other project's packages. Python's built-in tool is `venv`
(`python3 -m venv .venv`), which creates a lightweight folder containing a
private copy of the interpreter and `pip`. You activate it
(`source .venv/bin/activate` on macOS/Linux, `.venv\Scripts\activate` on
Windows) and any `pip install` from then on stays inside that folder.

## What is a Conda Environment?
Conda environments (`conda create -n myenv python=3.11`) serve the same
purpose but go a step further: Conda is both a package manager and an
environment manager, and it can install non-Python dependencies too (e.g.
CUDA libraries, compiled C/C++ binaries, R packages). This makes it the
preferred choice for data science and ML stacks (NumPy, Pandas, TensorFlow,
PyTorch) where packages often depend on specific compiled binary versions
that plain `pip`/`venv` cannot resolve as reliably.

## Why Dependency Isolation Matters
- **Avoids version conflicts:** Project A might need `pandas==1.5` while
  Project B needs `pandas==2.1`. Without isolation, installing one breaks
  the other.
- **Reproducibility:** A `requirements.txt` (pip) or `environment.yml`
  (conda) captures the exact versions used, so teammates or CI servers can
  recreate the same environment.
- **Clean system Python:** Keeps the OS-level Python free of project-specific
  clutter, reducing the risk of breaking system tools that depend on it.
- **Safe experimentation:** You can delete and recreate an environment at any
  time without affecting other projects or the system.

## venv vs Conda – Quick Comparison
| Aspect | venv | Conda |
|---|---|---|
| Scope | Python packages only | Python + non-Python binaries/libraries |
| Speed/size | Lightweight | Heavier (full package manager) |
| Package source | PyPI (pip) | Anaconda/conda-forge channels (+ pip) |
| Best for | Pure Python web/backend projects | Data science / ML with compiled deps |
| Config file | `requirements.txt` | `environment.yml` |

## Command Summary
```bash
# venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# conda
conda create -n pkcert-env python=3.11
conda activate pkcert-env
conda install numpy pandas scikit-learn
```

**Conclusion:** Both tools solve the same core problem — isolating a
project's dependencies from every other project and from the system Python —
but Conda is generally favored for AI/ML work because of its ability to
manage compiled, non-Python dependencies alongside Python packages.
