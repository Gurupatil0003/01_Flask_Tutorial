## Topics 

- [What is Flask](#what-is-flask)
- [Install Virtual Environment](#Install-Virtual-Environment)
- [How to Install Flask](#install-flask)
- [How check Flask  Version](#Pip-version)
- [A mini_Flask application](#a-minimal-app)
- [Flask Project Structure](#flask-project-structure) - a few options
- (WIP) [Flask Bootstrap Sample](#flask-bootstrap-sample) - a simple project built with Bootstrap
- (WIP) [Jinja Template](#jinja-template) - how to render HTML pages efficiently

<br />

## What is Flask

:point_right: Flask is a lightweight web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.
Compared to [Django](https://www.djangoproject.com/), Flask provides a lightweight codebase and more freedom to the developer.

<br />

<p align="right"><a href="#topics"> :point_up_2: Return to top</a></p>

<br />

## Install Flask

:point_right: The easiest way to install [Flask](https://palletsprojects.com/p/flask/) is to use [PIP](https://pip.pypa.io/en/stable/quickstart/) the official package-management tool.


pip install virtualenv
:point_right: We use a module named virtualenv which is a tool to create isolated Python environments. virtualenv creates a folder that contains all the necessary executables to use the packages that a Python project would need.

-A Python Virtual Environment is an isolated space where you can work on your Python projects, separately from your system-installed Python.

-You can set up your own libraries and dependencies without affecting the system Python.

-We will use virtualenv to create a virtual environment in Python.

-Why do we need a virtual environment?
Imagine a scenario where you are working on two web-based Python projects one of them uses Django 4.0 and the other uses Django 4.1 (check for the latest Django versions and so on). In such situations, we need to create a virtual environment in Python that can be really useful to maintain the dependencies of both projects.

```bash
#Installing Virtula environment
pip install virtualenv
```bash
#Call Virutal Environment and it's  local directory Name  Like--- Venv or Guru or Data etc....
virtualenv venv
```
```bash
#Activate a virtual environment based on your OS
For windows > venv\Scripts\activate
For linux > source ./venv/bin/activate
```



```bash
pip install Flask
```

<br />

**How to check Flask version**

Open a Python console (type python in terminal) and check the installed version as below:

```python 

import flask
flask_version = flask.__version__
print(f"Installed Flask version: {flask_version}")

       Or
flask --version

```

<br />

<p align="right"><a href="#topics"> :point_up_2: Return to top</a></p>

<br />
