#!/bin/bash

echo
echo
echo "⭐ Installing FRNN"
echo
# git clone --recursive https://github.com/lxxue/FRNN.git src/dependencies/FRNN

# install a prefix_sum routine first
cd src/dependencies/FRNN/external/prefix_sum
pip install .

# install FRNN
cd ../../ # back to the {FRNN} directory
pip install -e .
cd ../../../

echo
echo
echo "⭐ Installing Point Geometric Features"
echo
conda install -c omnia eigen3 -y
export EIGEN_LIB_PATH="$CONDA_PREFIX/include"
python -m pip install git+https://github.com/drprojects/point_geometric_features

echo
echo
echo "⭐ Installing Parallel Cut-Pursuit"
echo
# Clone parallel-cut-pursuit and grid-graph repos
# git clone -b improve_merge https://gitlab.com/1a7r0ch3/parallel-cut-pursuit.git src/dependencies/parallel_cut_pursuit
# git clone https://gitlab.com/1a7r0ch3/grid-graph.git src/dependencies/grid_graph

# Compile the projects
python scripts/setup_dependencies.py build_ext

echo
echo
echo "🚀 Successfully installed SPT"
