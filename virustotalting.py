import hashlib
import vt

def api_key():
    api_key = "01981a7334d54e3ab50bec8b10831aad7f144785f408b4d85ba9e2c9d425e050" # this is my own api key for testing
    #api_key = input("Enter your API key: ") # uncomment this line to get user input
    if not api_key:
        print("API key is required")
        print("To get your API key, sign up at https://www.virustotal.com")
        print("And visit https://www.virustotal.com/gui/user/your_api_key")
        exit()
    client = vt.Client(api_key)
    return client

def get_file_report(file_hash):
    client = api_key()
    file = client.get_object(f"/files/{file_hash}") #example "/files/44d88612fea8a8f36de82e1278abb02f"
    return file.last_analysis_stats

def get_link_report(link):
    client = api_key()
    url = client.get_object("/urls/https://www.google.com")
    return url.last_analysis_stats

def calculate_hash(file):
    with open(file, "rb") as f:
        bytes = f.read()
        hash = hashlib.sha256(bytes).hexdigest()
        return hash
# this is waste change and use other type of api sevice
