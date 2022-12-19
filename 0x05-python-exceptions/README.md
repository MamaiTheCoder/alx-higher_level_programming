# Python - Exceptions

ALX project done to facilitate completion of Full Stack Software Engineering course.

## Learning Objectives
* The difference between errors and exceptions.
* Applications of exceptions.
* The purpose of catching exceptions.
* How to raise a builtin exception.
* When we need to implement a clean-up action after an exception

## Technologies
* The Python files were tested on Ubuntu 20.04.
* The Python files have strictly followed [pycodestyle](https://github.com/PyCQA/pycodestyle) coding and documentation styles.
* The C files have strictly followed [Betty](https://github.com/holbertonschool/Betty) coding and documentation styles.
* The C file is compiled with `gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c`

| **Filename** | **Its Functions** |
| ---------- | ---------- |
| [0-safe_print_list.py](https://github.com/MamaiTheCoder/alx-higher_level_programming/blob/main/0x05-python-exceptions/0-safe_print_list.py) | Prints x elements of a list. Test file -> [0-main.py](https://github.com/MamaiTheCoder/alx-higher_level_programming/blob/main/0x05-python-exceptions/0-main.py) |
| [1-safe_print_integer.py](https://github.com/MamaiTheCoder/alx-higher_level_programming/blob/main/0x05-python-exceptions/1-safe_print_integer.py) | Prints an integer with "{:d}".format(). Test file -> [1-main.py](https://github.com/MamaiTheCoder/alx-higher_level_programming/blob/main/0x05-python-exceptions/1-main.py) |
| [2-safe_print_list_integers.py](https://github.com/MamaiTheCoder/alx-higher_level_programming/blob/main/0x05-python-exceptions/2-safe_print_list_integers.py) | Prints the first x elements of a list and only integers. Test file -> [2-main.py](https://github.com/MamaiTheCoder/alx-higher_level_programming/blob/main/0x05-python-exceptions/2-main.py) |
| [3-safe_print_division.py](https://github.com/MamaiTheCoder/alx-higher_level_programming/blob/main/0x05-python-exceptions/3-safe_print_division.py) | Divides 2 integers and prints the result. Test file -> [3-main.py](https://github.com/MamaiTheCoder/alx-higher_level_programming/blob/main/0x05-python-exceptions/3-main.py) |
| [4-list_division.py](https://github.com/MamaiTheCoder/alx-higher_level_programming/blob/main/0x05-python-exceptions/4-list_division.py) | Divides element by element 2 lists. Test file -> [4-main.py](https://github.com/MamaiTheCoder/alx-higher_level_programming/blob/main/0x05-python-exceptions/4-main.py) |
| [5-raise_exception.py](https://github.com/MamaiTheCoder/alx-higher_level_programming/blob/main/0x05-python-exceptions/5-raise_exception.py) | Raises a type exception. Test file -> [5-main.py](https://github.com/MamaiTheCoder/alx-higher_level_programming/blob/main/0x05-python-exceptions/5-main.py)
| [6-raise_exception_msg.py](https://github.com/MamaiTheCoder/alx-higher_level_programming/blob/main/0x05-python-exceptions/6-raise_exception_msg.py) | Raises a name exception with a message. Test file -> [6-main.py](https://github.com/MamaiTheCoder/alx-higher_level_programming/blob/main/0x05-python-exceptions/6-main.py) |
| [100-safe_print_integer_err.py](https://github.com/MamaiTheCoder/alx-higher_level_programming/blob/main/0x05-python-exceptions/100-safe_print_integer_err.py) | Prints an integer. Test file -> [100-main.py](https://github.com/MamaiTheCoder/alx-higher_level_programming/blob/main/0x05-python-exceptions/100-main.py)
| [101-safe_function.py](https://github.com/MamaiTheCoder/alx-higher_level_programming/blob/main/0x05-python-exceptions/101-safe_function.py) | Executes a function safely assuming that `fct` will be always a pointer to a function. Returns the result of the function, Otherwise, returns `None`. Test file -> [101-main.py ](https://github.com/MamaiTheCoder/alx-higher_level_programming/blob/main/0x05-python-exceptions/101-main.py) |
| [102-magic_calculation.py](https://github.com/MamaiTheCoder/alx-higher_level_programming/blob/main/0x05-python-exceptions/102-magic_calculation.py) | Works exactly the same as the Python bytecode |
| [103-python.c](https://github.com/MamaiTheCoder/alx-higher_level_programming/blob/main/0x05-python-exceptions/103-python.c) | contains three C functions that print some basic info about Python lists, Python bytes an Python float objects. |
