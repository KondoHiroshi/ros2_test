import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64


class MinimalSubscriber(object):

    def __init__(self):
        self.node = rclpy.create_node('minimal_subscriber')
        self.node.create_subscription(Float64,'topic',self.callback,10) #??
        #self.node.subscription  # prevent unused variable warning

    def callback(self, msg):
        print(msg.data)

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber.node)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
