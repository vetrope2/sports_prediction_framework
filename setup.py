from setuptools import setup, find_packages


def load_requirements(filename="requirements.txt"):
    with open(filename) as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]


setup(
    name="sports_prediction_framework",
    version="0.1",
    packages=find_packages(),
    install_requires=load_requirements()
)