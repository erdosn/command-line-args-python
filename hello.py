import sys
from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        "--name",
        help="Name of person to say hello to"
    )
    args = parser.parse_args()
    return vars(args)


def hello_world(name="rafael"):
    message = f"hello, {name}!!!!"
    return message

def main():
    args = parse_args()
    message = hello_world(args['name'])
    print(message)



if __name__=="__main__":
    main()