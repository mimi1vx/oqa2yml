import sys

from .args import get_parser
from .oqa2yml import Oqa2yml

def main():
    p = get_parser()
    args = p.parse_args(sys.argv[1:])
    sys.exit(Oqa2yml(args.host, args.testid[0])())
