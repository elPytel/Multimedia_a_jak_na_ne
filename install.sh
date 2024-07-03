#!/bin/bash
# By Pytel

# Install dependencies for the project

python_dependencies="requirements.txt"
apt_dependencies="apt-dependencies.txt"

# Install apt dependencies
sudo apt-get update
xargs sudo apt-get -y install < $apt_dependencies

# Install python dependencies
pip install -r $python_dependencies

echo -e "Done!"