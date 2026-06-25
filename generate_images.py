import requests
import urllib.parse
import os
import time
import hashlib

IMAGE_DIR = "images"
os.makedirs(IMAGE_DIR, exist_ok=True)

API_URL = "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image"
PLACEHOLDER_MD5 = "19a0b822edb11957055e4588c2159058"

images = [
    {
        "filename": "little_star_cover.png",
        "prompt": "Cute cartoon little star character with big friendly eyes smiling in night sky, warm golden glow, children's book illustration style, soft dreamy colors, whimsical",
    },
    {
        "filename": "little_star_page1.png",
        "prompt": "Lonely cute cartoon tiny star with sad expression looking up at bigger brighter stars, beautiful purple blue night sky, gentle crescent moon, children's picture book art, soft pastel colors",
    },
    {
        "filename": "little_star_page2.png",
        "prompt": "Friendly smiling crescent moon with kind face talking to tiny glowing star, fluffy white clouds, warm golden light, children's storybook illustration, whimsical cartoon style, night sky background",
    },
    {
        "filename": "little_star_page3.png",
        "prompt": "Tiny star shining bright beam of light down on cute glowing firefly in dark magical forest, trees and mushrooms, warm illumination, children's book illustration, enchanting night scene",
    },
    {
        "filename": "little_star_page4.png",
        "prompt": "Sweet little girl by bedroom window painting at easel, looking up and smiling at twinkling star outside, cozy warm bedroom, stuffed animals, firefly near window, heartwarming children's art style",
    },
    {
        "filename": "little_star_page5.png",
        "prompt": "Tiny star shining light path for lost cute baby bird flying to mother bird in nest on tree branch, green leaves, night time, warm glowing light beam, children's storybook illustration, gentle style",
    },
    {
        "filename": "little_star_page6.png",
        "prompt": "All stars in sky including big moon smiling down proudly at little twinkling star, showing firefly in forest, warm window light, bird in nest, panoramic beautiful night, children's book illustration",
    },
    {
        "filename": "little_star_page7.png",
        "prompt": "Happy glowing little star with big smile surrounded by friends firefly, baby bird with mother, little girl waving from window, beautiful starry sky, warm golden happy ending, children's book illustration, joy",
    }
]

def download_image(prompt, filename, image_size="landscape_4_3", max_retries=10):
    filepath = os.path.join(IMAGE_DIR, filename)
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"{API_URL}?prompt={encoded_prompt}&image_size={image_size}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    }

    for attempt in range(max_retries):
        try:
            print(f"  Attempt {attempt+1}/{max_retries}...", end=" ", flush=True)
            response = requests.get(url, headers=headers, timeout=180, allow_redirects=True)
            content = response.content
            size = len(content)
            md5 = hashlib.md5(content).hexdigest()

            if response.status_code == 200 and size > 50000 and md5 != PLACEHOLDER_MD5:
                with open(filepath, 'wb') as f:
                    f.write(content)
                print(f"✓ SUCCESS ({size} bytes)")
                return True
            else:
                wait_time = 30 + attempt * 15
                print(f"placeholder/too small ({size}b), waiting {wait_time}s...")
                time.sleep(wait_time)
        except Exception as e:
            print(f"error: {e}, waiting 30s...")
            time.sleep(30)

    print(f"  ✗ Failed after {max_retries} attempts")
    return False

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--one":
        idx = int(sys.argv[2]) if len(sys.argv) > 2 else 0
        if 0 <= idx < len(images):
            img = images[idx]
            print(f"Downloading single image: {img['filename']}")
            download_image(img["prompt"], img["filename"])
        else:
            print(f"Invalid index. Use 0-{len(images)-1}")
    else:
        print("=" * 60)
        print("Downloading story images (this may take a while)")
        print("Tip: Run with --one <index> to download one at a time")
        print("=" * 60)

        success = 0
        for i, img in enumerate(images):
            filepath = os.path.join(IMAGE_DIR, img["filename"])
            if os.path.exists(filepath) and os.path.getsize(filepath) > 50000:
                print(f"[{i+1}/{len(images)}] {img['filename']} already exists, skipping")
                success += 1
                continue

            print(f"\n[{i+1}/{len(images)}] Downloading {img['filename']}...")
            if download_image(img["prompt"], img["filename"]):
                success += 1
            if i < len(images) - 1:
                print(f"  Waiting 60s before next image...")
                time.sleep(60)

        print("\n" + "=" * 60)
        print(f"Downloaded {success}/{len(images)} images successfully!")
        print(f"Images saved to: {os.path.abspath(IMAGE_DIR)}")
        print("=" * 60)
