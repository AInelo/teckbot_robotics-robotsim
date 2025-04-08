from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, LogInfo
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    # Déclaration des arguments pour définir la position du robot
    declare_x_init = DeclareLaunchArgument(
        'x_init', default_value='-2.276574', description='Initial X position of the robot'
    )
    declare_y_init = DeclareLaunchArgument(
        'y_init', default_value='1.605198', description='Initial Y position of the robot'
    )
    declare_z_init = DeclareLaunchArgument(
        'z_init', default_value='0.030000', description='Initial Z position of the robot'
    )
    declare_yaw_init = DeclareLaunchArgument(
        'yaw_init', default_value='0.0', description='Initial yaw angle of the robot'
    )

    # Définition du chemin du fichier de lancement de l'environnement du labyrinthe
    maze_launch_path = PathJoinSubstitution(
        [FindPackageShare("maze_solving"), "launch", "maze.launch.py"]
    )

    maze_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([maze_launch_path]),
        launch_arguments={}.items()
    )

    # Définition du chemin du fichier de lancement pour le robot
    gazebo_launch_path = PathJoinSubstitution(
        [FindPackageShare("tekbot_description"), "launch", "gazebo.launch.py"]
    )
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([gazebo_launch_path]),
        launch_arguments={
            'x_init': LaunchConfiguration('x_init'),
            'y_init': LaunchConfiguration('y_init'),
            'z_init': LaunchConfiguration('z_init'),
            'yaw_init': LaunchConfiguration('yaw_init')
        }.items()
    )

    return LaunchDescription([
        declare_x_init,
        declare_y_init,
        declare_z_init,
        declare_yaw_init,
        maze_launch,
        gazebo_launch
    ])
