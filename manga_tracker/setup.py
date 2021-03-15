from setuptools import setup, find_packages

setup(
    name='mantrack',
    version='1.0.0',
    description='A simple web-crawler to check manga update',
    url='https://github.com/avidito/manga_tracker',
    author='Leonardi Fabianto',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'beautifulsoup4',
        'certifi',
        'chardet',
        'idna',
        'requests',
        'soupsieve',
        'urllib3'
    ],
    entry_points={
        'console_scripts': [
            'mantrack = mantrack.scripts.cli_interface:cli',
        ],
    },
)
