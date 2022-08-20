# dice-api

A small and fun API for virtual dice rolling needs 🎲

# Installation

Install the required libraries whether in the host itself or in a virtual machine:

```
pip install -r requirements.txt
```

# Run

Run the application with the following command:

```
uvicorn main:app --reload
```

To run without reloading after code changes, remove the `--reload` option

# Test

Run `pytest` to run tests

```
pytest
```