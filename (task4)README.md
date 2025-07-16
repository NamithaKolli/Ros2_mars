__Task4__

__Note:Please download the video for better quality.__

  [▶️ Cone detection Demo video](https://drive.google.com/file/d/18cWF08NQ1Up5IpKTperSHemE8e1-LHPY/view?usp=sharing) 

  
__Computer vision:__



* __Computer vision__ is when computers learn to see and understand images or videos like humans do.
* In simple words: It’s teaching computers to “look” at pictures and figure out what’s in them.
   
Examples:

* Recognizing faces in photos.
* Finding traffic cones on the road.
* Counting people in a crowd.
* Reading text from pictures.

__Open CV:__



* It is a python open source library,which is used for computer vision in artificial intelligence,machine learning,face recognition etc.
* It has hundreds of computer vision algorithms in C++,python,Java and MATLAB interfaces.
* It is used for object classification,object identification,object tracking,feature matching,image restoration and video motion analysis.
* Images are analysed by grayscale or RGB.
* In my node I have used HSV colour detection.
* __HSV __stands for Hue,saturation and value (brightness)
* We use a colour __mask __to detect certain colour hues in an image.Its a __binary image__ which shows white in regions where the pixel colour matches with the one we want to detect and black everywhere else.
* Mask__ __is like a stencil or cookie-cutter: 
- [ ] The mask is _black-and-white_, defining where to “cut out.”
- [ ] The result image “cuts out” the original colors only where the mask allows it.
* __cv_bridge __is used to convert ROS image messages (sensor_msgs/Image) to OpenCV image format (NumPy arrays).

__Some issues I faced during the process of detecting the cone:__



* Even after writing the correct code the colour detection window was completely black indicating it did not detect the orange in the cone , so I had to check using center check  and widen the range to detect the required colours.
* __Pros (Open CV)__
* The major Pro of using Open CV for detection is ,its implementation is very simple, we just need to add the colour ranges to detect any required colour.
* It is pretty flexible as we get to adjust hsv values, not just rgb .
* Works with the present Gazebo model no need to change it for detection. I have written a completely different node for open cv and didn't have to detect the current robot model.
* __Cons (Open CV)__
* As we have to manually set the ranges using HSV values, sometimes the ranges might be too narrow or too wide which can lead to improper detection, which I faced personally.
* It detected partially when the cone was farther ,so I had to again widen the range.
* The contour lines (bounding shapes) are not very clear when the object is at a distance due to low pixel detection,background blending etc.


* __YOLO__
* Using yolo can make detection much more precise and accurate as compared to open CV .But it requires more time and training .
* It can even detect shapes , if just colour doesn't give accurate results.
* As I did not know Yolo before and it will take some time to find out an actual pre-trained cone detecting model as well as install some other libraries, I choose Open Cv for basic detection.
* YOLO (especially segmentation-capable versions) will usually handle small/distant objects better than basic color threshold + contour detection (open CV).

__Future Applications / Next Steps Using Cone Detection:__



* __Obstacle Stopping Behavior:__

After detecting the cone using OpenCV, we can calculate its position in the image (e.g., center of contour). If the cone appears near the center of the frame and its size (area of contour or bounding box) exceeds a threshold, it indicates the cone is close. Based on this, the robot can stop by publishing zero velocity using a /cmd_vel publisher.



* __Navigating Around the Cone (Avoidance):__

Once the robot identifies the cone's position in the image (e.g., left, center, or right), it can steer slightly away from it. For example, if the cone appears on the left side of the image, the robot can turn slightly right while moving forward, using basic rules to adjust linear and angular velocity accordingly.

These next steps improve the robot’s ability to operate safely and intelligently in dynamic environments.
