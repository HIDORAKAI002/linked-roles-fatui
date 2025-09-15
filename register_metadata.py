# register_metadata.py
import os
import requests
from dotenv import load_dotenv

# --- IMPORTANT ---
# This imports the variables directly from your main bot file
# so you don't have to define them twice!
from discord_bot import CLIENT_ID, ROLE_METADATA

# Load secrets from your .env file
load_dotenv()
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# The URL to register the metadata
url = f"https://discord.com/api/v10/applications/{CLIENT_ID}/role-connections/metadata"

# The header with your bot's token for authentication
headers = {
    "Authorization": f"Bot {BOT_TOKEN}"
}

# The JSON payload is your ROLE_METADATA from the other file
# The requests library will automatically convert this Python list of dicts to JSON
json_payload = ROLE_METADATA

print("▶️  Attempting to register metadata with Discord...")
print(f"PAYLOAD: {json_payload}")

# Make the PUT request to Discord's API
response = requests.put(url, headers=headers, json=json_payload)

# Check the result
print(f"\n✅ RESPONSE\n-----------------")
print(f"Status Code: {response.status_code}")
try:
    # Try to print the JSON response
    print(response.json())
except requests.exceptions.JSONDecodeError:
    # If it's not JSON, print the raw text
    print(response.text)
