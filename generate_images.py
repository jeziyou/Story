import requests
import urllib.parse
import os
import time

os.makedirs("images", exist_ok=True)

API_URL = "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image"

images = [
    {
        "filename": "little_star_cover.png",
        "prompt": "A magical glowing cartoon star with big sparkly eyes, wearing a happy smile, surrounded by twinkling smaller stars in a dreamy night sky, children's book illustration, golden and purple colors, whimsical, 4k quality"
    },
    {
        "filename": "little_star_page1.png",
        "prompt": "A lonely cute tiny cartoon star looking sad and wistful, gazing up at larger brighter stars in a beautiful deep purple-blue night sky, a gentle silver crescent moon in the corner, children's picture book art, soft pastel colors"
    },
    {
        "filename": "little_star_page2.png",
        "prompt": "A friendly smiling crescent moon character with kind eyes and rosy cheeks, happily chatting with a tiny glowing yellow star, fluffy white clouds around them, warm golden light, whimsical children's storybook illustration"
    },
    {
        "filename": "little_star_page3.png",
        "prompt": "A tiny yellow star casting a bright magical beam of light down onto a cute glowing green firefly in a dark enchanted forest, trees with glowing mushrooms, warm golden illumination, children's book illustration, magical night scene"
    },
    {
        "filename": "little_star_page4.png",
        "prompt": "A sweet little girl with pigtails sitting by her bedroom window at night, painting at an easel, looking up and smiling happily at a twinkling star outside the window, cozy warm bedroom with stuffed animals, firefly near the window, children's art style"
    },
    {
        "filename": "little_star_page5.png",
        "prompt": "A tiny glowing star creating a shining light path for a lost cute baby bird flying toward its mother bird in a nest on a tree branch, green leaves, night time scene, warm golden beam of light, children's storybook illustration"
    },
    {
        "filename": "little_star_page6.png",
        "prompt": "All the stars in the sky including a big friendly moon smiling proudly down at a little twinkling star below, showing a firefly glowing in a forest, warm window light in a house, a bird in a nest, panoramic beautiful night sky, children's book illustration"
    },
    {
        "filename": "little_star_page7.png",
        "prompt": "A happy glowing little star with the biggest smile surrounded by friends: a friendly firefly, a baby bird with its mother, a little girl waving from her window, beautiful starry sky full of twinkling stars, warm golden happy ending scene, children's book illustration"
    }
]

print("Generating images with online model...")
print("=" * 60)

success_count = 0
for i, img in enumerate(images):
    encoded_prompt = urllib.parse.quote(img["prompt"])
    url = f"{API_URL}?prompt={encoded_prompt}&image_size=landscape_4_3"

    print(f"\n[{i+1}/{len(images)}] Generating {img['filename']}...")

    try:
        response = requests.get(url, timeout=120)
        print(f"    Status: {response.status_code}, Size: {len(response.content)} bytes")

        if response.status_code == 200 and len(response.content) > 1000:
            filepath = os.path.join("images", img["filename"])
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"    ✓ Saved: {filepath}")
            success_count += 1
        else:
            print(f"    ✗ Failed to save image")

    except Exception as e:
        print(f"    ✗ Error: {e}")

    time.sleep(3)

print("\n" + "=" * 60)
print(f"Generated {success_count}/{len(images)} images")

# Verify images are different
print("\nVerifying images are different:")
os.system("md5sum images/*.png")
