import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class RangeSubscriber(Node):
    """Subscribes to /front/range and prints CLEAR or STOP."""

    THRESHOLD = 0.50  # metres

    def __init__(self):
        super().__init__('range_subscriber')

        self.sub = self.create_subscription(
            Float32,
            '/front/range',
            self.callback,
            10,
        )

        self.get_logger().info(
            f'Subscriber listening on /front/range '
            f'(threshold = {self.THRESHOLD:.2f} m)'
        )

    def callback(self, msg):
        d = float(msg.data)
        if d >= self.THRESHOLD:
            self.get_logger().info(f'Reading {d:.2f} m -> CLEAR')
        else:
            self.get_logger().info(f'Reading {d:.2f} m -> STOP')


def main(args=None):
    rclpy.init(args=args)
    node = RangeSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
