#!/bin/bash
rostopic pub /fullbody_controller/command std_msgs/Float64MultiArray "
layout:
  dim:
  - label: ''
    size: 4
    stride: 0
  data_offset: 0
data:
    - 1
    - 1
    - -1
    - -1"
