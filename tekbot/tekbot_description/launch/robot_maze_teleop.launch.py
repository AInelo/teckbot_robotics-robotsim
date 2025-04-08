from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # Inclusion du fichier de lancement pour spawner le robot dans le labyrinthe
    spawn_robot = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare("tekbot_description"),
                "launch",
                "spawn_robot_in_maze.launch.py"
            ])
        ])
    )

    # Lancement de la téléopération via le clavier
    teleop = Node(
        package='teleop_twist_keyboard',
        executable='teleop_twist_keyboard',
        name='teleop_keyboard',
        output='screen', 
        prefix='xterm -e',  # Optionnel : ouvre dans un terminal séparé
        remappings=[('/cmd_vel', '/cmd_vel')]  # Assurez-vous que c'est le bon topic
    )

    return LaunchDescription([
        spawn_robot,
        teleop
    ])
