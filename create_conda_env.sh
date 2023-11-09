#!/bin/bash

PROJECT_NAME=spt
PYTHON=3.8
CONDA_DIR=`realpath ~/miniconda3`

echo
echo
echo "⭐ Creating conda environment '${PROJECT_NAME}'"
echo

# Create deep_view_aggregation environment from yml
conda create --name ${PROJECT_NAME} python=${PYTHON} -y

# Activate the env
source ${CONDA_DIR}/etc/profile.d/conda.sh  
conda activate ${PROJECT_NAME}