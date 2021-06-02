from os.path import dirname, join

from setuptools import find_packages, setup


def read(*names, **kwargs):
    with open(
        join(dirname(__file__), *names), encoding=kwargs.get("encoding", "utf8")
    ) as openfile:
        return openfile.read()


setup(
    name="nats-request-asap",
    packages=find_packages("src"),
    package_dir={"": "src"},
    version="0.1",
    license="BSD-2-Clause",
    description="Python function to return one or multiple responses to a "
    "NATS request as soon as possible. ",
    long_description=read("README.md"),
    author="Hugo O. Rivera",
    author_email="hugo@roguh.com",
    url="https://github.com/roguh/nats_request_asap",
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Utilities",
    ],
    project_urls={
        "Issue Tracker": "https://github.com/roguh/nats_request_asap/issues",
    },
    keywords=["NATS", "NATS request", "response as soon as possible", "asap response"],
    python_requires=">2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*",
    install_requires=[
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
    ],
    extras_require={},
    setup_requires=[],
    entry_points={},
)
