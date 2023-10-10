# Homework Project

The goal of this Homework Project is to create a Python library, which takes in an
array of records of variable size and splits the input to batches of records (array of
arrays) suitably sized for delivery to a system which has following limits:

- maximum size of output record is 1 MB, larger records should be discarded
- maximum size of output batch is 5 MB
- maximum number of records in an output batch is 500

Input for the library is: [\<record1\>, \<record2\>, \<record3\>, ... , \<recordn\>]

Output is: [\<batch1\>, \<batch2\>, ..., \<batchn\>] where each batch is an array of
records just like in the input.

The records can be assumed to be strings of variable length and they have to
pass intact through the system and records should stay in the order that they
arrive.

## Installation

This Homework Project is just an example and cannot be installed via PyPI. In the real world, it could be published e.g. using [Poetry's publish command](https://python-poetry.org/docs/cli/#publish).

## Contribution

This repository uses [Poetry](https://python-poetry.org/). Development requirements
can be installed by

```shell
poetry install --with=dev
```

Next, pre commit hooks needs to be installed. They can be installed by

```shell
poetry run pre-commit install
```

Now static file checks will be ran on each commit or by running

```shell
poetry run pre-commit run -a
```

## Running tests

Unit tests can be run with the following command:

```shell
poetry run python -m unittest
```

## Code quality

This project uses set of development tools to ensure code quality.

| Tool                                       | Description                                   |
| ------------------------------------------ | --------------------------------------------- |
| [pre-commit](https://pre-commit.com/)      | Used to run static file checks on each commit |
| [black](https://github.com/psf/black)      | Used to automate code formatting              |
| [isort](https://pycqa.github.io/isort/)    | Used to automate sorting imports properly     |
| [pylint](https://pypi.org/project/pylint/) | To do static code analyzing                   |
| [mypy](https://github.com/python/mypy)     | To ensure static typing                       |

## Future ideas to implement

The following points are not within the scope of this exercise, but they should be considered if a similar library were to be created in the real world.

- Ensure code quality by setting up GitHub Actions (run static code analysis and unit tests there on each push).
- Automatic releases on push to main (with Github Actions)
- Add more test cases to test all possible corner cases (empty strings, non-utf8 characters, large records, etc.).
- Provide a well-written README.md with clear installation, development, and contribution instructions.
- Tool such Bandit could be considered to find common security issues
