import os
from datetime import datetime
from subprocess import check_output

from dotenv import load_dotenv


def main():
    print(os.environ.get("TEST"))
    print(datetime.now())
    print(type(check_output))
    print(type(load_dotenv))
    pass


if __name__ == "__main__":
    main()
