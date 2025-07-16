from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'my_robo1_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        # Resource index
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        
        # Package-level files
        ('share/' + package_name, ['package.xml']),
        # Install launch files
        ('share/' + package_name + '/launch', glob('launch/*.py')),
        # Install URDF/XACRO files
        ('share/' + package_name + '/urdf', glob('urdf/*.xacro')),
        #Install .rviz files
        ('share/' + package_name + '/rviz', glob('rviz/*.rviz')),
        # Install world files
        ('share/' + package_name + '/worlds', glob('worlds/*.world')),
        
    ],
    
    install_requires=['setuptools', 'rclpy', 'std_msgs', 'ament_index_python'],
    zip_safe=True,
    maintainer='namitha',
    maintainer_email='namithasaikolli@gmail.com',
    description='4 wheeled differential drive robot',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'obstacle_stop_node = my_robo1_py_pkg.obstacle_stop_node:main',
        'object_detection_node = my_robo1_py_pkg.object_detection_node:main'
    ],
    },
)
