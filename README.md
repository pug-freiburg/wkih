# Wie-kann-ich-helfen Web-App

## Getting started with development

- Prerequisites: git, python, pip and virtualenv
- Clone this repository
- Create and activate a virtualenv
- Install requirements with `bin/init`

## Starting the development server

You can start the development server with `bin/run`. Open your browser at
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

 * Run the test suite with `bin/test`
 * Run the linter with `bin/lint`

Don't commit code that doesn't lint, or more importantly doesn't test. Aim to
improve test coverage with every commit.

Don't push to master!

We will probably provide a git hook for this, at some point.

### Integrating code into master branch

Use github to open pull requests from your branch into master. If you have a
mentor ask him to review the code for you before the branch is accepted and
merged.
