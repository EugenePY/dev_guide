# Learning Python from making a KLE parser.

### Enviroment Setup
#### package management 

1. [pip](https://github.com/pypa/pip)
2. [tox](https://tox.wiki/en/latest/)
3. [pyenv](https://github.com/pyenv/pyenv)
4. [pytest](https://docs.pytest.org/en/7.2.x/)

References
- [python setup.cfg](https://setuptools.pypa.io/en/latest/userguide/declarative_config.html)

## Installation

```shell
tox --devenv venv-py37 -e py37
```

# How to write a parser from scratch

1. Tokenizer
2. Parser

## Task 
1. Parse the Keyboard Layout Editor format.

[KLE format specs](https://github.com/ijprest/keyboard-layout-editor/wiki/Serialized-Data-Format)

## Writing the Parser

1. Writing a unit test(Failed)(Test Driven Development).
2. Make the failed test passed.
3. Make more failed tests.

Markdown

run `pytest` from commandline at the root dir.

```shell
pytest
```

```python
def function_name(arg, kwarg):
    ...
    a = arg
    return a 
```

```python
class ClassName:
    ...
```


remark: 
    __init__.py file

[regular expression](https://docs.python.org/3/library/re.html)

