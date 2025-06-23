__MY 4 WHEELED DIFFERENTIAL DRIVE ROBOT__

__STRUCTURE AND USAGE OF MY PACKAGE:__

__Packange_name:my_robo1_py_pkg__

__NOTE: google drive has compressed and automatically reduced the quality of video through link for best resolution please download the video before watching through this link .__

[▶️ demo video of my robot](https://drive.google.com/file/d/1EaPIZRA7TgUogHMNSCsFIpUKumJd2ER6/view?usp=sharing)

__Package structure:__

my_robo1_py_pkg/

├── launch/

│   ├── my_gazebo.launch.py

│   └── my_robo1.launch.py

│

├── urdf/

│   └── my_robo1.urdf.xacro

│

 ── worlds/

│   └── my_gazebo.world

│

├── my_robo1_py_pkg/                  # Python module directory

│   ├── __init__.py

│   └── obstacle_stop_node.py

│

├── package.xml

└── setup.py

__How to view the robot?__



1. __To visualize robot and in RViz:__

      Command: ```
               ros2 launch my_robo1_py_pkg my_robo1.launch.py
               ```

      The following are the parameters to set in RViz window:

       
Fixed_frame : dummy_root (because rviz gives an error if root link has              inertial tag)
      ADD->robot model -> in description topic type “robot_description”
   
To view the camera image of robot in rviz follow step 2 and     ADD->Ima
   
2. __To simulate robot in Gazebo.__

    Command:```ros2 launch my_robo1_py_pkg my_gazebo[.launch.py](.launch.py)```


    This command spawns the robot in gazebo.

3. __To run the obstacle stop node:__

    After step 2 in a new terminal run the obstacle_stop_node.

    Command: ```ros2 run my_robo1_py_pkg obstacle_stop_node```

4. __To manually control the robot using teleop_twist_keyboard:__

    After step 2 in a new terminal , run the teleop twist keyboard it publishes velocity commands to the topic cmd_vel which are read by gazebo.

5. __To view the camera image of robot in rviz2:__

    Run step 2 to open  gazebo , we can place some objects available in the gazebo window. Open rviz2 and set parameters as mentioned in step 1 but instead of robot mode add image.


__What is a differential drive Robot?__



* Differential drive robots are easy to build and control robots which follow simple kinematics.
* The motion of the wheels is determined by two main wheels which control the motion and direction of other wheels (if any) and the entire robot.

__WHAT IS URDF ?__



* Unified robotics description format (URDF) is an extensible markup language (XML file) that is used to create a physical description of a robot.
* In URDF we can define a robot’s body ,links like joints,properties like inertia ,collision geometry etc.
* The main purpose of URDF IS:
1. Describe how a robot looks (its structure).
2. Define How parts of a robot move (kinematic).
3. Provide collision and inertial properties for simulation (Gazebo).

__XACRO:__



* Using xacro we can make the urdf file more compact ,readable and easy to edit by using constants and macros.

__XML:__



* Extensible markup language (XML) is a language similar to HTML and is exclusively created for data transfer between two processes or applications.
* It is called extensible because we can extend the tags to any number of user defined tags  unlike HTML which uses predefined tags.
* XML validation ensures its structure is created according to a predefined schema like DTD or XSD.
* 

__Syntax:__

1.__Root Tag__

2. __XML prolog__

3.__Tags__ (All elements must have a closing tag,and they are case sensitive)

4.__Attributes__(Must be quoted):attributes are name-value pairs added to an element’s start tag to provide additional information about that element.

5.__Entity Reference__ :some characters have defined meaning in XML and they cannot be used to define elements that some entity references are used for.


<table>
  <tr>
   <td>Character
   </td>
   <td>Entity reference
   </td>
  </tr>
  <tr>
   <td>&
   </td>
   <td>&amp
   </td>
  </tr>
  <tr>
   <td>>
   </td>
   <td>&lt
   </td>
  </tr>
  <tr>
   <td>&lt;
   </td>
   <td>&gt
   </td>
  </tr>
  <tr>
   <td>“
   </td>
   <td>&quot
   </td>
  </tr>
  <tr>
   <td>‘
   </td>
   <td>&apos
   </td>
  </tr>
</table>


6.__Comments__ :&lt;!-- This is a comment - ->

__Transforms , robot_state_publisher , joint_state_publisher:__

Robots have many parts: wheels, arms, sensors, grippers, cameras, etc.Each part:



* Has its own coordinate frame
* Is connected to other frames by joints
* Joints move, rotate, or translate in space.

ROS uses TFs to keep track of all the frames and how they relate to each other over time.TFs represent the position and orientation of one coordinate frame relative to another.



* Joint_state_publisher_gui scans the urdf and creates sliders to control movable joints and when sliders are moved it publishes joint positions of message type [sensor_msgs/msg/JointState](https://github.com/ros2/common_interfaces/blob/eloquent/sensor_msgs/msg/JointState.msg) to the joint_states topic
* robot_state_publisher subscribes to this topic and uses those positions + URDF to generate TF’s. Basically it uses the joint positions sent by joint_state_publisher to broadcast the pose (position+orientation) of each link.
* Rviz uses these TF’s to display the robot.

__What are meshes?__

 __mesh__ is a 3D model made up of __lots of tiny triangles__ (or polygons) that together form the shape of an object.

Meshes are stored in 3D file formats like .stl,.dae,.obj.

It's used to make robot parts look realistic in simulation.

Interpolation used to make these shapes and parts look more smooth and realistic.



* __PROCEDURE:__
1. __Package: __I created a package my_robo1_py_pkg in my ROS 2 workspace.
* __Command:__ros2 pkg create --build-type ament_python my_robo1_py_pkg
* __(Include dependencies)Command:__ros2 pkg create --build-type ament_python my_robo1_py_pkg --dependencies rclpy std_msgs

    Dependencies can also be added later in the setup.py file.

2. __URDF/XACRO: __I have written a URDF xacro file for the physical appearance of the robot.
* The physical appearance and behaviour is defined by the tags &lt;visual> and &lt;collision>.
* Also used properties  in xacro to define some aspects of the robot like size, weight and  used macro to define wheels.
* The URDF file has a main base_link .
* Rviz was showing some error because the main root link cannot have inertia so I have made a dummy_root which is connected to base_link.
* The visual tag is used to define the geometry and appearance of the mode .It has sub elements in it like material , geometry etc.
* The collision tag is used to define the collision properties of the robot for simulation most of the time we would want to keep the collision properties similar to visual but here are the reasons why we shouldn't some times:
1. Because collision simulation of meshes is very complex and computationally heavy.
2. Sometimes we want to keep the parts of the robot safe by creating a collision geometry which encloses the main robot .
* Inertial tag is used to define the mass and other properties  for better simulation.
* I haven't added any meshes or textures to my robot because its my first time and keeping it simple will make learning easier.

       

3. __Launch File:__

__my_robo1.launch.py:__ this launch file does the following:

__urdf_path →__ Gets a path to the  .xacro file using FindPackageShare.

__robot_description_content→__ Run xacro to generate URDF at runtime.

__robot_description→__ Dictionary that holds the URDF content to share       with nodes.

__LogInfo→__ Prints the URDF path to the terminal (for debug/checking).

__robot_state_publisher Node→__ Publishes transforms (TFs) from URDF to simulate robot pose.

__joint_state_publisher_gui Node →__  GUI sliders to move joints manually for testing and publishes the joint positions .

__rviz2 Node→__  Launches  RViz to visualize the robot.

__my_gazebo.launch.py:__ This launch file loads my robot's URDF (via Xacro), starts Gazebo with my custom world, and spawns the robot automatically.



4. __Package.xml:__ the package.xml must include all build and execution dependencies 
5. __setup.py:__ This file is like a blueprint for installing a package It tells ROS and Python:
* Name of the package.
* What files to include
* What the  package depends on
* Which Python scripts should run as nodes (like obstacle_stop_node)
* Where to install  files (like launch, URDF, RViz, world files).
6. __Gazebo:__
* To simulate this robot in gazebo I specified the plugin __libgazebo_ros_diff_drive.so__ which is best to use for simulation of simple robots.But this plugin works for simulation in gazebo only.
* __Ros2_control__ provides a full robot control framework that works with both Gazebo + real hardware, but requires manual YAML, URDF, controller setup, nodes, launch config.
* Using __libgazebo_ros_diff_drive.so__ we can control the robot as it automatically subscribes to cmd_vel topic .However to control the robot in ros2_control we must manually configure and set up the controllers.
* __Libgazebo_ros_diff_drive.so__ reads ;wheels joints from urdf but ros2_control require transmission tags to be added as interface.
7. __Lidar Plugin:__
* I have used the libgazebo_ros_ray_sensor.so plugin.
* This plugin : 
1. Uses a ray-casting engine in Gazebo to measure distances to nearby objects.
2. Sends out sensor_msgs/msg/LaserScan messages to ROS, just like a real LIDAR.
3. We can configure angle, resolution, range, and number of rays (like real LIDARs).
4. The messages it sends can be consumed by RViz, navigation stacks, or  own custom nodes (like obstacle stop).

8.__Camera Plugin:__



* Captures visual data from the robot’s perspective inside Gazebo.
* Sends image frames (usually as sensor_msgs/msg/Image) to ROS.

__Errors I faced:__



* __TF not found: __Rviz was showing the error tf not found because robot_state_publisher was not receiving the correct urdf model there were some syntax errors in the file.
* Why should root_link be fixed?
* __Invalid xacro call in command() :__ There were some space issues due to which the address of xacro was concatenated to one string which showed the error:

         file not found: [Errno 2] No such file or directory: 'bash-cxacro'



* __Joint_state_publisher waiting for robot_description: __during runtime I continuously got the error :

    ```"Waiting for /robot_description to be set" ```


    Because I passed the robot description as a parameter only to robot_state_publisher but it should also be set as a parameter to the joint_state_publisher node .

* In RViz update interval was set to 0 and alpha was also too low so changed the values to 0.1 and 1 respectively.In description topic I set the topic to robot_description.
* Order in which i launch nodes in the launch file.
* Did not add the ros2_control tags so ros2_control couldn’t identify hardware ,joints etc
* Message type in lidar : at first I added the lidar plugin but ito make the obstacle_stop_node work i was facing some silent errors  it was subscribing to cmd_vel topic but publisher count was 0 so it was something was wrong with the plugin .Later i realised the message type was set to 2 different types and i had to manually force se the message type in the plugin.
