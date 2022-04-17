import click
import itertools
import json
import twitter


@click.command()
@click.version_option()
@click.argument("text")
@click.argument("image_paths", nargs=-1, type=click.File("rb"))
@click.option("alts", "--alt", help="Alt text for images", multiple=True)
@click.option(
    "--consumer-key", envvar="TWITTER_CONSUMER_KEY", help="Twitter consumer key"
)
@click.option(
    "--consumer-secret",
    envvar="TWITTER_CONSUMER_SECRET",
    help="Twitter consumer secret",
)
@click.option(
    "--access-token-key", envvar="TWITTER_ACCESS_TOKEN_KEY", help="Twitter access token"
)
@click.option(
    "--access-token-secret",
    envvar="TWITTER_ACCESS_TOKEN_SECRET",
    help="Twitter access token secret",
)
def cli(
    text,
    image_paths,
    alts,
    consumer_key,
    consumer_secret,
    access_token_key,
    access_token_secret,
):
    """
    Send a tweet with images

    Example usage::

        tweet-images "Pictures of my dog!" cleo.jpg cleo-snoozing.jpg

    You can pass between 0 and 4 images.

    To specify alt text, use --alt "Alt text" - you can pass this up to four times as well.

    Authentication is via environment variables or --consumer-key etc options.
    """
    if len(image_paths) > 4:
        raise click.ClickException("Pass a maximum of four images")
    if len(alts) > len(image_paths):
        raise click.ClickException("You passed more --alt text than you did images")

    # Upload the media
    api = twitter.Api(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token_key=access_token_key,
        access_token_secret=access_token_secret,
    )
    media_ids = []
    for image_path, alt in itertools.zip_longest(image_paths, alts):
        media_id = api.UploadMediaSimple(image_path)
        if alt:
            api.PostMediaMetadata(media_id, alt)
        media_ids.append(media_id)

    # Tweet it
    status = api.PostUpdate(text, media=media_ids)
    tweet_url = "https://twitter.com/{}/status/{}".format(
        status.user.screen_name, status.id
    )
    click.echo(tweet_url)
