# tweet-images

[![PyPI](https://img.shields.io/pypi/v/tweet-images.svg)](https://pypi.org/project/tweet-images/)
[![Changelog](https://img.shields.io/github/v/release/simonw/tweet-images?include_prereleases&label=changelog)](https://github.com/simonw/tweet-images/releases)
[![Tests](https://github.com/simonw/tweet-images/workflows/Test/badge.svg)](https://github.com/simonw/tweet-images/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/tweet-images/blob/master/LICENSE)

Send tweets with images from the command line

## Installation

Install this tool using `pip`:

    pip install tweet-images

## Usage

You'll need a consumer key, consumer secret, access token key and access token secret for a Twitter account that you wish to tweet from.

You can pass those as the `--consumer-key`, `--consumer-secret`, `--access-token-key`, `--access-token-secret` options to the command, or you can set them as environment variables like this:
```
export TWITTER_CONSUMER_KEY="..."
export TWITTER_CONSUMER_SECRET="..."
export TWITTER_ACCESS_TOKEN_KEY="..."
export TWITER_ACCESS_TOKEN_SECRET=".."
```

You can then send a tweet like this:

    tweet-images "This is my tweet"

Or attach between one and four images to that tweet by passing their file paths:

    tweet-images "Three pictures attached" one.jpg two.jpg three.jpg

You can pass `--alt "alt text"` one or more times to attach alt text to your images:

    tweet-images "Three pictures attached" one.jpg two.jpg \
      --alt "Alt text for one" --alt "Alt text for two"

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd tweet-images
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
