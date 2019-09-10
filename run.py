# 1. I need to create all of the containers from the same image
# 2. I need to run vpp inside all of the dockers using all of the correct configurations!
# 3. I need to create and test the memif interfaces

import commands
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-i", "--image", dest="image_id",
                    help='ID of the image to be used to create the container')
parser.add_argument("-n", "--name", dest="container_name",
                    help='Name of the new container to be created using this image')
args = parser.parse_args()

CONTAINERS = ['aa', 'bb', 'cc']
IMAGE_ID = args.image_id
CONTAINER_NAME = args.container_name

RUN_COMMAND = 'sudo docker run -it --entrypoint=/bin/bash -i --rm --name {container_name} --hostname {container_name} ' \
              '--privileged -v "/run/vpp/:/run/vpp/" -v "/home/mojtaba/:/home/" -d {image_id}'


for name in CONTAINERS:
    command = RUN_COMMAND.format(image_id=IMAGE_ID, container_name=name)
    print(command)
    result = commands.getstatusoutput(command)


# 2. attaching and running VPP
RUN_VPP = 'sudo docker exec {container_name} vpp -c /home/github-docker-experiment/in-band-OAM-Performance-Evaluation/configurations/{configuration_name}'
for name in CONTAINERS:
    configuration_name = name[0] + '-startup.conf'
    command = RUN_VPP.format(container_name=name, configuration_name=configuration_name)
    print(command)
    result = commands.getstatusoutput(command)
    print(result)

