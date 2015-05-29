
# Generate data URI for file content
# as defined in RFC 2397

import click
import urllib


# very simplistic file extension to mimetype mapping
mime_types = {
    "css": "text/css",
    "gif": "image/gif",
    "ico": "image/x-icon",
    "jpeg": "image/jpeg",
    "jpg": "image/jpeg",
    "js": "application/javascript",
    "png": "image/png",
}


@click.command()
@click.argument('path')
def main(path):
    if "." not in path:
        raise click.BadParameter("Input file name must have file name extension, e. g. .jpg")
    extension = path.split(".")[-1].lower()
    mime_type = mime_types.get(extension, "application/octet-stream")
    with click.open_file(path, 'r') as inputfile:
        content = inputfile.read()
        content = content.encode("base64")
        content = urllib.quote(content)
        content = "data:%s;base64,%s" % (mime_type, content)
        click.echo(content)


if __name__ == "__main__":
    main()
