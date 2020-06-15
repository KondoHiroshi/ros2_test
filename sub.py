
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MinimalSubscriber(object):

    def __init__(self):
        self.node = rclpy.create_node('minimal_subscriber')
        self.node.create_subscription(String,'topic',self.callback,10) #??
        self.subscription  # prevent unused variable warning

    def callback(self, msg):
        print(msg.data)

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

"""
import rclpy

from std_msgs.msg import String


def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('minimal_subscriber')

    subscription = node.create_subscription(
        String, 'topic', lambda msg: node.get_logger().info('I heard: "%s"' % msg.data), 10)
    subscription  # prevent unused variable warning

    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

"""
