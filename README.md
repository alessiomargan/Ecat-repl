## Getting started

install anaconda https://docs.anaconda.com/anaconda/install/

# prepare a conda env 

conda env create --file condaenv_repl.yaml
conda activate repl
conda install -y ipykernel ipywidgets
ipython kernel install --user --name=repl

# check kernel python path 

check in $HOME/.local/share/jupyter/kernels/repl/kernel.json

{
 "argv": [
  "/home/amargan/work/anaconda3/envs/repl/bin/python",
  "-m",
  "ipykernel_launcher",
  "-f",
  "{connection_file}"
 ],
 "display_name": "repl",
 "language": "python"
}


# install ecat-repl package

make install-dev

# Jupyter notebooks
