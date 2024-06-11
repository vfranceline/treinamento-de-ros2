from setuptools import find_packages, setup

package_name = 'basic_calculator'

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
            'calc_basic_server = basic_calculator.calculadora_basica_server:main',
            'calc_basic_client = basic_calculator.calculadora_basica_client:main',

        ],
    },
)
