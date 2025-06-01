<!-----



Conversion time: 1.06 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β44
* Mon May 26 2025 08:46:14 GMT-0700 (PDT)
* Source doc: mars task2
----->


**Mars Task2**

**Understanding communication system in ROS 2**

The main function of ROS 2 that makes it such a remarkable software used by developers throughout the world is that it  enables communication between various nodes (say parts of a robot).

In ROS 2 communication between nodes takes place via the following methods :



1. **Topics:**
* Topic allows communication between the publisher and subscriber nodes.
* This type of communication is useful for continuous information flow.
* For example, The information sent by the sensors through topics.
* The following are the commands related to usage or tracking of topics using command line:
* To list currently active topics in system

        ros2 topic list

*   To see the data being published on topic 

          ros2 topic echo <topic_name>

* To see topic information (type,number of publishers and subscribers)

        ros2 topic info <Topic_type>

*  To view the type of message being sent and received via a topic:

        ros2 interface show <Topic_type>

* To publish data to a topic directly from the command line :

        ros2 topic pub --once <topic_name> <msg_type> '<args>'
  (args is the actual data which is passed)
  
‘--once’ is an optional argument which will ensure only one message is published else the publisher will keep on publishing the message until manually stopped. 

        
2. **Services:**
* Services involve communication between service server and client.
* The client sends a request to the server and the server responds to that request.
* There can be multiple clients and servers sending and receiving messages in a network.\
* The following are some commands to use service communication in ROS 2:
* To view list of all services currently active in system:

            ros2 service list

* Service types are defined similarly to topic types, except service types have two parts: one message for the request and another for the response.

            ros2 service type <service_name>

* To call services from command line we need to know the structure of input arguments ,it can be found using the ros2 interface show:

            ros2 interface show <type_name>

* If we know the service type and the type of arguments to give we can make a service call in command line using:

            ros2 service call <service_name> <service_type> <arguments>

3. **Actions:**
* Actions are a combination of topics and services which are used for longterm communication .
* They consist of three parts: a goal, feedback, and a result.
* An “action client” node sends a goal to an “action server” node that acknowledges the goal and returns a stream of feedback and a result.
* The following are some commands to use service communication in ROS 2:

      ros2 node info <node_name>



* The above command provides a list of subscribers, publishers, services, action servers and action clients of the node.
* If there is some component listed under action server it means responds to and provides feedback for the mentioned node’s action.
* If there is some component listed under the action client it sends goals for that action name mentioned.
* To list the currently running actions along with their action type( which will further be necessary to implement an action from the command line)

    ros2 action list -t

* To implement action along with the action type we must also know the type of argument we have to give in the goal ,to know that we have to use the ros2 interface show command:

    ros2 interface show <Action_type>

* Sending an action goal:

ros2 action send_goal <action_name> <action_type> <values>

<values> need to be YAML format

All goals have a unique ID which will be sent in the return message.



* To receive the feedback to this goa; add - -feedback to the end of above command.

**Communication system in ROS 1 (The ROS master)**



* ROS 1 relies on a centralized master node called the ROS  master , to discover nodes and establish connection between them .
* It enables nodes to find each other and exchange messages between themselves.
* Uses TCP (transmission control protocol)

    **What is peer-to-peer communication?**

* Direct peer-to-peer (P2P) communication refers to a network communication model where two devices (peers) connect and exchange data directly with each other without involving an intermediary.
* In ROS 1  there is partial peer-to-peer communication. As the centralized ROS master is required to navigate and establish connection.Once the connection between nodes is established the communication becomes peer-to-peer.
* In ROS1, ROS nodes were originally developed to run on a single process. Later on, ROS1 nodelets were introduced, which allow multiple nodes to run on the same process (each node is compiled as a shared library and loaded at runtime by a container process).

**Disadvantages of ROS master:**



* **Security issues: **the working of Robots might involve communication over insecure networks (like the internet) . There is a threat to any kind of important data being transmitted between nodes.
* **Not real-time:** as the communication through ROS master involves a longer process some important tasks which need to be done in a given timeline fail.
* **Single point of failure:** Failure of ROS master can lead to communication failure** . **If a node is created it first gives information about its parameters , subscribers, and topics and any other node can communicate with this node 1 by communicating its information with ROS master.But ,under any circumstances if ROS master dies then any new node will not be able to communicate with this node 1 , hence all he communications depend on the working of this ROS master.

**Communication in ROS 2 (DDS)**



* The default middleware that ROS 2 uses for communication is DDS.
* It is an end-to-end middleware which means that it handles entire communication from the sending application to the receiving application. There is no need for a separate master to locate nodes.
* The DDS communication is implemented using Domain ID’s ,UDP ports (primarily), multicast and unicast ports.

**How DDS enables communication:**



1. **Node Initialization**: When a ROS 2 node starts;
* It creates a DomainParticipant (joins the communication domain).
* It sets up DDS entities like Publisher/Subscriber, DataWriter/DataReader.
2. **Publisher and Subscriber Setup**
* When a node creates a publisher, DDS creates a DataWriter for the given topic.
* When a subscriber is created, DDS creates a DataReader for the topic.
3. **DDS performs automatic discovery.**
4. **Data Exchange**
* The publisher sends messages via the DataWriter.

* The subscriber receives them via the DataReader.
5. **Qos management** (detailed below)
* **Domain ID** :Domain ID is an integer identifier that logically groups participants of DDS (nodes).
* Only nodes with the same Domain ID can communicate with each other.
* The default domain ID of any node is set to zero.
* We can set domain ID of a node using the command:

  export ROS_DOMAIN_ID= <Domain_ID>

* The domain ID is used by DDS to compute the UDP ports that will be used for discovery and communication.
* **UDP ports: **It is an unsigned 16-bit integer (thus highest UDP port number is 65535 ) which acts like a virtual doorway for sending and receiving messages.
* Calculation of UDP ports from domain ID is done using specific formulas and the largest possible domain ID is 232.
* However it is best suggested to use a Domain ID between 0 and 101 because other ports might clash with the operating system's ephemeral port range. 

**Comparison between UDP and TCP  (used in ROS 1):**



* TCP requires 3 way connection : the client requests ,the server accepts then the client confirms.

    UDP doesn't require connection; it means the sender directly sends packets of data without confirming whether the receiver is ready; there is no guarantee message was received.

* UDP supports multicast i.e UDP sends a packet to a multicast IP address which can be then subscribed by multiple subscribers ,thus sending same data to multiple users without duplicating .TCP only supports unicast as it is point-to-point communication.

**Why UDP if there is no guarantee message was sent?**



* Because, in real-time robotics, speed and timeliness are often more important than guaranteed delivery.

    It is one of the reasons why DDS (which primarily uses UDP is chosen for ROS 2 .



* Moreover, DDS adds reliability when required. Throus Qos(Quality of service) settings ROS 2 via DDS enables us to choose between :

**RELIABLE**:DDS adds acknowledgments & resends lost packets                      (like TCP).

**BEST_EFFORT**:DDS just sends and forgets (faster, like UDP)

