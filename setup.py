from setuptools import setup

setup(
    name='hpglsender',
    version='0.1.0rc1'
    packages=['hpglsender'],
    include_package_data=True,
    install_requires=[
        'pyserial',
        ],
    entry_points={
        'console_scripts': [
            'hpglsender=hpglsender.__main__:main'
            ]
        }
    )