from launch import LaunchDescription
from launch.actions import LogInfo
from launch.substitutions import Command, PathJoinSubstitution, TextSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    urdf_path = PathJoinSubstitution([
        FindPackageShare('my_robo1_py_pkg'),
        'urdf',
        'my_robo1.urdf.xacro'
    ])

    robot_description_content = Command([
        TextSubstitution(text='xacro '), urdf_path
    ])

    robot_description = {'robot_description': robot_description_content}

    return LaunchDescription([
        LogInfo(msg=urdf_path),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[robot_description]
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher',
            output='screen',
            parameters=[robot_description]
        )
    ])
