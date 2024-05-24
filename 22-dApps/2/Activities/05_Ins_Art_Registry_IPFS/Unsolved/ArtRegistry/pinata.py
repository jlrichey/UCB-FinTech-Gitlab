
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

# Set up headers using JWT
file_headers = {
    "Authorization": f"Bearer {os.getenv('PINATA_JWT')}",
}

json_headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.getenv('PINATA_JWT')}",
}

def convert_data_to_json(content):
    data = {
        "pinataOptions": {"cidVersion": 1},
        "pinataContent": content
    }
    return json.dumps(data)

def pin_file_to_ipfs(file_path):
    with open(file_path, 'rb') as file:
        files = {'file': file}
        r = requests.post(
            "https://api.pinata.cloud/pinning/pinFileToIPFS",
            files=files,
            headers=file_headers
        )
        try:
            r.raise_for_status()
            print(r.json())
            ipfs_hash = r.json()["IpfsHash"]
            return ipfs_hash
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
            print(f"Response content: {r.content}")
            return None

def pin_json_to_ipfs(json_data):
    r = requests.post(
        "https://api.pinata.cloud/pinning/pinJSONToIPFS",
        data=json_data,
        headers=json_headers
    )
    try:
        r.raise_for_status()
        print(r.json())
        ipfs_hash = r.json()["IpfsHash"]
        return ipfs_hash
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        print(f"Response content: {r.content}")
        return None