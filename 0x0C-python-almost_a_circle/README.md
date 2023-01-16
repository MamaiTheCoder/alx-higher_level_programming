# Python - Almost a circle
ALX project done to facilitate completion of Full Stack Software Engineering course.

## Learning Objective
* What is Unit testing and how to implement it in a large project.
* How to serialize and deserialize a Class.
* How to write and read a JSON file.
* Using `*args` and `**kwargs`.
* How to handle named arguments in a function.
## Technologies
* Python Scripts were written with Python 3
* Tested on Ubuntu 20.04 LTS
* The file have strictly followed [pycodestyle](https://github.com/PyCQA/pycodestyle) coding and documentation styles.

## Files

Inside `models` folder:

| Filename | Description |
| -------- | ----------- |
| `__init__.py` | Script that converts the directory as a package |
| `base.py` | Base class of geometrical instances |
| `rectangle.py` | Class that inherits attributes references from `Base` class |
| `square.py` | Class that inherits attributes references from `Square` class |

Each class contains public/private attibutes, class and static methods. Also, these class raise exceptions when is required.

Inside `tests/test_models` folder:

| Filename | Description |
| -------- | ----------- |
| `__init__.py` | Script that converts the directory as a package |
| `test_base.py` | Module that contains unittests to `Base` class |
| `test_rectangle.py` | Module that contains unittests to `Rectangle` class |
| `test_square.py` | Module that contains unittests to `Square` class |
