# dice-api

A small and fun API for virtual dice rolling needs 🎲

For a sample roll, try the following locally:

```
http://127.0.0.1:8000/dice/
```

To roll one's own set of dice, use the `dice` query parameter, for example:

```
http://127.0.0.1:8000/dice/?dice=d4,d6,d6
```

Valid dice include:

```
d4,d6,d8,d10,d12,d20
```

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

# Documentation

Auto-generated and interactive list of available routes is located at `/docs`, for example:

```
http://127.0.0.1:8000/docs
```

# Test

Run `pytest` to run tests

```
pytest
```