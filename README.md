# WatchOut CLI Tool

WatchOut is a command-line interface (CLI) tool for linux that detects malware in files and URLs using the VirusTotal API. This tool provides a simple and efficient way to scan files and URLs for potential threats.

## Features

- Scan files for malware using their hash values.
- Scan URLs for potential threats.
- Display detailed threat detection summaries.
- User-friendly command-line interface.

## Requirements

- Python 3.x
- `requests`
- `pyfiglet`
- `rich`
- `argparse`
- `vt`

## Installation
1. clone this repo:
    ```sh
    git clone https://github.com/Rohithgg/watchout.git
    cd watchout
    ```

1. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

2. Make the `watchout.py` script executable and install it:
    ```sh
    chmod +x watchout.py
    sudo ./watchinstall.sh
    ```

## Usage

To use the WatchOut CLI tool, open your terminal and type `watchout` followed by the desired options.

### Options

- `-h, --help`: Show the help message and exit.
- `-f, --file`: Specify the file to scan.
- `-u, --url`: Specify the URL to scan.
- `-k, --key`: Specify the API key.

### Examples

1. Scan a file:
    ```sh
    watchout -f <file_hash>
    ```

2. Scan a URL:
    ```sh
    watchout -u <url>
    ```

3. Specify the API key:
    ```sh
    watchout -k <api_key>
    ```

## Getting Your API Key

To use the VirusTotal API, you need an API key. Follow these steps to get your API key:
1. Sign up at [VirusTotal](https://www.virustotal.com).
2. Visit [your API key page](https://www.virustotal.com/gui/user/your_api_key) to retrieve your key.

## Acknowledgements

- [VirusTotal](https://www.virustotal.com) for providing the API.
- [Rich](https://github.com/Textualize/rich) for the beautiful console output.
- [PyFiglet](https://github.com/pwaller/pyfiglet) for the ASCII art.

---

### Note that this is under development, so use it at your own risk. lol
