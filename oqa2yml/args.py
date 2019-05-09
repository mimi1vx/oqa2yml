from argparse import ArgumentParser


def get_parser():
    parser = ArgumentParser()

    parser.add_argument(
        "testid", type=int, nargs=1, help="Test ID from openQA instance"
    )

    parser.add_argument(
        "-H",
        "--host",
        default="https://openqa.suse.de",
        type=str,
        help="OpenQA instance address",
    )

    return parser
