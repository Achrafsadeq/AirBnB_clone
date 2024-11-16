# 0x00. AirBnB Clone - The Console

## Description
This project is the first step towards building a full web application: an AirBnB clone. This first step consists of a custom command-line interface for data management and the base classes for the storage of this data.

## Requirements

### Python Scripts
* Allowed editors: `vi`, `vim`, `emacs`
* All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All files should end with a new line
* The first line of all files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Code should use pycodestyle (version 2.8.*)
* All files must be executable
* The length of files will be tested using `wc`
* All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)

### Python Unit Tests
* Allowed editors: `vi`, `vim`, `emacs`
* All test files should be inside a folder `tests`
* You have to use the unittest module
* All test files should be python files (extension: `.py`)
* All test files and folders should start with `test_`
* File organization in the tests folder should mirror project structure
* All tests should be executed using: `python3 -m unittest discover tests`
* Can also test file by file using: `python3 -m unittest tests/test_models/test_base_model.py`

## Project Structure
```
AirBnB_Clone/
├── models/
│   ├── __init__.py
│   ├── base_model.py
│   ├── user.py
│   ├── state.py
│   ├── city.py
│   ├── amenity.py
│   ├── place.py
│   └── review.py
├── tests/
│   ├── test_models/
│   │   ├── __init__.py
│   │   ├── test_base_model.py
│   │   ├── test_user.py
│   │   └── ...
├── console.py
├── AUTHORS
└── README.md
```
 
## Mission Director
This project is supervised by the ALX Software Engineering Program.

## Developer
**Codename**: Achraf Sadaeq, Elhoucine Smaili.

## Acknowledgments
Holberton School, in collaboration with the ALX Software Engineering Program, developed this project for educational purposes.
