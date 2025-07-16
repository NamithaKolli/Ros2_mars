#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image #for subscribing to camera image messages
import cv2  #open CV library for image processing
import numpy as np  #for handling image arrays
from cv_bridge import CvBridge    #Converts ROS images to OpenCV format

class ObjectDetectionNode(Node):
    #Node initialization
    def __init__(self):
        super().__init__('object_detection_node')
        self.get_logger().info('Object Detection Node Started')
        
        #subscription setup
        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',   #topic 
            self.listener_callback,#callback function when a message is received 
            10                     #queue size
        )
        self.bridge = CvBridge()  #cv bridge initialization 

    def listener_callback(self, msg): #This function is called whenever a message is received
        try:
        #converts ros2 message into Open CV type message
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        except Exception as e: 
        #if any error is detected in message conversion logs an error and returns 
            self.get_logger().error(f'cv_bridge error: {e}')
            return
            
        
        # Convert to HSV
        hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
        
        # Print HSV value of the center pixel
        #h, w, _ = hsv.shape
        #center_hsv = hsv[h//2, w//2]
        #print("Center HSV:", center_hsv) I have commented this step because I might need to use it to find out the hsf values of any other colour I  want to detect

        # Defining orange range
        lower_orange = np.array([0, 50, 50])
        upper_orange = np.array([30, 255, 255])

        # Defining white range 
        lower_white = np.array([0, 0, 120])
        upper_white = np.array([180, 100, 255])
        
        # mask for Orange
        mask_orange = cv2.inRange(hsv, lower_orange, upper_orange)    
        
        # Mask for white
        mask_white = cv2.inRange(hsv, lower_white, upper_white)

        # Combine both masks
        combined_mask = cv2.bitwise_or(mask_orange, mask_white)
        
        # Applying mask to the image 
        result = cv2.bitwise_and(cv_image, cv_image, mask=combined_mask)
        
        #Find contours on the combined mask
        contours, _ = cv2.findContours(combined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
        # Draw bounding boxes on the original image
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 500:
               #epsilon = 0.01 * cv2.arcLength(cnt, True)
               #approx = cv2.approxPolyDP(cnt, epsilon, True)
               cv2.drawContours(cv_image, [cnt], -1, (0, 255, 0), 2)
               #cv2.drawContours(cv_image, [approx], -1, (0, 255, 0), 2)

        
        #Window to show the masked image
        cv2.imshow("Mask", combined_mask)
        
        # Show
        cv2.imshow("Traffic cone Detection", result)
        
        # NEW: Show original image with boxes
        cv2.imshow("Bounding Boxes", cv_image)
        cv2.waitKey(1) #To allow open CV window to refresh 
        
def main(args=None):
    rclpy.init(args=args)
    node = ObjectDetectionNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

