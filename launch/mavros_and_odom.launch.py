#!/usr/bin/env python3

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, ExecuteProcess, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    """Launch Intel Realsense tracking camera with the px4 bridge AND mavros"""
    bridge_launch_dir = os.path.join(get_package_share_directory('realsense_mav_bridge'), 'launch')
    bridge_launch_dir = os.path.join(get_package_share_directory('mavbase2'), 'launch')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([bridge_launch_dir, '/camera_odom.launch.py'])
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([realsense_launch_dir, '/px4_usb.launch.py'])
        ),
])
