# realsense_mav_bridge
Ros2 package that enables Intel Realsense tracking cameras to be used with px4 micro-air-vehicle

## Dependencies
* [realsense2-camera](https://github.com/IntelRealSense/realsense-ros)
* [mavbase2](https://github.com/SkyRats/mavbase2) UAV control ros2 package (used only in the ```mavros_and_odom.launch.py```)


## Usage
```ros2 launch realsense_mav_bridge camera_odom.launch.py```