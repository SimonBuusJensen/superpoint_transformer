# Use the specified base image
FROM nvidia/cuda:11.8.0-devel-ubuntu20.04

# Avoid interaction with apt-get
ENV DEBIAN_FRONTEND=noninteractive

# Update the repository and install necessary packages (curl, wget etc.)
RUN apt-get update && apt-get install -y --no-install-recommends build-essential curl wget git nano openssh-client

# Make the default shell bash
SHELL ["/bin/bash", "-c"]

# Set username to the local user (simon)
ARG USERNAME=simon
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# ********************************************************
# * Anything else you want to do like clean up goes here *
# ********************************************************

# [Optional] Set the default user. Omit if you want to keep the default as root.
USER $USERNAME

# Set the working directory
WORKDIR /home/$USERNAME

# # Download and install Miniconda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-py38_23.3.1-0-Linux-x86_64.sh -O /home/$USERNAME/miniconda.sh
RUN chmod +x /home/$USERNAME/miniconda.sh

# # Verify that conda is installed with conda --version
RUN /home/$USERNAME/miniconda.sh -b -p /home/$USERNAME/miniconda3
RUN rm /home/$USERNAME/miniconda.sh

# Add conda to the path environment variable
ENV PATH=/home/$USERNAME/miniconda3/bin:$PATH