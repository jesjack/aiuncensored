from setuptools import setup, find_packages

setup(
    name="aiuncensored",
    version="1.3",
    description="Cliente para interactuar con el modelo llama-3-70b y la API AIUncensored",
    author="Vauth",
    url="https://github.com/jesjack/aiuncensored",
    packages=find_packages(),
    install_requires=[
        "requests",
        "fake-useragent"
    ],
    python_requires=">=3.7"
)