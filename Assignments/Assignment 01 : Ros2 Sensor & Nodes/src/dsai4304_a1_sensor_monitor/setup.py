
from setuptools import find_packages, setup

package_name = 'dsai4304_a1_sensor_monitor'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Sarah Abumandill',
    maintainer_email='sabumandil@gmail.com',
    description='Simulates a front-range sensor and detects nearby obstacles.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher = dsai4304_a1_sensor_monitor.publisher_node:main',
            'subscriber = dsai4304_a1_sensor_monitor.subscriber_node:main',
        ],
    },
)
