from distutils.core import setup

setup(
    name="pyavanza",
    version="3.0.0",
    description="Avanza Python library",
    py_modules=["avanza"],
    author="Daniel Johansson",
    author_email="donnex@donnex.net",
    license="BSD",
    install_requires=["requests"],
)
