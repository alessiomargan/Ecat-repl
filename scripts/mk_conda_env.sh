#!/bin/bash
#set -euo pipefail

conda env create --file condaenv_repl.yaml
#source $(conda info --base)/etc/profile.d/conda.sh
conda activate repl
conda install -y ipykernel ipywidgets
ipython kernel install --user --name=repl
make install-dev