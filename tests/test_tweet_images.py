from click.testing import CliRunner
from tweet_images.cli import cli
import pytest


@pytest.mark.parametrize(
    "options,error",
    (
        ([], "Error: Missing argument 'TEXT'."),
        (
            ["tweet", "file-that-does-not-exist.jpg"],
            "'file-that-does-not-exist.jpg': No such file or directory",
        ),
        (
            ["tweet", "one.jpg", "--alt", "one", "--alt", "two"],
            "You passed more --alt text than you did images",
        ),
        (
            ["tweet", "one.jpg", "two.jpg", "three.jpg", "four.jpg", "five.jpg"],
            "Pass a maximum of four images",
        ),
    ),
)
def test_errors(options, error):
    runner = CliRunner()
    with runner.isolated_filesystem():
        for key in ("one", "two", "three", "four", "five"):
            open("{}.jpg".format(key), "wb").write(key.encode("utf-8"))
        result = runner.invoke(cli, options)
        assert result.exit_code in (1, 2)
        assert result.output.strip().endswith(error)
