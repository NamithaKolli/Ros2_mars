from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, PathJoinSubstitution, TextSubstitution
from launch_ros.substitutions import FindPackageShare
import os
def generate_launch_description():
    xacro_file = PathJoinSubstitution([
        FindPackageShare("my_robo1_py_pkg"),
        "urdf",
        "my_robo1.urdf.xacro"
    ])
    world_path = PathJoinSubstitution([
    FindPackageShare("my_robo1_py_pkg"),
    "worlds",
    "my_gazebo.world"
])

    robot_description_content = Command([
        TextSubstitution(text="xacro"),
        TextSubstitution(text=" "),
        xacro_file
    ])

    return LaunchDescription([
                              Node(
                                  package="robot_state_publisher",
                                  executable="robot_state_publisher",
                                  output="screen",
                                  parameters=[{"robot_description": robot_description_content}],
                                  ),
        IncludeLaunchDescription(
                                PythonLaunchDescriptionSource([
                                                               PathJoinSubstitution([FindPackageShare('gazebo_ros'), 'launch', 'gazebo.launch.py'])
                                                             ]),
                                launch_arguments={
                                                  'world': world_path
                                                 }.items()
                                ),

        Node(
            package="gazebo_ros",
            executable="spawn_entity.py",
            arguments=[
                       '-topic', 'robot_description',
                       '-entity', 'my_robot',
                       '-x', '0.0',
                       '-y', '0.0',
                       '-z', '0.0',
                       '-Y', '3.14'  # Flips the robot 180 degrees (yaw)
                       ],
            output="screen"
            )
    ])

