import requests
import urllib.parse
import os
import time

IMAGE_DIR = "images"
os.makedirs(IMAGE_DIR, exist_ok=True)

FIXED_SEEDS = {
    "little_star_cover.png": 42,
    "little_star_page1.png": 101,
    "little_star_page2.png": 202,
    "little_star_page3.png": 303,
    "little_star_page4.png": 404,
    "little_star_page5.png": 505,
    "little_star_page6.png": 606,
    "little_star_page7.png": 707,
}

def generate_with_seed(prompt, filename, image_size="landscape_4_3", seed=None, retries=3):
    filepath = os.path.join(IMAGE_DIR, filename)
    
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt={encoded_prompt}&image_size={image_size}"
    if seed is not None:
        url += f"&seed={seed}"
    
    print(f"Generating {filename} (seed={seed})...")
    
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=120)
            if response.status_code == 200 and len(response.content) > 1000:
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                print(f"✓ Saved: {filename} ({len(response.content)} bytes)")
                time.sleep(2)
                return True
            else:
                print(f"  Attempt {attempt+1} failed: HTTP {response.status_code}, size={len(response.content)}")
                time.sleep(3)
        except Exception as e:
            print(f"  Attempt {attempt+1} error: {e}")
            time.sleep(3)
    
    print(f"✗ Failed to generate: {filename}")
    return False

images = [
    {
        "filename": "little_star_cover.png",
        "prompt": "Cute cartoon little star character with big friendly eyes smiling in night sky, warm golden glow, children's book illustration style, soft dreamy colors, whimsical, 4k quality",
        "size": "landscape_4_3"
    },
    {
        "filename": "little_star_page1.png",
        "prompt": "Lonely cute cartoon tiny star with sad expression looking up at bigger brighter stars, beautiful purple blue night sky, gentle crescent moon in corner, children's picture book art, soft pastel colors",
        "size": "landscape_4_3"
    },
    {
        "filename": "little_star_page2.png",
        "prompt": "Friendly smiling crescent moon with kind face talking to tiny glowing star, fluffy white clouds, warm golden light, children's storybook illustration, whimsical cartoon style, night sky background",
        "size": "landscape_4_3"
    },
    {
        "filename": "little_star_page3.png",
        "prompt": "Tiny star shining bright beam of light down on cute glowing firefly in dark magical forest, trees, mushrooms, warm illumination, children's book illustration, enchanting night scene",
        "size": "landscape_4_3"
    },
    {
        "filename": "little_star_page4.png",
        "prompt": "Sweet little girl by bedroom window painting at easel, looking up and smiling at twinkling star outside, cozy warm bedroom, stuffed animals, firefly near window, heartwarming children's art style",
        "size": "landscape_4_3"
    },
    {
        "filename": "little_star_page5.png",
        "prompt": "Tiny star shining light path for lost cute baby bird flying to mother bird in nest on tree branch, leaves, night time, warm glowing light beam, children's storybook illustration, gentle style",
        "size": "landscape_4_3"
    },
    {
        "filename": "little_star_page6.png",
        "prompt": "All stars in sky including big moon smiling down proudly at little twinkling star, below showing firefly in forest, warm window light, bird in nest, panoramic beautiful night, children's book illustration",
        "size": "landscape_4_3"
    },
    {
        "filename": "little_star_page7.png",
        "prompt": "Happy glowing little star with big smile surrounded by friends: firefly, baby bird with mother, little girl waving from window, beautiful starry sky, warm golden happy ending, children's book illustration, joy",
        "size": "landscape_4_3"
    }
]

print("=" * 60)
print("Generating story images with fixed seeds (offline version)")
print("=" * 60)

success = 0
for img in images:
    seed = FIXED_SEEDS.get(img["filename"])
    if generate_with_seed(img["prompt"], img["filename"], img["size"], seed=seed):
        success += 1

print("=" * 60)
print(f"Generated {success}/{len(images)} images successfully!")
print(f"Images saved to: {os.path.abspath(IMAGE_DIR)}")
print("=" * 60)
