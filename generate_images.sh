#!/bin/bash

IMAGE_DIR="images"
mkdir -p "$IMAGE_DIR"

declare -A IMAGES
IMAGES["little_star_cover.png"]="Cute cartoon little star character with big friendly eyes smiling in night sky, warm golden glow, children's book illustration style, soft dreamy colors, whimsical, 4k quality"
IMAGES["little_star_page1.png"]="Lonely cute cartoon tiny star with sad expression looking up at bigger brighter stars, beautiful purple blue night sky, gentle crescent moon in corner, children's picture book art, soft pastel colors"
IMAGES["little_star_page2.png"]="Friendly smiling crescent moon with kind face talking to tiny glowing star, fluffy white clouds, warm golden light, children's storybook illustration, whimsical cartoon style, night sky background"
IMAGES["little_star_page3.png"]="Tiny star shining bright beam of light down on cute glowing firefly in dark magical forest, trees, mushrooms, warm illumination, children's book illustration, enchanting night scene"
IMAGES["little_star_page4.png"]="Sweet little girl by bedroom window painting at easel, looking up and smiling at twinkling star outside, cozy warm bedroom, stuffed animals, firefly near window, heartwarming children's art style"
IMAGES["little_star_page5.png"]="Tiny star shining light path for lost cute baby bird flying to mother bird in nest on tree branch, leaves, night time, warm glowing light beam, children's storybook illustration, gentle style"
IMAGES["little_star_page6.png"]="All stars in sky including big moon smiling down proudly at little twinkling star, below showing firefly in forest, warm window light, bird in nest, panoramic beautiful night, children's book illustration"
IMAGES["little_star_page7.png"]="Happy glowing little star with big smile surrounded by friends: firefly, baby bird with mother, little girl waving from window, beautiful starry sky, warm golden happy ending, children's book illustration, joy"

API_URL="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image"

echo "Generating images using online model..."
echo "========================================"

for filename in "${!IMAGES[@]}"; do
    prompt="${IMAGES[$filename]}"
    encoded_prompt=$(python3 -c "import urllib.parse; print(urllib.parse.quote('$prompt'))")

    url="${API_URL}?prompt=${encoded_prompt}&image_size=landscape_4_3"

    echo "Generating $filename..."
    curl -s -L -o "${IMAGE_DIR}/${filename}" "$url" --max-time 120

    if [ -f "${IMAGE_DIR}/${filename}" ] && [ -s "${IMAGE_DIR}/${filename}" ]; then
        size=$(stat -c%s "${IMAGE_DIR}/${filename}" 2>/dev/null || stat -f%z "${IMAGE_DIR}/${filename}" 2>/dev/null)
        echo "✓ Saved: $filename ($size bytes)"
    else
        echo "✗ Failed: $filename"
    fi

    sleep 2
done

echo "========================================"
echo "Done! Images saved to: $(pwd)/$IMAGE_DIR"
