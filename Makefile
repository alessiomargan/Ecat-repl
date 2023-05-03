.PHONY: all install-dev test coverage cov test-all tox docs release clean-pyc mk-conda-env rm-conda-env up-conda-env

all: test

install-dev:
	pip install -q -e .[dev]

test: clean-pyc install-dev
	pytest

coverage: clean-pyc install-dev
	coverage run -m pytest
	coverage report
	coverage html

cov: coverage

test-all: install-dev
	tox

tox: test-all

docs: clean-pyc install-dev
	$(MAKE) -C docs html

release:
	python scripts/make-release.py

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

###################
# Conda Enviroment
###################

CONDA_ENV_NAME ?= repl
CONDA_YAML = condaenv_repl.yaml
ACTIVATE_ENV = conda activate $(CONDA_ENV_NAME)

mk-conda-env:	## Build the conda environment
	conda env create --quiet --file $(CONDA_YAML)
	$(ACTIVATE_ENV)

rm-conda-env:  ## Remove the conda environment and the relevant file
	conda remove --name $(CONDA_ENV_NAME) --all

up-conda-env:
	conda env update --file $(CONDA_YAML) --prune
	$(ACTIVATE_ENV)
