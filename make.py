#!/usr/bin/env python3

from argparse import ArgumentParser
from os import system


def run_command(cmd: str):
    print(cmd)
    ret = system(cmd)
    assert ret == 0


def make(version: str):
    repo = "ghcr.io/seekyct/spm-docker"
    tag = f"{repo}:{version}"
    latest = f"{repo}:latest"
    run_command(f"docker build . --tag {tag} --tag {latest}")
    run_command(f"docker push {tag}")
    run_command(f"docker push {latest}")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("version", type=str)
    args = parser.parse_args()

    make(args.version)
