from setuptools import find_packages, setup

package_name = 'radio'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vfran',
    maintainer_email='vitorianascimentomatos@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'radiostation = radio.radiostation:main',
            'radioreceiver = radio.radioreceiver:main',
            'educadora = radio.educadora:main',
            'receiver_fm = radio.radioreceiver_fm:main',
            'receiver_am = radio.radioreceiver_am:main',
        ],
    },
)
