from setuptools import setup, find_packages

# python3 -m pip install --force-reinstall --no-deps git+https://github.com/OhadRubin/mini_redis
setup(
    name='mini_redis',
    version='0.2.0',
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
        "fire",
        "sqlitedict == 2.0.0",
        "filelock == 3.8.0",


    ],
    entry_points={
        #we want to use 
        'console_scripts': [
            'mini_redis=mini_redis.run:main',
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)