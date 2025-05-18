LEARNING ROS-2

* __Version of ROS 2 and Ubuntu__
* From the ROS 2 documentation and as per mars team members suggestion I  have used the ROS 2 Humble Hawksbill version . Though Jazzy Jalisco is the newer version ,It is less stable and does not provide Long term support.
* I have dual booted my windows with Ubuntu 22.04.02 Jammy jellyfish LTS as it is mentioned in the document that ROS 2 Humble Hawksbill version provides official binary packages (precompiled,ready to install software packages and libraries) and is best compatible with this version of ubuntu.
* During the process I mistakenly dual booted the noble numbat version and realised I had to use docker for installing ROS 2 but decided deleting and dual booting again was much easier because it's my first time learning ROS and using Docker might make some things harder . So, In total I dual booted my laptop 3 times after starting mars!
* __WHY ROS?__

* ROS is all about making the process of building robots easier and more efficient.

* It is a brilliant software that makes innovation and creativity more accessible to all.

* Instead of learning or doing all parts of the robot building process simply downloading and understanding how to use the libraries will do most of the work.

* ROS is language agonistic which means it’s communication system doesn’t depend on any particular programming language thus any person trying to build a robot doesn’t have to waste time learning a completely new programming language.



* __ROS 2 Installation process__
* Ubuntu deb packages: these packages help installing softwares in Ubuntu easier.
* __Setting Locale:__ it is necessary to check if the locale is set to UTF 8 or maybe POSIX if we are using a docker.

	I am not using docker so I had to change locale settings using the commands given in the ROS 2 documentation.(Screenshot setting locale)

* __Repositories:__ these are servers which contain a set of packages .

	Most of the work can be done using Ubuntu repositories.


	They are of 4 types:

1. __Main:__ free and open software canonical supported (canonical.ltd is the company behind ubuntu so all the updates and safety are well taken care of).
2. __Universe:__ free and open source community maintained but supported by ubuntu any software updates or problems are forwarded to the authors by the ubuntu team.
3. __Restricted:__  not open source but supported by ubuntu any software updates or problems are forwarded to the authors by the ubuntu team.
4. __Multiverse:__ not open source not supported by canonical.(risky)\
* Installing softwares from repositories is not only about installing it to our computers but it’s also about __“how much and what kind of changes (updates) I am okay with over time?”__
* __Ubuntu repositories:__
1. __$release__ :No changes unless critical
2. __$release-security:__ allow only security related updates
3. __$release-updates:__ accept stable bug-fixes.
4. __$release-backports:__ accept new releases from future versions which can be safely adapted by the user ubuntu version.
5. __$devel:__ mostly used by professional developers who can handle any system failure .
* __Installing ROS:__
1. Ensure the Ubuntu universe repository is enabled.
     __ Command:```grep ^deb /etc/apt/sources.list | grep universe``` __



2. Update and upgrade as installation of ROS 2 dependencies might remove or damage some of the critical system packages.(screenshot update & upgrade)
3. __Command: ```sudo apt install ros-humble-desktop```__
4. Setting up the environment so that the ROS commands are recognized by the terminal.
5.
 __Command__: __```source /opt/ros/humble/setup.bash``` __

before running the above command we have to check the shell we are using
__Command__: __```echo $SHELL```__

  	 
6. Additionally I have also made ROS 2 available in all terminals by using

__Command:``` echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc```__



* To use deb packages root access from the system administrator/user for personal computers is necessary, as the packages make changes to the system.
* __Setting up my ROS 2 environment__
* __Workspace: __it is the term used for location in the memory where all ROS related data is stored.
* It is a directory system


The ROS workspace is divided into two parts:



1. __Underlay:__ it has the core ROS installation and some basic packages which are primary for the functioning of ROS.
2. __OVerlay:__ this is the user created or modified environment which can be modified and shaped according to individual conveniences and needs.

The separation of workspace into underlay and overlay is really important as it makes sure the basic important data of ROS isn’t damaged during working on ROS environment.



* __Sourcing the setup files: __if we directly try to run the ROS commands without sourcing its files the terminal will not recognize it .

	__Command:```source /opt/ros/humble/setup.bash``` __


	(here bash stands for my shell)


	Sourcing basically tells the terminal where to find ROS,its commands,and memory location of all the packages.


	I have made sourcing available for all terminals using
__Command: ```echo "source /opt/ros/humble/setup.bash" >>~/.bashrc```__
    	
__ Command:``` ~/.bashrc```__
      	

* __Check environment variables: __Environment variables are certain special settings related to our particular user environment.

	To make sure the ROS functions properly we must check the environment variables  and make any changes if needed. To check __Command: printenv | grep -i ROS __


	Some of the variables are :	 

1. __ROS_DOMAIN_ID:__

	Default middleware that ROS 2 uses for communication is DDS(Data Distribution service).


	ROS 2 nodes on the same domain can freely send messages to each other, while ROS 2 nodes on different domains cannot.


	All ROS 2 nodes use domain ID 0 by default.


	To avoid interference between different groups of computers running ROS 2 on the same network, a different domain ID should be set for each group.


	Safe number for domain ID can be chosen from the range [0,101].


	The domain ID is used by DDS to compute the UDP ports that will be used for discovery and communication


	__UDP Ports-__ UDP is a type of internet communication protocol UDP port is like a virtual doorway that lets the user send or receive data.


	In ROS 2 data is communicated node to node via UDP ports.


	Domain ID (other parameters used in the formula of UDP calculation are constant for a device) is used to calculate these UDP ports.


	UDP is an unsigned 16-bit integer so maximum Domain ID is 232. However, there are some platform specific constraints as the UDP ports used by ROS 2 might clash with the ephemeral ports (used by the OS) .


	If I set a number as Domain ID in a terminal using the


	__Command:```export ROS_DOMAIN_ID=&lt;my_domain_id>```__


 	it means that I am telling ROS that any Node I create in the current terminal or any other node with same domain ID in other terminal can communicate with each other


	__Command: ```echo "export ROS_DOMAIN_ID=&lt;your_domain_id>" >> ~/.bashrc```__


	The above command adds domain ID setting to all terminals thus any nodes created in any terminal on a device can communicate

* __Creating Nodes__

	A node is a single program which performs a designated task like collecting the sensor data , finding obstacles etc.


	Many such nodes together communicate with each other in a network to achieve a collective goal of running a Robot.

* __How Do Nodes communicate?__
1. __Topics:__ It is like a broadcast channel (for continuous data) ,one node publishes data and others subscribe to it.It is best for sensor data.
2. __Services:__ It is a form of communication which involves one time request and response between the subscriber node and the publisher node.
3. __Action:__ The communication pattern is similar to service i.e it involves request and response but it is used for more time consuming or elaborate tasks during the process of which the publisher node keeps sending the current status of work and the subscriber can also cancel the request midway between the task.
4. __Parameters:__
1. __Publisher Node:__ Node that collects and sends data (like reading sensor data)
2. __Subscriber Node:__ Node that receives data via a topic.

	__<span style="text-decoration:underline;">Week 1 </span>__

Question:Create a publisher node that sends a number, and a subscriber node that receives this number, calculates its square, and displays the result in the terminal.



1. Creating Root Directory (ROS 2 Workspace):

	__Command: ```mkdir -p ~/ros2_ws/src```__


	__Command: ```cd ~/ros2_ws/src```__

2. Creating a C++ROS 2 Package:

	__Command: ```ros2 pkg create mars_week1_cpp_pkg --build-type ament_cmake --dependencies rclcpp std_msgs```__


	The above command

* Creates the folder mars_week1_cpp_pkg
* Sets the folder to use ament_cmake for C++
* Adds dependencies rclcpp(ROS2 client library) and std_msgs
3. Workspace Structure:

```
ros2_ws/
└── src/
	└── mars_week1_cpp_pkg/
    	├── CMakeLists.txt      	# Build script
    	|* Tells ROS 2 how to compile cpp
    	|* Defines executables (number_publisher.cpp&square_subscriber.cpp)
    	|* Links dependencies
    	├── package.xml         	# Package metadata
    	└── src/  (It has the main cpp code but is not compiled) 
        	├── number_publisher.cpp   # Publisher node
        	└── square_subscriber.cpp  # Subscriber node
```

4. Add source code:

__Command:```gedit number_publisher/square_subscriber.cpp```__



5. Update CMakelists.txt
6. Build the Workspace
* Go back to the workspace (ros2_ws)
* __Command: colcon build __(it compiles source code in src/ and turn it into executable programs that ROS 2 can run.)
7. After building now the nodes can be run in different terminals  using

	__Command: ```ros2 run mars_week1_cpp_pkg number_publisher```__

