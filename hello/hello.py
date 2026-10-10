#!/usr/bin/env python3
import argparse


def hello(mode=None):
    s = "Hello world!"
    if mode == "upper":
        s = s.upper()
    elif mode == "lower":
        s = s.lower()
    elif mode == "title":
        s = s.title()

    return s


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--mode")
    args = p.parse_args()

    print(hello(args.mode))


if __name__ == "__main__":
    main()
