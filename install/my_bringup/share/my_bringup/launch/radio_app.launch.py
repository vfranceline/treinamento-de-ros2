from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    educadora_node = Node(
        package="radio",
        executable="educadora"
    )

    receiver_oeste_node = Node (
        package="radio",
        executable="receiver_am",
        name="Oeste",
        remappings=[
            ("AM", "AM999")
        ]
    )

    receiver_conquista_node = Node (
        package="radio",
        executable="receiver_am",
        name="Conquistense",
        remappings=[
            ("AM", "AM1215")
        ]
    )

    receiver_chapada_node = Node (
        package="radio",
        executable="receiver_fm",
        name="Chapada",
        remappings=[
            ("FM", "FM995")
        ]
    )

    receiver_chico_node = Node (
        package="radio",
        executable="receiver_fm",
        name="VelhoChico",
        remappings=[
            ("FM", "FM1031")
        ]
    )

    receiver_teixeira_node = Node (
        package="radio",
        executable="receiver_fm",
        name="Teixeira",
        remappings=[
            ("FM", "FM971")
        ]
    )

    ld.add_action(educadora_node)
    ld.add_action(receiver_chapada_node)
    ld.add_action(receiver_chico_node)
    ld.add_action(receiver_teixeira_node)
    ld.add_action(receiver_oeste_node)
    ld.add_action(receiver_conquista_node)

    return ld