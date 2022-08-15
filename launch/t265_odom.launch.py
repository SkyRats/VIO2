#!/usr/bin/env python3

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, ExecuteProcess, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    """Launch t265 Intel Realsense camera with the px4 bridge"""
    realsense_launch_dir = os.path.join(get_package_share_directory('realsense2_camera'), 'launch')
    bridge_launch_dir = os.path.join(get_package_share_directory('realsense_mav_bridge'), 'launch')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([realsense_launch_dir, '/rs_launch.py'])
        ),
        Node(
            package='realsense_mav_bridge',
            executable='bridge.py',
        ),
])
