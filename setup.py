from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = [
        line.strip() for line in f
        if line.strip() and not line.startswith("-e")
    ]

setup(
    name="ANIME-RECOMMENDER",
    version="0.1",
    author="Shikhar",
    packages=find_packages(),
    install_requires=requirements,
)
