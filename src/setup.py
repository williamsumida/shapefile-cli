from setuptools import setup

setup(
    name="shapefile-cli",
    version="1.0.0",
    py_modules=["main"],
    install_requires=["Click"],
    entry_points={"console_scripts": ["shapecli=main:cli"]},
)
