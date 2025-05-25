# `clocker`

`clocker` is a Python package that helps you measure the time taken by code execution. It provides a simple and intuitive way to track performance and optimize your code.

## Todos

- Implement basic functionality.
- Add templates for PR and issues.
- Deploy to `pypi`
  - Add `LICENSE`
  - Add `pyproject.toml`
- CI/CD

## Features

### Context Manager

`clocker` supports to measure the time taken by a block of code using a context manager.

```python
from clocker import clock

with clock() as sw:
    ...
print(sw.elapsed)
```

### Decorator

`clocker` also supports to measure the time taken by a function using a decorator.

```python
from clocker import clock

@clock
def my_function():
    ...
my_function() # Elapsed time: ...
```
