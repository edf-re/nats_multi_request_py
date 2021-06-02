from setuptools import find_packages, setup

setup(
    name="nats-request-asap",
    packages=find_packages("src"),
    package_dir={"": "src"},
)
