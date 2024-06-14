from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    calculator_server_node = Node(
        package="calculator",
        executable="calculator_server"
    )

    calculator_client_node = Node(
        package="calculator",
        executable="calculator_client"
    )

    calculator_client_param_node = Node(
        package="calculator",
        executable="calculator_client_param"
    )

    ld.add_action(calculator_server_node)
    ld.add_action(calculator_client_node)
    ld.add_action(calculator_client_param_node)
    return ld