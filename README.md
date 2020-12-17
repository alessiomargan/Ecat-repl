## Getting started

install anaconda https://docs.anaconda.com/anaconda/install/

# prepare a conda env 

conda env create --file condaenv_repl.yaml
conda activate repl
conda install -y ipykernel ipywidgets
ipython kernel install --user --name=repl

# install package

make install-dev

# Jupyter notebooks

