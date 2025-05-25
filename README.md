# `stopwatch`

`stopwatch` is a Python package that helps you measure the time taken by code execution. It provides a simple and intuitive way to track performance and optimize your code.

## Todos

- Add templates for PR and issues.
- Deploy to `pypi`
- CI/CD

## Features

### Context Manager

`stopwatch` supports to measure the time taken by a block of code using a context manager.

```python
from stopwatch import Stopwatch

with Stopwatch() as sw:
    ...
print(sw.elapsed)
```

### Decorator

`stopwatch` also supports to measure the time taken by a function using a decorator.

```python
from stopwatch import stopwatch

@stopwatch
def my_function():
    ...
my_function() # Elapsed time: ...
```
