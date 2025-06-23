from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # Launch argument to control whether RViz should start
    use_rviz = LaunchConfiguration('use_rviz')

    # Node to publish joint states (required for TF computation)
    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output='screen'
    )

    # Node to publish transforms from URDF
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': Command([
                'xacro ',
                PathJoinSubstitution([
                    FindPackageShare('my_robo1_py_pkg'),
                    'urdf',
                    'my_robo1.urdf.xacro'
                ])
            ])
        }]
    )

    # RViz visualization node (optional)
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', PathJoinSubstitution([
            FindPackageShare('my_robo1_py_pkg'),
            'urdf',
            'default.rviz'
        ])],
        condition=use_rviz
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_rviz',
            default_value='true',
            description='Whether to open RViz automatically'
        ),
        joint_state_publisher,
        robot_state_publisher,
        rviz_node
    ])

