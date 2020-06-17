source /opt/ros/melodic/setup.bash
rosservice call /gazebo/reset_world
sleep 1

rosservice call /gazebo/set_model_state "model_state:
  model_name: 'ra_ball_large'
  pose:
    position: {x: 0.0, y: 3.0, z: 0.01}
    orientation: {x: 0.0, y: 0.0, z: 1.0, w: 0.0}
  twist:
    linear: {x: 0.0, y: 0.0, z: 0.0}
    angular: {x: 0.0, y: 0.0, z: 0.0}"

sleep 1

rosservice call /gazebo/apply_body_wrench "body_name: 'ra_ball_large::link'
wrench:
  force: {x: -1.2, y: -30.0, z: 0.0}
  torque: {x: 0.0, y: 0.0, z: 0.0}
start_time: {secs: 0, nsecs: 0}
duration: {secs: 0, nsecs: 10000000}"

