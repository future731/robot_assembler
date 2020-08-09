#!/bin/bash
source /my_entrypoint.sh

while true
do
# reset pose
echo "reset pose"
python forth_move_and_check.py

# first
echo "catch start"
python forth_move_with_ball.py

# catch
sleep 3
done
