import rospy
from geometry_msgs.msg import Twist

rospy.init_node("speed_controller")
sub = rospy.Subscriber("/cmd_vel", Twist, queue_size = 1)
r = rospy.Rate(4)
