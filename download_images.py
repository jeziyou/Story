import requests
import urllib.parse
import os
import time

IMAGE_DIR = "images"
os.makedirs(IMAGE_DIR, exist_ok=True)

def get_text_to_image_url(prompt, image_size="landscape_4_3"):
    encoded_prompt = urllib.parse.quote(prompt)
    return f"https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt={encoded_prompt}&image_size={image_size}"

def download_image(prompt, filename, image_size="landscape_4_3", retries=3):
    filepath = os.path.join(IMAGE_DIR, filename)
    if os.path.exists(filepath):
        print(f"✓ Already exists: {filename}")
        return True
    
    url = get_text_to_image_url(prompt, image_size)
    print(f"Downloading {filename}...")
    
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=120)
            if response.status_code == 200:
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                print(f"✓ Saved: {filename}")
                time.sleep(1)
                return True
            else:
                print(f"  Attempt {attempt+1} failed: HTTP {response.status_code}")
                time.sleep(2)
        except Exception as e:
            print(f"  Attempt {attempt+1} error: {e}")
            time.sleep(2)
    
    print(f"✗ Failed to download: {filename}")
    return False

images_to_download = [
    {
        "filename": "little_star_cover.png",
        "prompt": "Cute cartoon little star shining in night sky with big friendly eyes, children's book illustration style, soft warm colors, dreamy atmosphere",
        "size": "landscape_4_3"
    },
    {
        "filename": "little_star_page1.png",
        "prompt": "Lonely little cartoon star with sad expression looking at other bigger brighter stars in night sky, children's picture book style, soft purple and blue night sky, gentle moon in background",
        "size": "landscape_4_3"
    },
    {
        "filename": "little_star_page2.png",
        "prompt": "Friendly cartoon moon with gentle smile talking to tiny star, beautiful night sky with soft clouds, warm glow, children's book illustration, whimsical style",
        "size": "landscape_4_3"
    },
    {
        "filename": "little_star_page3.png",
        "prompt": "Tiny star shining brightly down on a cute little firefly in dark forest, path illuminated by warm starlight, magical forest scene at night, children's illustration style",
        "size": "landscape_4_3"
    },
    {
        "filename": "little_star_page4.png",
        "prompt": "Little girl by bedroom window painting and looking up at smiling star, cozy bedroom with warm light, firefly nearby, children's picture book art style, heartwarming scene",
        "size": "landscape_4_3"
    },
    {
        "filename": "little_star_page5.png",
        "prompt": "Little star shining light on lost baby bird flying towards mother bird in nest, tree branches, night scene with soft glowing light, children's storybook illustration",
        "size": "landscape_4_3"
    },
    {
        "filename": "little_star_page6.png",
        "prompt": "All stars in sky smiling and looking at little star who is glowing proudly, moon smiling too, below can be seen firefly, girl's window light, bird in nest, panoramic night scene, children's art",
        "size": "landscape_4_3"
    },
    {
        "filename": "little_star_page7.png",
        "prompt": "Happy little star shining brightly with big smile, surrounded by friends firefly, bird, little girl waving from window, beautiful starry night sky, warm golden glow, children's book illustration, happy ending",
        "size": "landscape_4_3"
    }
]

print("=" * 50)
print("Downloading story images...")
print("=" * 50)

success = 0
for img in images_to_download:
    if download_image(img["prompt"], img["filename"], img["size"]):
        success += 1

print("=" * 50)
print(f"Downloaded {success}/{len(images_to_download)} images")
print("=" * 50)
