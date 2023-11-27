# Use the specified base image
FROM nvidia/cuda:11.8.0-devel-ubuntu20.04

# Avoid interaction with apt-get
ENV DEBIAN_FRONTEND=noninteractive

# Update the repository and install necessary packages (curl, wget etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    wget \
    git \
    nano \
    openssh-client \
    screen

WORKDIR /home/simon

# Download and install Miniconda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-py38_23.3.1-0-Linux-x86_64.sh -O /home/simon/miniconda.sh
RUN chmod +x /home/simon/miniconda.sh
RUN /home/simon/miniconda.sh -b -p /home/simon/miniconda3

# Add conda to the path environment variable
ENV PATH=/home/simon/miniconda3/bin:$PATH

# Create the anaconda environment
RUN conda create --name spt python=3.8

SHELL ["conda", "run", "-n", "spt", "/bin/bash", "-c"]

RUN conda install pip nb_conda_kernels -y
RUN pip install matplotlib
RUN pip install plotly==5.9.0
RUN pip install "jupyterlab>=3" "ipywidgets>=7.6" jupyter-dash
RUN pip install "notebook>=5.3" "ipywidgets>=7.5"
RUN pip install ipykernel
RUN pip3 install torch==2.0.* torchvision --index-url https://download.pytorch.org/whl/cu118
RUN pip install torchmetrics[detection]
RUN pip install torch_geometric==2.3 pyg_lib torch_scatter torch_sparse torch_cluster torch_spline_conv -f https://data.pyg.org/whl/torch-2.0.0+cu118.html
RUN pip install plyfile
RUN pip install h5py
RUN pip install colorhash
RUN pip install seaborn
RUN pip3 install numba
RUN pip install pytorch-lightning
RUN pip install pyrootutils
RUN pip install hydra-core --upgrade
RUN pip install hydra-colorlog
RUN pip install hydra-submitit-launcher
RUN pip install rich
RUN pip install torch_tb_profiler
RUN pip install wandb
RUN pip install gdown

# RUN ./install_external_dependencies.sh
