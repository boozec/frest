import argparse
from manage.utils import logo, create_app
from manage.utils import logging, logging_arg
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--startapp", "-s", type=str, help="create new app")
    args = parser.parse_args()

    if args.startapp:
        if not os.path.exists("scheme"):
            logging_arg("Create {}... ", "scheme/")
            logging("OK", 3, "\n")
            os.mkdir("scheme")

        create_app(args.startapp)


if __name__ == "__main__":
    logo()
    main()
