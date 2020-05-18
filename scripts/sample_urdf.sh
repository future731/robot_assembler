#!/bin/bash
./run_docker.sh roslaunch robot_assembler robot_assembler.launch ROBOT_NAME:=SAMPLE \
    OUTPUT_DIR:=/userdir START_WITH:=/catkin_ws/src/robot_assembler/sample/SAMPLE.roboasm.l
