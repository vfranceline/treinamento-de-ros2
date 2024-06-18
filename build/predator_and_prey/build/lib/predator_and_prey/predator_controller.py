#!/usr/bin/env python3

import rclpy
import math
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class PredatorControllerNode(Node):
    def __init__(self):
        super().__init__("predator_controller")
        self._pose = None
        self._target_x = 10.0
        self._target_y = 10.0
        self._pose_subscriber = self.create_subscription(Pose, "turtle1/pose", self.callback_turtle_pose,10)
        self._cmd_vel_publisher = self.create_publisher(Twist, "turtle1/cmd_vel",10)
        self.control_loop_timer = self.create_timer(0.01, self.control_loop)

    
    def callback_turtle_pose(self,msg):
        self._pose = msg
        self.get_logger().info("Pose (x, y, theta): ()"+str(self._pose.x)+";"+
                               str(self._pose.y)+","+str(self._pose.theta)+")")
        
    def control_loop(self):
        if self._pose == None:
            return
        else:
            delta_x = self._target_x - self._pose.x
            delta_y = self._target_y - self._pose.y
            distance2target = math.sqrt(delta_x * delta_y + delta_y * delta_y)
            msg = Twist()

            if distance2target < 0.5:
                msg.linear.x = 0.0
                msg.angular.z = 0.0
            else:
                angle2target = math.atan2(delta_y, delta_x) - self._pose.theta
                if angle2target > math.pi:
                    angle2target -=2*math.pi
                elif angle2target < -math.pi:
                    angle2target += 2*math.pi

                msg.linear.x = distance2target
                msg.angular.z = 3 * angle2target
            self._cmd_vel_publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = PredatorControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()