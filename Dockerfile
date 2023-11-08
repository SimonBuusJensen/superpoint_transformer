# Use the specified base image
FROM nvidia/cuda:11.8.0-devel-ubuntu20.04

# Avoid interaction with apt-get
ENV DEBIAN_FRONTEND=noninteractive

# Update the repository and install necessary packages (curl, wget etc.)
RUN apt-get update && apt-get install -y --no-install-recommends build-essential curl wget git nano 

# Define environment variable
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility

# Make the default shell bash
SHELL ["/bin/bash", "-c"]

# Set the working directory
ENV USERNAME="simon"
WORKDIR /home/$USERNAME

# Copy the entire content of the specified directory into the working directory of the container
COPY . /home/$USERNAME

# # Download and install Miniconda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-py38_23.3.1-0-Linux-x86_64.sh -O /home/$USERNAME/miniconda.sh
RUN chmod +x /home/$USERNAME/miniconda.sh

# Verify that conda is installed with conda --version
RUN /home/$USERNAME/miniconda.sh -b -p /home/$USERNAME/miniconda3
RUN rm /home/$USERNAME/miniconda.sh

ENV DEBIAN_FRONTEND=interactive

# Install the python environment using conda
# Make sure the script is executable
RUN chmod +x install.sh

# Execute the install.sh script
RUN ./install.sh

# Add conda to the path environment variable
ENV PATH=/home/simon/miniconda3/bin:$PATH

# Initialize conda for bash
RUN conda init bash 
RUN bash -c "source ${HOME}/.bashrc" 
RUN conda activate spt