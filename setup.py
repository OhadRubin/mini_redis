from setuptools import setup, find_packages

setup(
    name='mini_redis',
    version='0.1.0',
    description='A mini Redis-like system implemented with FastAPI',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/OhadRubin/mini_redis',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'fastapi',
        'uvicorn',
        'requests',  # If your client is part of the package and requires requests
    ],
    entry_points={
        'console_scripts': [
            'start_mini_redis=my_mini_redis.run:main',
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)