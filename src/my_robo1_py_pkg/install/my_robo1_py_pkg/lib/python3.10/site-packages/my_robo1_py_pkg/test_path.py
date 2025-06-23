#!/usr/bin/env python3

from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution
from launch import LaunchContext

desc = PathJoinSubstitution([
    FindPackageShare('my_robo1_py_pkg'),
    'urdf',
    'my_robo1.urdf.xacro'
])

ctx = LaunchContext()
resolved_path = desc.perform(ctx)

print("Resolved path:", resolved_path)

