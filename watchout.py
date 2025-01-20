#!/usr/bin/env python3
import requests
import pyfiglet
import argparse
from rich.console import Console
from rich.text import Text
import vt

console = Console()

def banner():
    pyfiglet.print_figlet("WatchOut", colors="yellow")
    print("welcome to WatchOut")
    print("*" * 50)

def error():
    err_text = Text("Oops, An error has occurred. Please refer to the help below:  ", style="bold red")
    console.print(err_text)
    print("\n")

def api_key():
    api_key = "01981a7334d54e3ab50bec8b10831aad7f144785f408b4d85ba9e2c9d425e050" # this is my own api key for testing
    #api_key = input("Enter your API key: ") # uncomment this line to get user input
    if not api_key:
        print("API key is required")
        print("To get your API key, sign up at https://www.virustotal.com. \n its free")
        print("And visit https://www.virustotal.com/gui/user/your_api_key")
        exit()
    client = vt.Client(api_key)
    return client

def helpfun():
    help_text = Text("Help", style="bold green")
    console.print(help_text)
    print("Usage: watchout.py [OPTIONS]")
    print("Options:")
    print("  -h, --help     Show this help message and exit")
    print("  -f, --file     Specify the file to scan")
    print("  -u, --url      Specify the URL to scan")
    print("  -k, --key      Specify the API key")
    print("\n")


def get_file_report(file_hash):
    client = "01981a7334d54e3ab50bec8b10831aad7f144785f408b4d85ba9e2c9d425e050" # this is my own api key for testing
    file = client.get_object(f"/files/{file_hash}") #example "/files/44d88612fea8a8f36de82e1278abb02f"
    return file.last_analysis_stats


def detect_malware_in_link(url, api_key = "01981a7334d54e3ab50bec8b10831aad7f144785f408b4d85ba9e2c9d425e050"):
    # VirusTotal API endpoint
    api_endpoint = "https://www.virustotal.com/api/v3/urls"

    # Prepare the payload
    payload = {"url": url}
    headers = {
        "x-apikey": api_key
    }

    try:
        # Submit URL for scanning
        response = requests.post(api_endpoint, data=payload, headers=headers)
        response.raise_for_status()  # Raise an error for HTTP errors

        # Get the analysis ID
        analysis_id = response.json()["data"]["id"]

        # Check analysis results
        result_endpoint = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"
        result_response = requests.get(result_endpoint, headers=headers)
        result_response.raise_for_status()

        # Get final results
        result_data = result_response.json()

        # Extract scan results
        stats = result_data["data"]["attributes"]["stats"]

        data = {
            "malicious": stats["malicious"],
            "suspicious": stats["suspicious"],
            "undetected": stats["undetected"],
            "harmless": stats["harmless"]
        }

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


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
            data = detect_malware_in_link(u)
            detect_summary(data)


    else:
        error()
        helpfun()
main()
