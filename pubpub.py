import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import time

class MinimalPublisher(object):

    def __init__(self):
        self.node = rclpy.create_node('minimal_publisher')
        self.publisher = self.node.create_publisher(Float64, 'topic', 10)
        timer_period = 2  # seconds

        self.node.create_timer(timer_period, self.clock)

    def clock(self):
        time.sleep(1)
        msg = Float64()
        msg.data = time.time()
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher.node)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
