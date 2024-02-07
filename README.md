# Introduction to Python

## Creating a Virtual Environment

This step is optional. You can create and activate a virtual environment using the following commands.

```
python3 -m venv venv
source venv/bin/activate
```

A virtual environment acts as a separate environment which isolates the dependencies of your project from the rest of your system. Different projects can have different or conflicting requirements, so it is recommended to use virtual enviornments, but not necessary. If you don't use a virtual environment, all packages will be installed in the system python.

The environment can be deactivated using `deactivate` command.

## Installing the Dependencies

```
pip install -r requirements.txt
```

This will install all packages listed in the `requirements.txt` file. You can also install them individually using `pip install <package-name>`.

## Running the Code

If `main.py` is the file you want to run, use the following command

```
python main.py
```