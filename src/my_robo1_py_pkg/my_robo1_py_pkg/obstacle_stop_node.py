import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class ObstacleStopNode(Node):
    def __init__(self):
        super().__init__('obstacle_stop_node')

        # Subscriber to LIDAR scan
        self.scan_sub = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        # Publisher to cmd_vel
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)

        # Logger info
        self.get_logger().info('Obstacle stop node started. Monitoring /scan')

    def scan_callback(self, msg):
        self.get_logger().info("LIDAR callback triggered")

        min_distance = min(msg.ranges)
        threshold = 0.5  # meters

        cmd = Twist()

        if min_distance < threshold:
            self.get_logger().info(f'Obstacle too close! Distance: {min_distance:.2f} m. Stopping.')
            cmd.linear.x = 0.0
            cmd.angular.z = 0.0
        else:
            self.get_logger().info(f'Path clear. Moving forward. Distance: {min_distance:.2f} m')
            cmd.linear.x = 0.2  # Move forward
            cmd.angular.z = 0.0

        self.cmd_pub.publish(cmd)



def main(args=None):
    rclpy.init(args=args)
    node = ObstacleStopNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()

