from setuptools import setup

setup(
    name="pytest-ipdb",
    py_modules=["pytest_ipdb"],
    install_requires=['ipdb'],
    version="0.1",
    author="David Szotten",
    author_email="davidszotten@gmail.com",
    description = "Automatically disable output capturing when launching ipdb",
    url="https://github.com/davidszotten/pytest_ipdb",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Communications :: Email",
        "Topic :: Software Development :: Debuggers",
        "Topic :: Software Development :: Testing",
    ],

    entry_points = {
        "pytest11": [
            "pytest_ipdb = pytest_ipdb",
        ]
    },
)
