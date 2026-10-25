"""Pixel-art sprites for HDBapocalypse residents and zombies.
Each sprite is drawn on a 16x24 grid, then outlined and scaled up."""
from PIL import Image, ImageDraw, ImageFont
import json, os, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else "out"
os.makedirs(OUT, exist_ok=True)
W, H = 16, 24
SCALE = 8

SKIN = ['#f5d0a9', '#e8b98a', '#d39a6a', '#a86b42', '#7a4a2a']
ZSKIN = '#9cc35a'
OUTLINE = (30, 26, 32, 255)


def hexc(c):
    c = c.lstrip('#')
    if len(c) == 3:
        c = ''.join(ch * 2 for ch in c)
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4)) + (255,)


def shade(c, f):
    r, g, b, a = hexc(c)
    return '#%02x%02x%02x' % tuple(max(0, min(255, int(v * f))) for v in (r, g, b))


class S:
    def __init__(self):
        self.g = [[None] * W for _ in range(H)]

    def p(self, x, y, c):
        if 0 <= x < W and 0 <= y < H and c:
            self.g[y][x] = c

    def r(self, x0, y0, x1, y1, c):
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                self.p(x, y, c)

    def image(self):
        im = Image.new('RGBA', (W + 2, H + 2), (0, 0, 0, 0))
        filled = {(x, y) for y in range(H) for x in range(W) if self.g[y][x]}
        for (x, y) in filled:
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                n = (x + dx, y + dy)
                if n not in filled:
                    im.putpixel((n[0] + 1, n[1] + 1), OUTLINE)
        for (x, y) in filled:
            im.putpixel((x + 1, y + 1), hexc(self.g[y][x]))
        return im


def body(d):
    """Draw the base figure. d: dict of options. Returns sprite and anchor info."""
    s = S()
    kid = d.get('kid')
    wide = d.get('wide', 0)
    skin = d['skin']
    top, bot = d['top'], d['bottom']
    shoes = d.get('shoes', '#3a3a44')
    # vertical layout
    th, lh = (4, 4) if kid else (6, 5)  # torso, leg heights
    head_y = 22 - lh - th - 1 - 7 - 1 + (1 if kid else 0)
    hy = head_y
    ty = hy + 8  # torso top (after neck)
    ly = ty + th  # legs top
    fy = ly + lh  # feet
    # legs
    bs = d.get('bottom_style', 'pants')
    for x0 in (5, 8):
        x1 = x0 + 2
        if bs == 'pants':
            s.r(x0, ly, x1, fy - 1, bot)
        elif bs == 'shorts':
            s.r(x0, ly, x1, ly + 1, bot)
            s.r(x0 + (1 if x0 == 5 else 0), ly + 2, x1 - (0 if x0 == 5 else 1), fy - 1, skin)
        elif bs == 'skirt':
            s.r(x0 + (1 if x0 == 5 else 0), ly, x1 - (0 if x0 == 5 else 1), fy - 1, skin)
    if bs == 'skirt':
        s.r(4, ly, 11, ly + 1, bot)
        s.r(5, ly + 2, 10, ly + 2, bot)
    s.r(7, ly + 1, 7, fy - 1, shade(bot, .78)) if bs == 'pants' else None
    # shoes
    s.r(4, fy, 7, fy, shoes)
    s.r(8, fy, 11, fy, shoes)
    # torso
    s.r(4 - wide, ty, 11 + wide, ly - 1, top)
    s.r(4 - wide, ly - 1, 11 + wide, ly - 1, shade(top, .8))
    # arms
    sl = d.get('sleeves', 'short')
    arms = d.get('arms', 'down')
    ax = (3 - wide, 12 + wide)
    if arms == 'down':
        for x in ax:
            s.r(x, ty, x, ly, skin)
            if sl == 'short':
                s.r(x, ty, x, ty + 1, top)
            elif sl == 'long':
                s.r(x, ty, x, ly - 1, top)
    else:  # zombie arms reaching out at shoulder height
        for side, x in ((-1, ax[0]), (1, ax[1])):
            s.p(x, ty, top if sl != 'none' else skin)
            for k in range(1, 4):
                s.p(x + side * k if False else x, ty, None)
            # forearms out front: draw raised arms going sideways
            s.r(min(x, x + side * 2), ty + 1, max(x, x + side * 2), ty + 1, skin)
            s.p(x + side * 2, ty, skin)
    # neck
    s.r(7, hy + 7, 8, hy + 7, shade(skin, .85))
    # head
    s.r(5, hy, 10, hy + 6, skin)
    s.r(5, hy + 6, 10, hy + 6, shade(skin, .92))
    eye = d.get('eye', '#1d1a22')
    s.p(6, hy + 3, eye)
    s.p(9, hy + 3, eye)
    if d.get('blush'):
        s.p(6, hy + 4, '#e79a8a'); s.p(9, hy + 4, '#e79a8a')
    if d.get('mouth', True):
        s.r(7, hy + 5, 8, hy + 5, shade(skin, .7))
    # hair
    hc = d.get('hair', '#2b1d14')
    st = d.get('hairstyle', 'short')
    if st in ('short', 'bun', 'ponytail', 'long', 'side'):
        s.r(6, hy - 1, 9, hy - 1, hc)
        s.r(5, hy, 10, hy, hc)
        s.p(5, hy + 1, hc); s.p(10, hy + 1, hc)
    if st == 'side':
        s.r(6, hy + 1, 8, hy + 1, hc)
    if st == 'bun':
        s.r(7, hy - 3, 8, hy - 2, hc)
    if st == 'ponytail':
        s.r(11, hy + 1, 11, hy + 4, hc)
    if st == 'long':
        s.r(4, hy + 1, 4, hy + 7, hc); s.r(11, hy + 1, 11, hy + 7, hc)
        s.r(5, hy + 2, 5, hy + 2, hc); s.p(10, hy + 2, hc)
    if st == 'perm':
        for x in range(5, 11):
            s.p(x, hy - 1, hc if x % 2 else shade(hc, 1.3))
        s.r(4, hy, 11, hy, hc)
        s.r(4, hy + 1, 4, hy + 4, hc); s.r(11, hy + 1, 11, hy + 4, hc)
        s.p(6, hy - 2, hc); s.p(8, hy - 2, hc)
    if st == 'spiky':
        s.p(5, hy - 2, hc); s.p(7, hy - 3, hc); s.p(9, hy - 2, hc); s.p(10, hy - 2, hc)
        s.r(5, hy - 1, 10, hy - 1, hc); s.r(5, hy, 10, hy, hc)
        s.p(5, hy + 1, hc); s.p(10, hy + 1, hc)
    if st == 'thin':
        s.p(5, hy, hc); s.p(10, hy, hc); s.p(5, hy + 1, hc); s.p(10, hy + 1, hc)
        s.p(7, hy - 1, hc); s.p(9, hy - 1, hc)
    if st == 'crop':
        s.r(5, hy, 10, hy, hc); s.r(6, hy - 1, 9, hy - 1, hc)
    return s, dict(hy=hy, ty=ty, ly=ly, fy=fy, wide=wide, skin=skin, arms=arms, shoes=shoes)


def lift(s, a, side):
    """Walk frame: raise one foot one pixel and swing the opposite hand up."""
    fy = a['fy']
    xs = range(4, 8) if side == 0 else range(8, 12)
    for x in xs:
        s.g[fy][x] = None
        if 5 <= x <= 10 or s.g[fy - 1][x] is None:
            s.p(x, fy - 1, a['shoes'])
    if a['arms'] == 'down':
        hx = 12 + a['wide'] if side == 0 else 3 - a['wide']
        if s.g[a['ly']][hx] == a['skin']:
            s.g[a['ly']][hx] = None


# ---------- accessories ----------
def glasses(s, a, c='#222'):
    hy = a['hy']
    s.r(5, hy + 3, 10, hy + 3, c)
    s.p(6, hy + 3, '#a8d8f0'); s.p(9, hy + 3, '#a8d8f0')


def shades(s, a):
    hy = a['hy']; s.r(5, hy + 3, 10, hy + 3, '#111'); s.p(7, hy + 3, '#444')


def cap(s, a, c, brim_right=True):
    hy = a['hy']
    s.r(5, hy - 2, 10, hy, c)
    s.r(6, hy - 3, 9, hy - 3, c)
    if brim_right:
        s.r(10, hy, 12, hy, shade(c, .7))
    else:
        s.r(5, hy + 1, 10, hy + 1, shade(c, .7))


def lanyard(s, a, c='#c0392b'):
    ty = a['ty']
    s.p(6, ty, c); s.p(9, ty, c); s.p(7, ty + 1, c); s.p(8, ty + 1, c)
    s.r(7, ty + 2, 8, ty + 3, '#f2f2f2')


def apron(s, a, c='#f2f0e6'):
    ty, ly = a['ty'], a['ly']
    s.r(5, ty + 1, 10, ly + 1, c)
    s.r(6, ty, 9, ty, c)


def vest(s, a, c, stripe='#e8e8e8'):
    ty, ly = a['ty'], a['ly']
    s.r(4, ty, 5, ly - 1, c); s.r(10, ty, 11, ly - 1, c)
    s.r(4, ty + 3, 11, ty + 3, stripe)


# ---------- the cast ----------
def spec_list():
    L = []

    def add(key, label, group, d, extra=None, note=''):
        L.append(dict(key=key, label=label, group=group, d=d, extra=extra, note=note))

    add('you', 'You (block leader)', 'resident',
        dict(skin=SKIN[2], hair='#151515', hairstyle='side', top='#2f6f73', sleeves='long', bottom='#3b3f4a'),
        lambda s, a: (s.r(3, a['ty'] + 1, 3, a['ty'] + 2, '#d9534f'), s.p(9, a['ty'] + 1, '#f2d14b')),
        'Teal jacket, red armband, star badge.')
    add('ahma', 'Grandma (Ah Ma)', 'resident',
        dict(skin=SKIN[0], hair='#d6d6d6', hairstyle='bun', top='#b5677d', sleeves='short', bottom='#4a4e69', shoes='#7a5c45'),
        lambda s, a: [s.p(x, a['ty'] + y, '#f3c6d3') for x, y in ((5, 1), (8, 2), (10, 4), (6, 4), (9, 0))],
        'Grey bun, floral blouse, slippers.')
    add('ahgong', 'Grandpa (Ah Gong)', 'resident',
        dict(skin=SKIN[1], hair='#d6d6d6', hairstyle='thin', top='#f4f4ee', sleeves='none', bottom='#5d6b7a', bottom_style='shorts', shoes='#2f6fb5'),
        lambda s, a: glasses(s, a, '#555'),
        'White singlet, shorts, blue slippers.')
    add('tinker', 'Retired technician', 'resident',
        dict(skin=SKIN[3], hair='#9a9a9a', hairstyle='crop', top='#6b7d5c', sleeves='short', bottom='#4b4b52'),
        lambda s, a: (cap(s, a, '#3d5a80'), glasses(s, a), s.r(4, a['ly'] - 1, 11, a['ly'] - 1, '#7a5230'), s.p(5, a['ly'] - 1, '#c9c9c9'), s.p(10, a['ly'] - 1, '#e3a92b')),
        'Cap, glasses, tool belt. Inventor.')
    add('polystu', 'Poly engineering student', 'resident',
        dict(skin=SKIN[1], hair='#2b1d14', hairstyle='side', top='#5c6f8f', sleeves='long', bottom='#2e3440', shoes='#f2f2f2'),
        lambda s, a: (s.r(5, a['hy'] - 1, 10, a['hy'] - 1, '#5c6f8f'), s.p(4, a['hy'] + 3, '#f2f2f2'), s.p(11, a['hy'] + 3, '#f2f2f2'), s.r(7, a['ty'] + 2, 8, a['ty'] + 2, '#e3a92b')),
        'Hoodie, earbuds, white sneakers. Inventor.')
    add('nsman', 'NSman', 'resident',
        dict(skin=SKIN[2], hair='#151515', hairstyle='crop', top='#55613f', sleeves='long', bottom='#55613f', shoes='#1d1d1d'),
        lambda s, a: (cap(s, a, '#4a5535'), [s.p(x, a['ty'] + y, '#3f4a2e') for x, y in ((5, 1), (9, 2), (7, 4), (10, 0))], [s.p(x, a['ly'] + y, '#3f4a2e') for x, y in ((6, 1), (9, 3))]),
        'Camo uniform and jockey cap.')
    add('nsf', 'NSF on book-out', 'resident',
        dict(skin=SKIN[1], hair='#151515', hairstyle='crop', top='#55613f', sleeves='short', bottom='#55613f', shoes='#1d1d1d'),
        lambda s, a: (s.r(5, a['hy'] - 2, 10, a['hy'], '#7a1f2b'), s.r(4, a['hy'] - 1, 5, a['hy'], '#7a1f2b'), s.p(9, a['hy'] - 1, '#e3c14b'), s.r(10, a['ty'] + 1, 12, a['ly'] + 1, '#2f3a24')),
        'Beret, uniform, duffel bag.')
    add('helper', 'Domestic helper', 'resident',
        dict(skin=SKIN[3], hair='#151515', hairstyle='ponytail', top='#8e7cc3', sleeves='short', bottom='#2e3440'),
        lambda s, a: (apron(s, a, '#f6efe0'), s.r(12, a['ly'] - 1, 14, a['ly'] + 1, '#d9b36c'), s.r(12, a['ly'] - 1, 14, a['ly'] - 1, '#b8904b')),
        'Ponytail, apron, laundry basket.')
    add('nurse', 'Nurse', 'resident',
        dict(skin=SKIN[1], hair='#151515', hairstyle='bun', top='#9fd3df', sleeves='short', bottom='#9fd3df', shoes='#f2f2f2'),
        lambda s, a: (s.r(6, a['ty'], 6, a['ty'] + 3, '#33415c'), s.r(9, a['ty'], 9, a['ty'] + 3, '#33415c'), s.p(7, a['ty'] + 3, '#c0c4cc'), s.p(8, a['ty'] + 3, '#c0c4cc'), s.r(5, a['hy'] + 4, 10, a['hy'] + 5, '#cfe7ee')),
        'Scrubs, stethoscope, face mask.')
    add('driver', 'Ride-hail driver', 'resident',
        dict(skin=SKIN[2], hair='#151515', hairstyle='short', top='#2e9a8a', sleeves='short', bottom='#3b3f4a'),
        lambda s, a: (s.r(5, a['hy'] - 1, 10, a['hy'] - 1, '#111'), s.p(6, a['hy'] - 1, '#555'), s.p(9, a['hy'] - 1, '#555'), s.p(7, a['ty'], '#f2f2f2'), s.p(8, a['ty'], '#f2f2f2'), s.r(12, a['ly'] - 1, 12, a['ly'], '#222'), s.p(12, a['ly'] - 2, '#4aa3df')),
        'Polo shirt, shades on head, phone.')
    add('hawker', 'Kopitiam uncle', 'resident',
        dict(skin=SKIN[2], hair='#2b1d14', hairstyle='thin', top='#f4f4ee', sleeves='none', bottom='#3b3f4a', bottom_style='shorts', shoes='#c0392b', wide=0),
        lambda s, a: (s.r(10, a['ty'], 12, a['ty'] + 3, '#e8d9b0'), s.r(12, a['ly'] - 2, 13, a['ly'] - 1, '#9aa0a6'), s.p(14, a['ly'] - 2, '#9aa0a6')),
        'Singlet, towel on shoulder, ladle.')
    add('cleaner', 'Town council cleaner', 'resident',
        dict(skin=SKIN[3], hair='#3b2a20', hairstyle='short', top='#5c9ea0', sleeves='long', bottom='#3b3f4a', shoes='#1d1d1d'),
        lambda s, a: (cap(s, a, '#e2b23a', brim_right=False), vest(s, a, '#ff8c1a', '#f2f2f2'), s.r(13, a['ty'] - 3, 13, a['fy'] - 1, '#a0784e'), s.r(12, a['fy'] - 2, 14, a['fy'], '#d8c27a')),
        'Bucket hat, hi-vis vest, broom.')
    add('rcauntie', 'RC auntie', 'resident',
        dict(skin=SKIN[0], hair='#3b2a20', hairstyle='perm', top='#c0392b', sleeves='short', bottom='#33415c', shoes='#7a5c45'),
        lambda s, a: (lanyard(s, a, '#2f3a9b'), s.r(12, a['ty'] + 2, 14, a['ly'], '#c8a46a'), s.r(12, a['ty'] + 2, 14, a['ty'] + 2, '#555'), s.p(13, a['ty'] + 4, '#f2f2f2')),
        'Permed hair, polo, lanyard, clipboard.')
    add('student', 'Sec school student', 'resident',
        dict(skin=SKIN[1], hair='#151515', hairstyle='short', top='#f4f4ee', sleeves='short', bottom='#3a4a6b', bottom_style='shorts', shoes='#f2f2f2'),
        lambda s, a: (s.r(2, a['ty'], 3, a['ly'], '#c0392b'), s.r(12, a['ty'], 13, a['ly'], '#c0392b'), s.p(4, a['ty'], '#c0392b'), s.p(11, a['ty'], '#c0392b'), s.p(5, a['ty'] + 1, '#3a4a6b')),
        'School uniform, backpack.')
    add('kid', 'Primary school kid', 'resident',
        dict(skin=SKIN[0], hair='#2b1d14', hairstyle='short', top='#f2d14b', sleeves='short', bottom='#3a6ea5', bottom_style='shorts', kid=True, blush=True, shoes='#f2f2f2'),
        lambda s, a: (s.r(12, a['ty'] + 1, 13, a['ty'] + 3, '#c8915a'), s.p(12, a['ty'] + 0, '#c8915a'), s.p(13, a['ty'], '#c8915a')),
        'Yellow tee, shorts, teddy bear.')
    add('pmet', 'Office worker', 'resident',
        dict(skin=SKIN[1], hair='#151515', hairstyle='side', top='#a9c6e8', sleeves='long', bottom='#2e3440', shoes='#1d1d1d'),
        lambda s, a: (s.r(7, a['ty'], 8, a['ty'] + 4, '#33415c'), s.r(12, a['ly'] - 1, 14, a['ly'] + 1, '#3d2b1f'), lanyard(s, a, '#4a90d9') if False else None),
        'Shirt and tie, briefcase.')
    add('karang', 'Karang guni man', 'resident',
        dict(skin=SKIN[3], hair='#9a9a9a', hairstyle='thin', top='#8a6a4a', sleeves='short', bottom='#4b4b52', shoes='#2f6fb5'),
        lambda s, a: (cap(s, a, '#c06d3a'), s.r(11, a['ty'] - 1, 14, a['ly'] + 1, '#d9c8a0'), s.r(11, a['ty'] - 1, 14, a['ty'] - 1, '#b8a476'), s.p(13, a['ty'] + 2, '#b8a476')),
        'Cap, sack of scrap over shoulder.')
    add('ahbeng', 'Ah Beng', 'resident',
        dict(skin=SKIN[2], hair='#c26a2b', hairstyle='spiky', top='#1d1d1d', sleeves='none', bottom='#3b4c7a', shoes='#f2f2f2'),
        lambda s, a: (shades(s, a), s.r(6, a['ty'], 9, a['ty'], '#e3c14b'), s.p(4, a['ty'] + 2, '#3b6ea5'), s.p(3, a['ty'] + 3, '#3b6ea5')),
        'Dyed spiky hair, shades, gold chain, tattoo.')
    add('teacher', 'Teacher', 'resident',
        dict(skin=SKIN[3], hair='#151515', hairstyle='long', top='#7aa37a', sleeves='long', bottom='#4a4e69', bottom_style='skirt', shoes='#3d2b1f'),
        lambda s, a: (glasses(s, a), s.r(12, a['ty'] + 2, 14, a['ty'] + 5, '#b5677d'), s.r(12, a['ty'] + 4, 14, a['ty'] + 4, '#f2f2f2')),
        'Cardigan, glasses, stack of books.')
    add('worker', 'Construction worker', 'resident',
        dict(skin=SKIN[4], hair='#151515', hairstyle='crop', top='#6c8ebf', sleeves='long', bottom='#3a4a6b', shoes='#7a5230'),
        lambda s, a: (s.r(5, a['hy'] - 2, 10, a['hy'], '#f2c12e'), s.r(4, a['hy'], 11, a['hy'], '#d9a91f'), vest(s, a, '#ff8c1a', '#f2f2f2'), s.r(13, a['ty'], 13, a['ly'] + 1, '#8a8f98')),
        'Hard hat, hi-vis vest, steel pipe.')
    # zombies
    add('z_shuffler', 'Uncle shuffler', 'zombie',
        dict(skin=ZSKIN, hair='#d6d6d6', hairstyle='thin', top='#d8d8c8', sleeves='none', bottom='#5d6b7a', bottom_style='shorts', arms='out', eye='#c0392b', mouth=False, shoes='#2f6fb5'),
        lambda s, a: (s.p(6, a['ty'] + 2, '#8b2e2e'), s.p(9, a['ty'] + 4, '#8b2e2e'), s.r(7, a['hy'] + 5, 8, a['hy'] + 5, '#3b1d1d'), s.p(11, a['ly'] - 2, None)),
        'Slow. Torn singlet, one slipper.')
    add('z_runner', 'PMD runner', 'zombie',
        dict(skin=ZSKIN, hair='#151515', hairstyle='short', top='#3b6ea5', sleeves='short', bottom='#2e3440', arms='out', eye='#c0392b', mouth=False),
        lambda s, a: (s.r(5, a['hy'] - 2, 10, a['hy'], '#e2e2e2'), s.r(5, a['hy'] - 2, 10, a['hy'] - 2, '#4a90d9'), s.r(3, a['fy'] + 1, 12, a['fy'] + 1, '#333'), s.p(3, a['fy'], '#333'), s.p(12, a['fy'], '#333'), s.r(7, a['hy'] + 5, 8, a['hy'] + 5, '#3b1d1d')),
        'Fast. Helmet, scooter deck.')
    add('z_bloated', 'Bloated (wet market)', 'zombie',
        dict(skin='#8fb35a', hair='#3b2a20', hairstyle='thin', top='#cfd6c4', sleeves='none', bottom='#4b4b52', bottom_style='shorts', arms='out', wide=2, eye='#c0392b', mouth=False, shoes='#1d1d1d'),
        lambda s, a: (apron(s, a, '#e6e8e0'), s.p(6, a['ty'] + 3, '#6a8a3a'), s.p(9, a['ty'] + 2, '#6a8a3a'), s.p(8, a['ty'] + 5, '#8b2e2e'), s.r(7, a['hy'] + 5, 8, a['hy'] + 5, '#3b1d1d')),
        'Swollen, rubber apron. Bursts.')
    add('z_ahlong', 'Ah Long', 'zombie',
        dict(skin=ZSKIN, hair='#151515', hairstyle='side', top='#7a1f2b', sleeves='short', bottom='#1d1d1d', arms='out', eye='#c0392b', mouth=False, shoes='#1d1d1d'),
        lambda s, a: (s.r(6, a['ty'], 9, a['ty'], '#e3c14b'), s.p(7, a['ty'] + 1, '#e3c14b'), shades(s, a), s.r(7, a['hy'] + 5, 8, a['hy'] + 5, '#3b1d1d')),
        'Debt collector. Bangs on doors.')
    add('z_riot', 'Riot-gear zombie', 'zombie',
        dict(skin=ZSKIN, hair='#151515', hairstyle='crop', top='#26324a', sleeves='long', bottom='#26324a', arms='down', eye='#c0392b', mouth=False, shoes='#111'),
        lambda s, a: (s.r(4, a['hy'] - 2, 11, a['hy'] + 1, '#26324a'), s.r(5, a['hy'] + 2, 10, a['hy'] + 4, '#9fb4c8'), s.p(6, a['hy'] + 3, '#c0392b'), s.p(9, a['hy'] + 3, '#c0392b'), s.r(0, a['ty'] - 1, 3, a['ly'] + 3, '#7f95ad'), s.r(1, a['ty'], 2, a['ly'] + 2, '#a6bacd')),
        'Tough. Helmet and riot shield.')
    return L


def main():
    cast = spec_list()
    meta = []
    big = []
    for c in cast:
        s, a = body(c['d'])
        if c['extra']:
            c['extra'](s, a)
        im = s.image()
        im.save(os.path.join(OUT, c['key'] + '_1x.png'))
        b = im.resize((im.width * SCALE, im.height * SCALE), Image.NEAREST)
        b.save(os.path.join(OUT, c['key'] + '.png'))
        big.append((c, b))
        meta.append(dict(key=c['key'], label=c['label'], group=c['group'], note=c['note']))
    # animation atlas: rows = residents, infected residents, zombies; cols = idle, step L, idle, step R
    rows = [(c, False) for c in cast if c['group'] == 'resident'] + \
           [(c, True) for c in cast if c['group'] == 'resident'] + \
           [(c, False) for c in cast if c['group'] == 'zombie']
    CW, CH = W + 2, H + 2
    atlas = Image.new('RGBA', (CW * 4, CH * len(rows)), (0, 0, 0, 0))
    index = []
    for ri, (c, inf) in enumerate(rows):
        d = dict(c['d'])
        if inf:
            d['skin'] = ZSKIN
        for fi, step in enumerate((None, 0, None, 1)):
            sp, an = body(d)
            if c['extra']:
                c['extra'](sp, an)
            if step is not None:
                lift(sp, an, step)
            atlas.alpha_composite(sp.image(), (fi * CW, ri * CH))
        index.append(('inf_' if inf else '') + c['key'])
    atlas.save(os.path.join(OUT, 'atlas.png'), optimize=True)
    json.dump(index, open(os.path.join(OUT, 'atlas.json'), 'w'))
    # preview of the walk frames, scaled up
    atlas.resize((atlas.width * 4, atlas.height * 4), Image.NEAREST).save(os.path.join(OUT, 'atlas_preview.png'))
    # labelled sheet
    cols = 5
    cw, ch = big[0][1].width + 90, big[0][1].height + 50
    rows = (len(big) + cols - 1) // cols
    sheet = Image.new('RGBA', (cols * cw, rows * ch), (243, 239, 230, 255))
    dr = ImageDraw.Draw(sheet)
    try:
        f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 15)
    except Exception:
        f = ImageFont.load_default()
    for i, (c, b) in enumerate(big):
        x, y = (i % cols) * cw, (i // cols) * ch
        if c['group'] == 'zombie':
            dr.rectangle([x + 4, y + 4, x + cw - 4, y + ch - 4], fill=(225, 232, 214, 255))
        sheet.alpha_composite(b, (x + 45, y + 8))
        tw = dr.textlength(c['label'], font=f)
        dr.text((x + (cw - tw) / 2, y + ch - 36), c['label'], fill=(40, 36, 44), font=f)
    sheet.save(os.path.join(OUT, 'hdbapocalypse_sprite_sheet.png'))
    # game-ready strip (1x, no labels) in cast order
    strip = Image.new('RGBA', ((W + 2) * len(cast), H + 2), (0, 0, 0, 0))
    for i, c in enumerate(cast):
        strip.alpha_composite(Image.open(os.path.join(OUT, c['key'] + '_1x.png')), (i * (W + 2), 0))
    strip.save(os.path.join(OUT, 'sprites_strip_1x.png'))
    json.dump(meta, open(os.path.join(OUT, 'sprites.json'), 'w'), indent=1)
    print('ok', len(cast))


main()
