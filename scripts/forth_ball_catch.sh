#!/bin/bash
source /my_entrypoint.sh

# reset pose
echo "reset pose"
python forth_move_and_check.py

# first
echo "catch start"
python forth_move_with_ball.py

# catch
sleep 3

# reset pose
echo "reset pose"
python forth_move_and_check.py

# second
echo "catch start"
python forth_move_with_ball.py
sleep 3

# reset pose
echo "reset pose"
python forth_move_and_check.py
