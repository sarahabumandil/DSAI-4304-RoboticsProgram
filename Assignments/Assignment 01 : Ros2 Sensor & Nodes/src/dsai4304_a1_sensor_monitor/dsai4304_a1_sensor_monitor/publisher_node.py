import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class RangePublisher(Node):
    """Publishes deterministic distance readings on /front/range at 5 Hz."""

    def __init__(self):
        super().__init__('range_publisher')

        # Publisher: topic '/front/range', type Float32, queue size 10
        self.pub = self.create_publisher(Float32, '/front/range', 10)

        # Deterministic test readings (metres) — covers CLEAR and STOP cases
        self.distances = [0.60, 0.40, 0.80, 0.30, 0.50]
        self.index = 0

        # Timer at 5 Hz => every 0.2 seconds
        self.timer = self.create_timer(0.2, self.timer_callback)

        self.get_logger().info(
            'Publisher started on /front/range at 5 Hz '
            '(unit: metres, expected range: 0.00-5.00 m)'
        )

    def timer_callback(self):
        value = self.distances[self.index % len(self.distances)]

        msg = Float32()
        msg.data = float(value)
        self.pub.publish(msg)

        self.get_logger().info(f'Publishing: {value:.2f} m')
        self.index += 1


def main(args=None):
    rclpy.init(args=args)
    node = RangePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
