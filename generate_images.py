from PIL import Image, ImageDraw, ImageFont
import os
import math
import random

os.makedirs("images", exist_ok=True)

WIDTH = 800
HEIGHT = 600

def create_star(draw, x, y, size, color, points=5):
    angle = math.pi * 2 / points
    outer_r = size
    inner_r = size * 0.4
    coords = []
    for i in range(points * 2):
        r = outer_r if i % 2 == 0 else inner_r
        a = i * angle / 2 - math.pi / 2
        coords.append((x + r * math.cos(a), y + r * math.sin(a)))
    draw.polygon(coords, fill=color, outline=(255, 255, 200))

def create_moon(draw, x, y, size, color):
    draw.ellipse([x - size, y - size, x + size, y + size], fill=color)
    draw.ellipse([x - size//2, y - size, x - size//2 + size*1.5, y + size], fill=(25, 25, 70))

def create_cloud(draw, x, y, size, color):
    for dx, dy, r in [(0, 0, size*0.5), (size*0.4, -size*0.2, size*0.4), (size*0.8, 0, size*0.5), (size*0.3, size*0.1, size*0.35)]:
        draw.ellipse([x+dx-r, y+dy-r, x+dx+r, y+dy+r], fill=color)

def create_tree(draw, x, y, height):
    trunk_w = height * 0.15
    draw.rectangle([x - trunk_w//2, y, x + trunk_w//2, y + height*0.3], fill=(101, 67, 33))
    for i in range(3):
        w = height * 0.5 * (1 - i * 0.15)
        ty = y - height * 0.4 + i * height * 0.25
        draw.polygon([(x - w, ty), (x + w, ty), (x, ty - height*0.35)], fill=(34, 100, 34))

def create_house(draw, x, y, size):
    draw.rectangle([x - size, y - size, x + size, y + size], fill=(210, 180, 140))
    draw.polygon([(x - size*1.2, y - size), (x + size*1.2, y - size), (x, y - size*2)], fill=(139, 69, 19))
    draw.rectangle([x - size*0.3, y, x + size*0.3, y + size], fill=(101, 67, 33))
    draw.rectangle([x - size*0.8, y - size*0.7, x - size*0.4, y - size*0.2], fill=(173, 216, 230))
    draw.rectangle([x + size*0.4, y - size*0.7, x + size*0.8, y - size*0.2], fill=(173, 216, 230))

def get_font(size):
    try:
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size)
    except:
        return ImageFont.load_default()

images = []

# 1. Cover
img = Image.new('RGB', (WIDTH, HEIGHT), (20, 20, 60))
draw = ImageDraw.Draw(img)
for i in range(50):
    sx, sy = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    create_star(draw, sx, sy, random.randint(3, 8), (255, 255, random.randint(150, 255)))
create_moon(draw, 120, 100, 60, (255, 248, 220))
create_star(draw, WIDTH//2, HEIGHT//2 + 30, 100, (255, 215, 0))
for _ in range(20):
    rx = WIDTH//2 + random.randint(-150, 150)
    ry = HEIGHT//2 + 30 + random.randint(-150, 150)
    create_star(draw, rx, ry, random.randint(2, 5), (255, 255, 200))
font = get_font(40)
draw.text((WIDTH//2, HEIGHT - 80), "✨ The Little Star ✨", fill=(255, 215, 0), font=font, anchor="mm")
font_sm = get_font(20)
draw.text((WIDTH//2, HEIGHT - 40), "Children's Story", fill=(200, 200, 255), font=font_sm, anchor="mm")
images.append(("little_star_cover.png", img))

# 2. Page 1 - Lonely star
img = Image.new('RGB', (WIDTH, HEIGHT), (30, 25, 80))
draw = ImageDraw.Draw(img)
for i in range(30):
    sx, sy = random.randint(0, WIDTH), random.randint(0, HEIGHT//2)
    create_star(draw, sx, sy, random.randint(8, 20), (255, 255, random.randint(200, 255)))
create_moon(draw, 680, 80, 45, (255, 248, 220))
create_star(draw, 150, 450, 25, (180, 180, 220))
images.append(("little_star_page1.png", img))

# 3. Page 2 - Moon talking
img = Image.new('RGB', (WIDTH, HEIGHT), (25, 30, 90))
draw = ImageDraw.Draw(img)
create_cloud(draw, 100, 150, 80, (80, 80, 120))
create_cloud(draw, 500, 80, 70, (70, 70, 110))
create_moon(draw, 250, 200, 80, (255, 248, 220))
draw.ellipse([220, 170, 240, 190], fill=(0,0,0))
draw.ellipse([270, 170, 290, 190], fill=(0,0,0))
draw.arc([230, 190, 280, 230], 0, 180, fill=(0,0,0), width=3)
create_star(draw, 550, 350, 50, (255, 215, 0))
images.append(("little_star_page2.png", img))

# 4. Page 3 - Forest firefly
img = Image.new('RGB', (WIDTH, HEIGHT), (15, 40, 20))
draw = ImageDraw.Draw(img)
for i in range(10):
    create_tree(draw, 50 + i*80, 550, 180)
create_star(draw, 400, 100, 60, (255, 215, 0))
draw.polygon([(380, 160), (420, 160), (400, 350)], fill=(255, 255, 200, 50))
for i in range(15):
    fx = 350 + i*5
    fy = 160 + i*12
    draw.ellipse([fx-3, fy-3, fx+3, fy+3], fill=(255, 255, 100))
draw.ellipse([385, 360, 415, 390], fill=(255, 255, 100))
draw.ellipse([390, 365, 398, 373], fill=(0,0,0))
draw.ellipse([402, 365, 410, 373], fill=(0,0,0))
for i in range(8):
    mx = random.randint(100, 700)
    my = random.randint(400, 550)
    draw.ellipse([mx-8, my-5, mx-2, my+5], fill=(200, 100, 50))
    draw.ellipse([mx+2, my-5, mx+8, my+5], fill=(220, 220, 220))
images.append(("little_star_page3.png", img))

# 5. Page 4 - Girl painting
img = Image.new('RGB', (WIDTH, HEIGHT), (60, 50, 80))
draw = ImageDraw.Draw(img)
draw.rectangle([0, HEIGHT-150, WIDTH, HEIGHT], fill=(180, 140, 100))
create_house(draw, 200, 400, 120)
for wx in [130, 170, 230, 270]:
    draw.rectangle([wx-15, 330, wx+15, 390], fill=(255, 220, 150))
draw.rectangle([450, 200, 750, 500], fill=(100, 150, 200))
draw.rectangle([460, 210, 740, 490], fill=(150, 200, 255))
create_star(draw, 700, 100, 35, (255, 215, 0))
draw.ellipse([520, 300, 570, 370], fill=(255, 200, 150))
draw.rectangle([520, 360, 570, 450], fill=(255, 150, 150))
draw.rectangle([580, 340, 620, 450], fill=(255, 200, 150))
draw.rectangle([600, 310, 680, 400], fill=(255, 255, 200))
draw.ellipse([605, 280, 630, 305], fill=(100, 100, 200))
draw.ellipse([655, 280, 680, 305], fill=(100, 100, 200))
images.append(("little_star_page4.png", img))

# 6. Page 5 - Baby bird
img = Image.new('RGB', (WIDTH, HEIGHT), (20, 30, 70))
draw = ImageDraw.Draw(img)
draw.rectangle([0, 500, WIDTH, HEIGHT], fill=(30, 80, 30))
draw.rectangle([200, 400, 600, 420], fill=(101, 67, 33))
create_tree(draw, 150, 500, 200)
create_tree(draw, 650, 500, 180)
draw.ellipse([350, 370, 450, 430], fill=(139, 90, 43))
draw.ellipse([380, 350, 440, 380], fill=(180, 120, 60))
draw.ellipse([390, 385, 405, 400], fill=(0,0,0))
draw.ellipse([415, 385, 430, 400], fill=(0,0,0))
draw.polygon([(440, 395), (460, 400), (440, 405)], fill=(255, 165, 0))
create_star(draw, 200, 150, 40, (255, 215, 0))
for i in range(20):
    bx = 200 - (i+1)*8
    by = 190 + i*13
    if by < 400:
        draw.ellipse([bx-2, by-2, bx+2, by+2], fill=(255, 255, 200))
draw.ellipse([100, 350, 150, 400], fill=(200, 180, 100))
draw.polygon([(145, 370), (160, 375), (145, 380)], fill=(255, 165, 0))
images.append(("little_star_page5.png", img))

# 7. Page 6 - All stars smiling
img = Image.new('RGB', (WIDTH, HEIGHT), (25, 20, 70))
draw = ImageDraw.Draw(img)
for i in range(40):
    sx, sy = random.randint(0, WIDTH), random.randint(0, HEIGHT//2 - 50)
    s = random.randint(5, 25)
    create_star(draw, sx, sy, s, (255, 255, random.randint(180, 255)))
create_moon(draw, 100, 100, 50, (255, 248, 220))
create_star(draw, 400, 250, 70, (255, 215, 0))
draw.rectangle([0, HEIGHT-150, WIDTH, HEIGHT], fill=(20, 50, 20))
draw.ellipse([150, 500, 170, 520], fill=(255, 255, 100))
create_house(draw, 650, 520, 80)
draw.rectangle([610, 470, 690, 490], fill=(255, 220, 150))
draw.ellipse([400, 480, 440, 510], fill=(139, 90, 43))
images.append(("little_star_page6.png", img))

# 8. Page 7 - Happy ending
img = Image.new('RGB', (WIDTH, HEIGHT), (30, 25, 80))
draw = ImageDraw.Draw(img)
for i in range(60):
    sx, sy = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    create_star(draw, sx, sy, random.randint(2, 6), (255, 255, random.randint(180, 255)))
create_star(draw, WIDTH//2, 200, 90, (255, 215, 0))
draw.ellipse([WIDTH//2-25, 170, WIDTH//2-5, 190], fill=(0,0,0))
draw.ellipse([WIDTH//2+5, 170, WIDTH//2+25, 190], fill=(0,0,0))
draw.arc([WIDTH//2-20, 185, WIDTH//2+20, 220], 0, 180, fill=(0,0,0), width=3)
draw.ellipse([150, 380, 175, 405], fill=(255, 255, 100))
draw.ellipse([250, 400, 290, 430], fill=(200, 180, 100))
draw.ellipse([500, 350, 550, 420], fill=(255, 200, 150))
draw.rectangle([480, 420, 570, 520], fill=(255, 150, 200))
draw.rectangle([560, 380, 620, 520], fill=(255, 200, 150))
font = get_font(30)
draw.text((WIDTH//2, HEIGHT - 50), "✨ Happy Ending ✨", fill=(255, 215, 0), font=font, anchor="mm")
images.append(("little_star_page7.png", img))

print("Generating images offline with Pillow...")
print("=" * 50)
for filename, img in images:
    filepath = os.path.join("images", filename)
    img.save(filepath, "PNG")
    print(f"✓ Saved: {filepath}")

print("=" * 50)
print(f"Generated {len(images)} images successfully!")
print("Verifying images:")
os.system("md5sum images/*.png")
