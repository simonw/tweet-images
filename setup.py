from setuptools import setup
import os

VERSION = "0.1.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="tweet-images",
    description="Send tweets with images from the command line",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/tweet-images",
    project_urls={
        "Issues": "https://github.com/simonw/tweet-images/issues",
        "CI": "https://github.com/simonw/tweet-images/actions",
        "Changelog": "https://github.com/simonw/tweet-images/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["tweet_images"],
    entry_points="""
        [console_scripts]
        tweet-images=tweet_images.cli:cli
    """,
    install_requires=["click", "python-twitter"],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.7",
)
