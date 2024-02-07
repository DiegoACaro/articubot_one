#!/usr/bin/env python3

import rclpy
from geometry_msgs.msg import Twist
import time

def move_square():
    rclpy.init()
    node = rclpy.create_node('move_square')
    velocity_publisher = node.create_publisher(Twist, '/cmd_vel', 10)
    vel_msg = Twist()

    speed = 0.2
    distance = 2.0
    for i in range(4):
        # Avanzar
        vel_msg.linear.x = speed
        t0 = time.time()
        current_distance = 0

        while current_distance < distance:
            velocity_publisher.publish(vel_msg)
            t1 = time.time()
            current_distance = speed * (t1 - t0)

        # Detenerse
        vel_msg.linear.x = 0.0
        velocity_publisher.publish(vel_msg)
        time.sleep(1)  # Pausa de 1 segundo

        # Girar
        vel_msg.angular.z = 0.2
        t0 = time.time()
        current_angle = 0

        while current_angle < 90:
            velocity_publisher.publish(vel_msg)
            t1 = time.time()
            current_angle = 0.2 * (t1 - t0) * 180 / 3.1415926535

        # Detenerse
        vel_msg.angular.z = 0.0
        velocity_publisher.publish(vel_msg)



if __name__ == '__main__':
    try:
        move_square()
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()
