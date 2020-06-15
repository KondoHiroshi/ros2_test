import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64


class MinimalPublisher(object):

    def __init__(self):
        self.node = rclpy.create_node('minimal_publisher')
        self.publisher = self.create_publisher(Float64, 'topic', 10)
        timer_period = 0.5  # seconds

        self.node.create_timer(timer_period, self.clock)

    def clock(self):
        msg = Float64()
        msg.data = time.time()
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()


"""
import rclpy

from std_msgs.msg import String


def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('minimal_publisher')
    publisher = node.create_publisher(String, 'topic', 10)

    msg = String()
    i = 0

    def timer_callback():
        nonlocal i
        msg.data = 'Hello World: %d' % i
        i += 1
        node.get_logger().info('Publishing: "%s"' % msg.data)
        publisher.publish(msg)

    timer_period = 0.5  # seconds
    timer = node.create_timer(timer_period, timer_callback)

    rclpy.spin(node)

    # Destroy the timer attached to the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_timer(timer)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

"""
