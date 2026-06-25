import requests
import urllib.parse
import json
import time
import os

os.makedirs("images", exist_ok=True)

# Test API with different prompts
test_prompts = [
    "yellow star",
    "blue ocean",
    "red flower"
]

API_BASE = "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image"

for i, prompt in enumerate(test_prompts):
    encoded = urllib.parse.quote(prompt)
    url = f"{API_BASE}?prompt={encoded}&image_size=landscape_4_3"
    print(f"\nTest {i+1}: {prompt}")
    print(f"URL: {url[:100]}...")

    resp = requests.get(url, timeout=120)
    print(f"Status: {resp.status_code}")
    print(f"Content-Type: {resp.headers.get('Content-Type', 'unknown')}")
    print(f"Size: {len(resp.content)} bytes")

    # Save test image
    with open(f"images/test_{i+1}.png", "wb") as f:
        f.write(resp.content)

    time.sleep(2)

print("\n\nChecking if images are different:")
for i in range(1, 4):
    os.system(f"md5sum images/test_{i}.png")
