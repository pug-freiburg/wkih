# Wie-kann-ich-helfen Web-App

## Getting started with development

- Prerequisites: git, python
- Clone this repository and cd into its directory
- Run `python bootstrap.py`

**Important:** Make sure you call bootstrap.py with the python version that you
want to use for development. Example: `C:\Python34\python.exe bootstrap.py`

To activate the virtualenv run `$ . venv/bin/activate` on OS X and Linux
or `venv\scripts\activate` on Windows. Deactivate by running `deactivate`

## Starting the development server

You can start the development server with `run`. Open your browser at
`http://localhost:5000` to view the app.

## Developing new features

### repository branches

Please do not push directly to the master branch. Always create a new branch
with git. Feature branches should have a `feat/`-prefix, bugfix branches should
have a `fix/`-prefix. Example:

 * `git checkout -b feat/new_awesome_feature`
 * `git checkout -b fix/fix_for_embrasing_typo`

### writing unit tests

Always write tests for your features. The unit test suite can be found under
`tests/unit`.

### Commiting code to the repository

Before commiting:

 * Run the test suite with `test`
 * Run the linter with `lint`

Don't commit code that doesn't lint, or more importantly doesn't test. Aim to
improve test coverage with every commit.

Don't push to master!

We will probably provide a git hook for this, at some point.

### Integrating code into master branch

Use github to open pull requests from your branch into master. If you have a
mentor ask him to review the code for you before the branch is accepted and
merged.


### Development commands

After bootstrapping these development commands are installed and available:

 - `init` - Install requirements
 - `lint` - Run the linter
 - `run`  - Run the development server
 - `test`  - Run tests
