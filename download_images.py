import requests
import os
import hashlib
import time
import sys

PLACEHOLDER_SIZE = 176626
PLACEHOLDER_MD5 = "19a0b822edb11957055e4588c2159058"
API_URL = "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image"
OUTPUT_DIR = "/workspace/images"
MAX_RETRIES = 5
RETRY_DELAY = 60
REQUEST_DELAY = 60

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

images = [
    ("little_star_cover.png", "starry night sky cartoon"),
    ("little_star_page1.png", "cartoon moon night"),
    ("little_star_page2.png", "crescent moon stars"),
    ("little_star_page3.png", "magical forest night"),
    ("little_star_page4.png", "cartoon girl window"),
    ("little_star_page5.png", "cute bird tree"),
    ("little_star_page6.png", "starry sky night"),
    ("little_star_page7.png", "happy cartoon friends"),
]

def log(msg, end="\n"):
    print(msg, flush=True, end=end)

def get_md5(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

def get_md5_from_content(content):
    return hashlib.md5(content).hexdigest()

def is_placeholder(file_path=None, content=None):
    if content is not None:
        if len(content) != PLACEHOLDER_SIZE:
            return False
        return get_md5_from_content(content) == PLACEHOLDER_MD5
    else:
        file_size = os.path.getsize(file_path)
        if file_size != PLACEHOLDER_SIZE:
            return False
        file_md5 = get_md5(file_path)
        return file_md5 == PLACEHOLDER_MD5

def download_image(filename, prompt):
    filepath = os.path.join(OUTPUT_DIR, filename)
    params = {
        "prompt": prompt,
        "image_size": "square"
    }
    
    last_content = None
    for attempt in range(1, MAX_RETRIES + 1):
        log(f"Downloading {filename} (attempt {attempt}/{MAX_RETRIES})...")
        try:
            response = requests.get(API_URL, params=params, headers=HEADERS, timeout=180, allow_redirects=True)
            response.raise_for_status()
            content = response.content
            last_content = content
            
            log(f"  Received {len(content)} bytes")
            
            if is_placeholder(content=content):
                log(f"  -> Placeholder detected! ", end="")
                if attempt < MAX_RETRIES:
                    log(f"Retrying in {RETRY_DELAY} seconds...")
                    time.sleep(RETRY_DELAY)
                else:
                    log(f"Max retries reached. Saving placeholder.")
                continue
            
            with open(filepath, "wb") as f:
                f.write(content)
            
            file_size = os.path.getsize(filepath)
            file_md5 = get_md5(filepath)
            log(f"  -> SUCCESS! Size: {file_size} bytes, MD5: {file_md5}")
            return True, file_size, file_md5
            
        except Exception as e:
            log(f"  -> Error: {e}")
            if attempt < MAX_RETRIES:
                log(f"  -> Retrying in {RETRY_DELAY} seconds...")
                time.sleep(RETRY_DELAY)
    
    if last_content is not None:
        with open(filepath, "wb") as f:
            f.write(last_content)
        log(f"  -> Saved last attempt for {filename}")
        file_size = os.path.getsize(filepath)
        file_md5 = get_md5(filepath)
        return False, file_size, file_md5
    
    log(f"  -> Failed to download {filename} after {MAX_RETRIES} attempts")
    return False, 0, ""

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    results = []
    
    log("=" * 60)
    log("Starting image download with image_size=square")
    log(f"Request delay: {REQUEST_DELAY}s, Retry delay: {RETRY_DELAY}s, Max retries: {MAX_RETRIES}")
    log("=" * 60)
    
    for i, (filename, prompt) in enumerate(images):
        success, size, md5 = download_image(filename, prompt)
        results.append((filename, success, size, md5, prompt))
        
        if i < len(images) - 1:
            log(f"Waiting {REQUEST_DELAY} seconds before next request...")
            time.sleep(REQUEST_DELAY)
    
    log("\n" + "=" * 60)
    log("DOWNLOAD SUMMARY")
    log("=" * 60)
    success_count = 0
    for filename, success, size, md5, prompt in results:
        status = "SUCCESS" if success else "FAILED/PLACEHOLDER"
        if success:
            success_count += 1
        log(f"{filename}:")
        log(f"  Prompt: {prompt}")
        log(f"  Status: {status}")
        log(f"  Size: {size} bytes")
        log(f"  MD5: {md5}")
        log("")
    
    log(f"Successfully downloaded: {success_count}/{len(images)} images")

if __name__ == "__main__":
    main()
