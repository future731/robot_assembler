#!/bin/bash
apt-get update && apt-get install -y ros-melodic-jsk-pcl-ros
source /opt/ros/melodic/setup.bash
roslaunch forth_stereo.launch
