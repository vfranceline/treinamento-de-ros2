#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from example_interfaces.msg import String

class ReceiverNodeAM(Node):
    def __init__(self):
        super().__init__("radioreceiver_am")
        self._subscriber = self.create_subscription(String, "AM536", self.callback_radioreceiver_am, 10)
        self._publisher = self.create_publisher(String, "AM", 1)
        self.timer = self.create_timer(10, self.pub_mensagem_am)

        self.mensagem = None

        self.get_logger().info("O rádio receptor AM foi ligado")
    
    def callback_radioreceiver_am(self,msg_am):
        self.get_logger().info(str(msg_am.data))
        self.mensagem = 'Retransmitindo - ' + msg_am.data


    def pub_mensagem_am(self):
        mensagem = String()
        mensagem.data = self.mensagem
        self._publisher.publish(mensagem)
        self.get_logger().info('publicando: "%s"' % mensagem.data)


def main(args=None):
    rclpy.init(args=args)
    node = ReceiverNodeAM()
    rclpy.spin(node)
    rclpy.shutdown()