# in-band OAM Performance Evaluation
This repository contains the files for the performance evaluation of i-OAM research effort (Telecom Paristech, University of Leige, Cisco)


* We have used a manipulated version of Ligato https://github.com/ligato/vpp-base repository in this experiment

# Building the docker image inside the vpp-base repository:
docker build -t custom-vpp .

# Run the experiment using the run.py
Usage:
In order to get help use:
python2 run.py --help

To run the experiment:
python2 run.py --image custom-vpp

# Attach to the docker containers:
sudo docker exec -it aa bash
sudo docker exec -it bb bash
sudo docker exec -it cc bash

# Resetting the experiment and deleting containers:
Use docker stop and docker rm commands to delete container
