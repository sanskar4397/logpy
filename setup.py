from setuptools import find_packages, setup

setup(
    name='logpy',
    packages=find_packages(include=['logpy']),
    version='0.0.7',
    description='simple python library can be used for logging fastapi',
    author='Sanskar Gupta',
    license='MIT',
    install_requires=["starlette_context==0.3.5"],
    # setup_requires=["pytest-runner==6.0.0"],
    # tests_require=["pytest==7.2.0"],
    # test_suite='tests',
)
