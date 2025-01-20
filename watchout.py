#!/usr/bin/env python3
import pyfiglet
import requests
import hashlib
import argparse
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich import box
import vt

from virustotalting import get_file_report, get_link_report

console = Console()


def banner():
    print("welcome to WatchOut")
    print("*" * 50)


def error():
    err_text = Text("An error has occurred. Please refer to the help below:  ", style="bold red")
    console.print(err_text)
    print("\n")


def help():
    help_text = Text("Help", style="bold green")
    console.print(help_text)
    print("Usage: watchout.py [OPTIONS]")
    print("Options:")
    print("  -h, --help     Show this help message and exit")
    print("  -f, --file     Specify the file to scan")
    print("  -u, --url      Specify the URL to scan")
    print("  -k, --key      Specify the API key")
    print("\n")
# try:
#
#     def output(f_name, data):
#         file_name = f"{f_name}.txt"
#         try:
#             with open(file_name, "w") as f:
#                 f.write(data)
#         except:
#             error()
#             return False

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Specify the file to scan")
    parser.add_argument("-u", "--url", help="Specify the URL to scan")
    parser.add_argument("-k", "--key", help="Specify the API key")
    args = parser.parse_args()
    f = args.path[0] if args.file else False
    u = args.url[0] if args.url else False
    k = args.key[0] if args.key else False
    return f, u, k

def detect_summary(data):
    print("Threat Detection Summary".center(40, "-"))
    print(f"{'Category':<20}{'Count':<20}")
    print("-" * 40)
    for category, count in data.items():
        print(f"{category:<20}{count:<20}")

def main():
    banner()
    f, u, k = parse_args()
    if f!=False or u!=False:
        if f:
            #hashval = calculate_hash(f)
            data = get_file_report(f)
            detect_summary(data)
        elif u:
            data = get_link_report(u)

    else:
        error()
        help()
main()