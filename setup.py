from setuptools import setup, find_packages

setup(
    name='bughandler',
    packages=find_packages(),
    install_requires=[
        "six>=1.9",
    ],
    entry_points={
        'console_scripts': [
            'spray_bug = killer.kill:spray',
            'shoot_bug = killer.kill:shoot',
        ]
    }
)