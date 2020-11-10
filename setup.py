from setuptools import setup

setup(
    name="weather_cli",
    version="0.0.1",
    py_modules=['weather_cli'],
    install_requires=[
        'beautifulsoup4',
        'requests',
        'html5lib'
    ],
    entry_points={
        'console_scripts': [
            'get_weather = weather_cli.__main__:main',
        ],
    },
)


    
