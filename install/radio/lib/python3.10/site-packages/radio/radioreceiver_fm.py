#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from example_interfaces.msg import String

class ReceiverNodeFM(Node):
    def __init__(self):
        super().__init__("radioreceiver_fm")
        self._subscriber = self.create_subscription(String, "FM1075", self.callback_radioreceiver_fm, 10)
        self._publisher = self.create_publisher(String, "FM", 1)
        self.timer = self.create_timer(10, self.pub_mensagem_fm)

        self.mensagem = None

        self.get_logger().info("O rádio receptor FM foi ligado")


    def callback_radioreceiver_fm(self,msg_fm):
        self.get_logger().info(str(msg_fm.data))
        self.mensagem = 'Retransmitindo - ' + msg_fm.data


    def pub_mensagem_fm(self):
        mensagem = String()
        mensagem.data = self.mensagem
        self._publisher.publish(mensagem)
        self.get_logger().info(str(mensagem.data))

def main(args=None):
    rclpy.init(args=args)
    node = ReceiverNodeFM()
    rclpy.spin(node)
    rclpy.shutdown()