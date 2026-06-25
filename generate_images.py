from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import math
import random

os.makedirs("images", exist_ok=True)

W, H = 1024, 1024

def get_font(size, bold=False):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def new_img(c1, c2):
    img = Image.new('RGBA', (W, H), c1 + (255,))
    draw = ImageDraw.Draw(img)
    for y in range(H):
        ratio = y / H
        r = int(c1[0] + (c2[0] - c1[0]) * ratio)
        g = int(c1[1] + (c2[1] - c1[1]) * ratio)
        b = int(c1[2] + (c2[2] - c1[2]) * ratio)
        draw.line([(0, y), (W, y)], fill=(r, g, b, 255))
    return img, draw

def radial_glow(img, cx, cy, radius, color, alpha=80):
    glow = Image.new('RGBA', img.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    for r in range(radius, 0, -3):
        a = int(alpha * (1 - r / radius) ** 1.5)
        gd.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(*color, a))
    return Image.alpha_composite(img, glow)

def draw_star(draw, x, y, size, color, points=5, outline=None):
    angle = math.pi * 2 / points
    outer_r, inner_r = size, size * 0.42
    coords = []
    for i in range(points * 2):
        r = outer_r if i % 2 == 0 else inner_r
        a = i * angle / 2 - math.pi / 2
        coords.append((x + r * math.cos(a), y + r * math.sin(a)))
    fill = color if len(color) == 4 else color + (255,)
    ol = outline if outline is None or len(outline) == 4 else outline + (255,) if outline else None
    draw.polygon(coords, fill=fill, outline=ol)

def draw_star_face(draw, cx, cy, size):
    eye_y = cy - size * 0.05
    eye_off = size * 0.22
    eye_r = size * 0.1
    draw.ellipse([cx - eye_off - eye_r, eye_y - eye_r, cx - eye_off + eye_r, eye_y + eye_r], fill=(30, 20, 50, 255))
    draw.ellipse([cx + eye_off - eye_r, eye_y - eye_r, cx + eye_off + eye_r, eye_y + eye_r], fill=(30, 20, 50, 255))
    hw = size * 0.08
    draw.ellipse([cx - eye_off - eye_r + hw, eye_y - eye_r + hw//2, cx - eye_off - eye_r + hw*2, eye_y - eye_r + hw*2], fill=(255,255,255,200))
    draw.ellipse([cx + eye_off - eye_r + hw, eye_y - eye_r + hw//2, cx + eye_off - eye_r + hw*2, eye_y - eye_r + hw*2], fill=(255,255,255,200))
    mouth_y = cy + size * 0.18
    draw.arc([cx - size*0.18, mouth_y - size*0.1, cx + size*0.18, mouth_y + size*0.18], 10, 170, fill=(30, 20, 50, 255), width=max(2, int(size*0.04)))
    blush_r = int(size * 0.08)
    blush_y = cy + size * 0.08
    draw.ellipse([cx - size*0.35 - blush_r, blush_y - blush_r, cx - size*0.35 + blush_r, blush_y + blush_r], fill=(255, 150, 150, 60))
    draw.ellipse([cx + size*0.35 - blush_r, blush_y - blush_r, cx + size*0.35 + blush_r, blush_y + blush_r], fill=(255, 150, 150, 60))

def draw_cute_moon(draw, x, y, size, bg_color, color=(255, 245, 210)):
    draw.ellipse([x - size, y - size, x + size, y + size], fill=color + (255,))
    draw.ellipse([x - size*0.35, y - size*1.05, x + size*1.2, y + size*1.05], fill=bg_color + (255,))
    eye_r = size * 0.1
    eye_y = y - size * 0.1
    eye_off = size * 0.25
    draw.ellipse([x - eye_off - eye_r - size*0.1, eye_y - eye_r, x - eye_off + eye_r - size*0.1, eye_y + eye_r], fill=(30, 20, 50, 255))
    draw.ellipse([x + eye_off - eye_r - size*0.15, eye_y - eye_r, x + eye_off + eye_r - size*0.15, eye_y + eye_r], fill=(30, 20, 50, 255))
    hw = size * 0.06
    draw.ellipse([x - eye_off - eye_r - size*0.1 + hw, eye_y - eye_r + hw//2, x - eye_off - eye_r - size*0.1 + hw*2, eye_y - eye_r + hw*2], fill=(255,255,255,200))
    draw.ellipse([x + eye_off - eye_r - size*0.15 + hw, eye_y - eye_r + hw//2, x + eye_off - eye_r - size*0.15 + hw*2, eye_y - eye_r + hw*2], fill=(255,255,255,200))
    draw.arc([x - size*0.25, y + size*0.05, x + size*0.05, y + size*0.35], 10, 170, fill=(30, 20, 50, 255), width=max(2, int(size*0.04)))

def draw_cloud(draw, x, y, size, color=(255, 255, 255, 120)):
    parts = [(0, 0, size*0.45), (size*0.35, -size*0.2, size*0.4), (size*0.7, -size*0.1, size*0.42),
             (size*0.2, size*0.1, size*0.35), (size*0.55, size*0.12, size*0.32)]
    for dx, dy, r in parts:
        draw.ellipse([int(x+dx-r), int(y+dy-r), int(x+dx+r), int(y+dy+r)], fill=color)

def draw_tree(draw, x, y_base, height, color=(30, 90, 40)):
    trunk_w = height * 0.12
    draw.rectangle([x - int(trunk_w//2), y_base - int(height*0.25), x + int(trunk_w//2), y_base], fill=(100, 65, 30, 255))
    for i in range(3):
        w = height * (0.48 - i * 0.08)
        ty = y_base - int(height * 0.3) - int(i * height * 0.2)
        draw.polygon([(x - int(w), ty), (x + int(w), ty), (x, int(ty - height*0.35))], fill=color + (255,))

def draw_house(draw, x, y, size, lit=True):
    draw.rectangle([x - size, y - size, x + size, y + size], fill=(220, 190, 150, 255))
    draw.polygon([(x - int(size*1.15), y - size), (x + int(size*1.15), y - size), (x, y - int(size*1.9))], fill=(150, 70, 40, 255))
    draw.rectangle([x - int(size*0.25), y, x + int(size*0.25), y + size], fill=(100, 60, 30, 255))
    wcolor = (255, 230, 150, 255) if lit else (100, 120, 140, 255)
    draw.rectangle([x - int(size*0.75), y - int(size*0.7), x - int(size*0.4), y - int(size*0.25)], fill=wcolor)
    draw.rectangle([x + int(size*0.4), y - int(size*0.7), x + int(size*0.75), y - int(size*0.25)], fill=wcolor)

def draw_bird(draw, x, y, size, color=(255, 200, 100), beak=(255, 165, 0)):
    c = color + (255,)
    b = beak + (255,)
    draw.ellipse([int(x - size), int(y - size*0.7), int(x + size), int(y + size*0.7)], fill=c)
    draw.ellipse([int(x + size*0.3), int(y - size*0.9), int(x + size*1.1), int(y - size*0.1)], fill=c)
    eye_r = size * 0.1
    draw.ellipse([int(x + size*0.55 - eye_r), int(y - size*0.65 - eye_r), int(x + size*0.55 + eye_r), int(y - size*0.65 + eye_r)], fill=(0,0,0,255))
    draw.polygon([(int(x + size*1.1), int(y - size*0.5)), (int(x + size*1.5), int(y - size*0.4)), (int(x + size*1.1), int(y - size*0.3))], fill=b)
    draw.ellipse([int(x - size*0.8), int(y - size*0.2), int(x - size*0.2), int(y + size*0.4)], fill=c)
    draw.ellipse([int(x + size*0.1), int(y - size*0.1), int(x + size*0.7), int(y + size*0.5)], fill=c)

def draw_firefly(draw, x, y, size=8):
    for r in [size*6, size*4, size*2]:
        a = int(60 * (1 - r/(size*6)))
        draw.ellipse([int(x-r), int(y-r), int(x+r), int(y+r)], fill=(255, 255, 100, a))
    draw.ellipse([int(x-size), int(y-size), int(x+size), int(y+size)], fill=(255, 255, 180, 255))

def draw_girl(draw, x, y, size):
    skin = (255, 210, 170, 255)
    hair = (120, 70, 30, 255)
    dress = (255, 130, 170, 255)
    draw.polygon([(int(x - size*0.8), int(y + size*1.2)), (int(x + size*0.8), int(y + size*1.2)), (x, int(y - size*0.1))], fill=dress)
    draw.ellipse([int(x - size*0.45), int(y - size*0.9), int(x + size*0.45), int(y - size*0.05)], fill=skin)
    draw.ellipse([int(x - size*0.55), int(y - size*1.0), int(x + size*0.55), int(y - size*0.2)], fill=hair)
    draw.pieslice([int(x - size*0.55), int(y - size*1.0), int(x + size*0.55), int(y - size*0.1)], 180, 360, fill=hair)
    eye_y = int(y - size*0.5)
    draw.ellipse([int(x - size*0.2 - 3), eye_y - 3, int(x - size*0.2 + 3), eye_y + 3], fill=(0,0,0,255))
    draw.ellipse([int(x + size*0.2 - 3), eye_y - 3, int(x + size*0.2 + 3), eye_y + 3], fill=(0,0,0,255))
    draw.arc([int(x - size*0.15), int(y - size*0.35), int(x + size*0.15), int(y - size*0.15)], 0, 180, fill=(200, 100, 100, 255), width=2)

def add_twinkles(draw, count, seed=42):
    rng = random.Random(seed)
    for _ in range(count):
        sx, sy = rng.randint(20, W-20), rng.randint(20, H-20)
        ss = rng.randint(1, 3)
        bright = rng.randint(200, 255)
        draw.ellipse([sx-ss, sy-ss, sx+ss, sy+ss], fill=(bright, bright, rng.randint(180, 255), 255))
        if ss > 1:
            draw.line([(sx-ss*2, sy), (sx+ss*2, sy)], fill=(bright, bright, 200, 150), width=1)
            draw.line([(sx, sy-ss*2), (sx, sy+ss*2)], fill=(bright, bright, 200, 150), width=1)

def save_img(img, name):
    rgb = img.convert('RGB').filter(ImageFilter.SMOOTH)
    rgb.save(os.path.join("images", name), "PNG")
    print(f"  Saved {name}")

print("Generating children's story illustrations...\n")

# 1. Cover
img, draw = new_img((15, 15, 60), (60, 30, 90))
add_twinkles(draw, 80, seed=1)
img = radial_glow(img, W//2, H//2 - 40, 250, (255, 220, 100), alpha=70)
draw = ImageDraw.Draw(img)
draw_star(draw, W//2, H//2 - 60, 140, (255, 220, 80), outline=(255, 240, 150))
draw_star_face(draw, W//2, H//2 - 80, 120)
draw_cute_moon(draw, 130, 130, 55, (60, 30, 90))
rng = random.Random(10)
for i in range(5):
    s = 12 + i * 4
    draw_star(draw, 820 + i*15, 150 + i*25, s, (255, 230, 150, 200))
draw_cloud(draw, 200, 200, 45, (100, 90, 140, 60))
draw_cloud(draw, 700, 260, 40, (90, 80, 130, 50))
font_big = get_font(56, bold=True)
font_sm = get_font(30)
draw.text((W//2, H - 130), "The Little Star", fill=(255, 220, 100, 255), font=font_big, anchor="mm")
draw.text((W//2, H - 70), "Children's Story", fill=(200, 190, 230, 255), font=font_sm, anchor="mm")
save_img(img, "little_star_cover.png")

# 2. Page 1 - Lonely star
img, draw = new_img((20, 15, 70), (80, 40, 120))
add_twinkles(draw, 60, seed=2)
draw_cute_moon(draw, 840, 120, 50, (80, 40, 120))
for i in range(6):
    sx = 180 + i * 120
    sy = 140 + (i % 2) * 60
    ss = 25 + (i % 3) * 10
    draw_star(draw, sx, sy, ss, (255, 240, 180), outline=(255, 255, 220))
img = radial_glow(img, 180, H - 160, 140, (200, 200, 255), alpha=50)
draw = ImageDraw.Draw(img)
draw_star(draw, 180, H - 180, 60, (190, 190, 220))
draw_star_face(draw, 180, H - 190, 50)
draw.arc([160, H - 150, 200, H - 125], 200, 340, fill=(80, 80, 130, 200), width=2)
draw_cloud(draw, 100, 280, 55, (70, 60, 110, 50))
save_img(img, "little_star_page1.png")

# 3. Page 2 - Moon talking to star
img, draw = new_img((25, 30, 80), (50, 50, 110))
add_twinkles(draw, 50, seed=3)
draw_cloud(draw, 80, 90, 60, (255, 255, 255, 70))
draw_cloud(draw, 620, 170, 50, (240, 240, 255, 60))
draw_cloud(draw, 320, 70, 45, (255, 255, 255, 50))
img = radial_glow(img, 270, 290, 160, (255, 240, 200), alpha=60)
draw = ImageDraw.Draw(img)
draw_cute_moon(draw, 270, 290, 95, (50, 50, 110))
img = radial_glow(img, 700, 440, 140, (255, 220, 100), alpha=70)
draw = ImageDraw.Draw(img)
draw_star(draw, 700, 440, 85, (255, 220, 80), outline=(255, 240, 150))
draw_star_face(draw, 700, 430, 72)
for i in range(3):
    bx = 370 + i*28
    by = 230 - i*10
    draw.ellipse([bx-10, by-8, bx+10, by+8], fill=(255,255,255,100))
save_img(img, "little_star_page2.png")

# 4. Page 3 - Forest with firefly
img, draw = new_img((8, 25, 15), (18, 55, 35))
for i in range(8):
    draw_tree(draw, 40 + i * 130, H - 30, 230 + (i%3)*20, (20+i*5, 75+i*4, 30+i*2))
add_twinkles(draw, 30, seed=4)
img = radial_glow(img, W//2, 170, 220, (255, 230, 100), alpha=80)
draw = ImageDraw.Draw(img)
draw_star(draw, W//2, 170, 90, (255, 220, 80), outline=(255, 240, 150))
draw_star_face(draw, W//2, 160, 78)
for i in range(25):
    fy = 260 + i * 23
    fx = W//2 + int(70 * math.sin(i * 0.6))
    draw.ellipse([fx-2, fy-2, fx+2, fy+2], fill=(255, 255, 180, 180))
draw_firefly(draw, W//2, H - 180, 14)
rng2 = random.Random(5)
for i in range(12):
    fx = rng2.randint(80, W-80)
    fy = rng2.randint(H//2 + 50, H - 60)
    draw_firefly(draw, fx, fy, 4 + rng2.randint(0,3))
for i in range(5):
    mx = 80 + i * 200
    my = H - 50
    draw.ellipse([mx-12, my-8, mx-2, my+8], fill=(180, 80, 50, 255))
    draw.ellipse([mx+2, my-8, mx+12, my+8], fill=(200, 200, 200, 255))
save_img(img, "little_star_page3.png")

# 5. Page 4 - Girl by window
img, draw = new_img((35, 25, 65), (75, 55, 100))
add_twinkles(draw, 35, seed=6)
draw_house(draw, 180, H - 220, 90, lit=True)
draw.rectangle([480, 80, W-70, H-80], fill=(100, 140, 190, 255), outline=(70, 100, 140, 255), width=5)
draw.rectangle([490, 90, W-80, H-90], fill=(150, 190, 230, 255))
img = radial_glow(img, 800, 190, 120, (255, 220, 100), alpha=90)
draw = ImageDraw.Draw(img)
draw_star(draw, 800, 190, 50, (255, 220, 80))
draw_firefly(draw, 570, 480, 9)
draw_girl(draw, 720, 540, 85)
draw.rectangle([520, 370, 620, 540], fill=(255, 250, 220, 255), outline=(180, 160, 120, 255), width=2)
draw.rectangle([615, 390, 628, 550], fill=(140, 90, 40, 255))
draw_firefly(draw, 280, H - 90, 7)
draw_firefly(draw, 380, H - 120, 6)
save_img(img, "little_star_page4.png")

# 6. Page 5 - Baby bird
img, draw = new_img((15, 20, 60), (35, 50, 90))
add_twinkles(draw, 40, seed=7)
draw.rectangle([0, H - 90, W, H], fill=(25, 65, 28, 255))
draw.rectangle([230, H - 210, 770, H - 190], fill=(100, 65, 30, 255))
draw_tree(draw, 110, H - 70, 260)
draw_tree(draw, 910, H - 70, 240)
draw.ellipse([440, H - 280, 540, H - 210], fill=(150, 100, 50, 255))
draw.ellipse([430, H - 300, 550, H - 250], fill=(180, 120, 60, 255))
draw_bird(draw, 490, H - 260, 24, color=(200, 160, 100))
img = radial_glow(img, 190, 190, 160, (255, 230, 100), alpha=70)
draw = ImageDraw.Draw(img)
draw_star(draw, 190, 190, 70, (255, 220, 80))
for i in range(28):
    bx = 190 - i * 6
    by = 260 + i * 16
    if by < H - 220:
        draw.ellipse([bx-3, by-3, bx+3, by+3], fill=(255, 255, 150, 150))
draw_bird(draw, 340, 510, 22, color=(255, 210, 130))
save_img(img, "little_star_page5.png")

# 7. Page 6 - All stars smiling
img, draw = new_img((18, 10, 55), (55, 30, 100))
add_twinkles(draw, 75, seed=8)
draw_cute_moon(draw, 110, 110, 52, (55, 30, 100))
positions = [(290, 95, 38), (440, 75, 42), (590, 100, 36), (740, 85, 40), (880, 120, 33),
             (190, 190, 28), (390, 170, 32), (540, 210, 26), (690, 160, 30), (840, 200, 28)]
for sx, sy, ss in positions:
    draw_star(draw, sx, sy, ss, (255, 240, 180), outline=(255, 255, 220))
img = radial_glow(img, W//2, 340, 200, (255, 220, 100), alpha=100)
draw = ImageDraw.Draw(img)
draw_star(draw, W//2, 340, 105, (255, 220, 80), outline=(255, 240, 150))
draw_star_face(draw, W//2, 330, 90)
draw.rectangle([0, H - 110, W, H], fill=(18, 48, 22, 255))
draw_house(draw, 810, H - 170, 55, lit=True)
draw_firefly(draw, 190, H - 70, 9)
draw_firefly(draw, 290, H - 90, 7)
draw.ellipse([480, H - 120, 550, H - 75], fill=(150, 100, 50, 255))
draw_bird(draw, 515, H - 100, 13, color=(200, 170, 110))
save_img(img, "little_star_page6.png")

# 8. Page 7 - Happy ending
img, draw = new_img((22, 12, 65), (65, 35, 105))
add_twinkles(draw, 90, seed=9)
rng3 = random.Random(11)
for i in range(8):
    sx = rng3.randint(60, W-60)
    sy = rng3.randint(60, 280)
    ss = rng3.randint(14, 28)
    draw_star(draw, sx, sy, ss, (255, 240, 180, 220))
img = radial_glow(img, W//2, 290, 220, (255, 220, 100), alpha=110)
draw = ImageDraw.Draw(img)
draw_star(draw, W//2, 290, 115, (255, 220, 80), outline=(255, 240, 150))
draw_star_face(draw, W//2, 280, 98)
draw_firefly(draw, 240, 490, 13)
draw_firefly(draw, 290, 550, 9)
draw_bird(draw, 370, 520, 27, color=(255, 200, 120))
draw_bird(draw, 310, 500, 19, color=(220, 180, 130))
draw_girl(draw, 710, 510, 82)
draw.rectangle([0, H - 70, W, H], fill=(25, 55, 30, 255))
for i in range(8):
    draw_firefly(draw, rng3.randint(60, W-60), rng3.randint(H-220, H-80), 4)
font = get_font(46, bold=True)
draw.text((W//2, H - 38), "Happy Ending", fill=(255, 220, 100, 255), font=font, anchor="mm")
save_img(img, "little_star_page7.png")

print("\n" + "="*50)
print("All 8 illustrations generated!")
print("="*50)
