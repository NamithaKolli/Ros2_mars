import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/namitha/ros2_ws/src/my_robo1_py_pkg/install/my_robo1_py_pkg'
