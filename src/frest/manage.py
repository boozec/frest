import argparse
from manage.utils import logo, create_app
from manage.utils import logging
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--startapp", "-s", type=str, help="create new app")
    args = parser.parse_args()

    if args.startapp:
        if not os.path.exists("scheme"):
            logging("Create ")
            logging("scheme/", 0)
            logging("... ")
            logging("OK", 3, "\n")
            os.makedirs("scheme")

        create_app(args.startapp.lower())


if __name__ == "__main__":
    logo()
    main()
