#!/usr/bin/env python3
"""Generate now.gg games portal site."""
import os
import json

BASE = "/Users/noahgardner/Documents/GitHub/Ngardner29"
SITE_NAME = "DaGoatGames"
SITE_DOMAIN = "dagoatgames.com"

# Games database: (slug, title, nowgg_path, category, icon_id, icon_slug, rating)
# icon URL pattern: https://cdn.now.gg/apps-content/{icon_id}/icon/{icon_slug}.png
GAMES = [
    # Action
    ("ace-defender", "Ace Defender", "/apps/juefeng-games/9152/ace-defender.html", "Action", "9152", "ace-defender", "4.6"),
    ("counter-attack", "Counter Attack", "/apps/plug-in-digital/8258/counter-attack.html", "Action", "8258", "counter-attack", "3.9"),
    ("gangs-wars-pixel-shooter-rp", "Gangs Wars: Pixel Shooter RP", "/apps/playducky-com/8827/gangs-wars-pixel-shooter-rp.html", "Action", "8827", "gangs-wars-pixel-shooter-rp", "4.1"),
    ("rumble-club", "Rumble Club", "/apps/lightfox-games-inc/8697/rumble-club.html", "Action", "8697", "rumble-club", "4.1"),
    ("blox-fruit", "Blox Fruit", "/apps/Blox-fruit/19901/Blox-fruit.html", "Action", "19901", "b", "4.5"),
    ("80-anime-vanguards", "80 Anime Vanguards", "/apps/80-anime-vanguards/19908/80-anime-vanguards.html", "Action", "19908", "80-anime-vanguards", "4.5"),
    ("battle-through-the-heavens", "Battle Through the Heavens", "/apps/juefeng-games/9089/battle-through-the-heavens.html", "Action", "9089", "battle-through-the-heavens", "4.4"),
    ("bullet-echo", "Bullet Echo", "/apps/zeptolab/8700/bullet-echo.html", "Action", "8700", "bullet-echo", "4.3"),
    ("krunker", "Krunker", "/apps/krunker/51300/krunker.html", "Action", "51300", "krunker", "4.2"),
    ("super-sus", "Super Sus", "/apps/super-sus/8750/super-sus.html", "Action", "8750", "super-sus", "4.3"),
    # Casual
    ("impostor-rescue", "Impostor Rescue", "/apps/mobaso/8840/impostor-rescue.html", "Casual", "8840", "impostor-rescue", "4.5"),
    ("comfy-girl", "Comfy Girl", "/apps/plug-in-digital/8730/comfy-girl.html", "Casual", "8730", "comfy-girl", "4.2"),
    ("paws-go", "Paws Go!", "/apps/sofish-games/8826/paws-go.html", "Casual", "8826", "paws-go", "4.0"),
    ("gacha-life-2", "Gacha Life 2", "/apps/lunime/5691/gacha-life-2.html", "Casual", "5691", "gacha-life-2", "4.4"),
    ("gacha-club", "Gacha Club", "/apps/lunime/2132/gacha-club.html", "Casual", "2132", "gacha-club", "4.4"),
    ("gacha-life", "Gacha Life", "/apps/lunime/5767/gacha-life.html", "Casual", "5767", "gacha-life", "4.3"),
    ("animal-run", "Animal Run!", "/apps/animal-run/8760/animal-run.html", "Casual", "8760", "animal-run", "4.1"),
    ("couple-flip", "Couple Flip", "/apps/couple-flip/8770/couple-flip.html", "Casual", "8770", "couple-flip", "4.0"),
    ("draw-the-rest", "Draw the Rest", "/apps/draw-the-rest/8780/draw-the-rest.html", "Casual", "8780", "draw-the-rest", "4.0"),
    # Simulation
    ("cat-from-hell-cat-simulator", "Cat From Hell - Cat Simulator", "/apps/nolodin/10613/cat-from-hell-cat-simulator.html", "Simulation", "10613", "cat-from-hell-cat-simulator", "4.4"),
    ("adopt-me", "Adopt Me", "/apps/adopt-me/19912/adopt-me.html", "Simulation", "19912", "adopt-me", "4.5"),
    ("brookhaven", "Brookhaven", "/apps/Brookhaven/19905/Brookhaven.html", "Simulation", "19905", "Brookhaven", "4.5"),
    ("grow-a-garden", "Grow a Garden", "/apps/Grow-a-Garden/19903/Grow-a-Garden.html", "Simulation", "19903", "Grow-a-Garden", "4.5"),
    ("idle-prison-empire-tycoon", "Idle Prison Empire Tycoon", "/apps/wazzapps-global-limited/8695/idle-prison-empire-tycoon.html", "Simulation", "8695", "idle-prison-empire-tycoon", "4.7"),
    ("roller-coaster-life-theme-park", "Roller Coaster Life Theme Park", "/apps/sparkling-society-park-building-island-v/8698/roller-coaster-life-theme-park.html", "Simulation", "8698", "roller-coaster-life-theme-park", "4.4"),
    ("dragon-city-mobile", "Dragon City Mobile", "/apps/dragon-city/8790/dragon-city-mobile.html", "Simulation", "8790", "dragon-city-mobile", "4.3"),
    ("my-talking-tom-2", "My Talking Tom 2", "/apps/outfit7/8800/my-talking-tom-2.html", "Simulation", "8800", "my-talking-tom-2", "4.2"),
    ("my-talking-angela-2", "My Talking Angela 2", "/apps/outfit7/8810/my-talking-angela-2.html", "Simulation", "8810", "my-talking-angela-2", "4.2"),
    # Racing
    ("indian-bikes-driving-3d", "Indian Bikes Driving 3D", "/apps/rohit-gaming-studio/8822/indian-bikes-driving-3d.html", "Racing", "8822", "indian-bikes-driving-3d", "4.1"),
    ("mr-racer-car-racing", "MR RACER - Car Racing", "/apps/chennaigames-studio-private-limited/51921/mr-racer-car-racing.html", "Racing", "51921", "mr-racer-car-racing", "4.1"),
    ("smash-karts", "Smash Karts", "/apps/tall-team/51304/smash-karts.html", "Racing", "51304", "smash-karts", "4.2"),
    ("hill-climb-racing-2", "Hill Climb Racing 2", "/apps/fingersoft/8830/hill-climb-racing-2.html", "Racing", "8830", "hill-climb-racing-2", "4.4"),
    ("happy-wheels", "Happy Wheels", "/apps/happy-wheels/51310/happy-wheels.html", "Racing", "51310", "happy-wheels", "4.3"),
    ("racing-smash-3d", "Racing Smash 3D", "/apps/racing-smash/8835/racing-smash-3d.html", "Racing", "8835", "racing-smash-3d", "4.0"),
    ("hot-wheels-unlimited", "Hot Wheels Unlimited", "/apps/hot-wheels/8840/hot-wheels-unlimited.html", "Racing", "8840", "hot-wheels-unlimited", "4.1"),
    # Puzzle
    ("polybuzz", "PolyBuzz", "/apps/cloud-whale-interactive-technology-llc/10386/polybuzz.html", "Puzzle", "10386", "polybuzz", "4.2"),
    ("ink-game", "Ink Game", "/apps/ink-game/19906/ink-game.html", "Puzzle", "19906", "ink-game", "4.5"),
    ("escape-lockdown", "Escape Lockdown", "/apps/spatial-io/51907/escape-lockdown.html", "Puzzle", "51907", "escape-lockdown", "4.5"),
    ("paranormal-inc", "Paranormal Inc.", "/apps/plug-in-digital/8264/paranormal-inc.html", "Puzzle", "8264", "paranormal-inc", "4.5"),
    ("kitten-match", "Kitten Match", "/apps/kitten-match/8850/kitten-match.html", "Puzzle", "8850", "kitten-match", "4.1"),
    ("house-painter", "House Painter", "/apps/house-painter/8855/house-painter.html", "Puzzle", "8855", "house-painter", "4.0"),
    ("sudoku", "Sudoku.com", "/apps/sudoku/8860/sudoku.html", "Puzzle", "8860", "sudoku", "4.2"),
    # Strategy
    ("war-master", "War Master", "/apps/nese-dijital/8692/war-master.html", "Strategy", "8692", "war-master", "4.2"),
    ("army-tycoon-idle-base", "Army Tycoon: Idle Base", "/apps/hello-games-team/8688/army-tycoon-idle-base.html", "Strategy", "8688", "army-tycoon-idle-base", "4.6"),
    ("state-of-survival", "State of Survival", "/apps/state-of-survival/8870/state-of-survival.html", "Strategy", "8870", "state-of-survival", "4.3"),
    ("lords-mobile", "Lords Mobile", "/apps/lords-mobile/8875/lords-mobile.html", "Strategy", "8875", "lords-mobile", "4.2"),
    ("rush-royale", "Rush Royale", "/apps/rush-royale/8880/rush-royale.html", "Strategy", "8880", "rush-royale", "4.3"),
    ("clash-royale", "Clash Royale", "/apps/supercell/8885/clash-royale.html", "Strategy", "8885", "clash-royale", "4.5"),
    # Adventure
    ("99-nights", "99 Nights in the Forest", "/apps/99-Nights/19902/99-Nights.html", "Adventure", "19902", "99-Nights", "4.5"),
    ("poppy-playtime", "Poppy Playtime", "/apps/mob-games-studio/1293/poppy-playtime.html", "Adventure", "1293", "poppy-playtime", "4.4"),
    ("dynamons-7", "Dynamons 7", "/apps/azerion-casual-games/51917/dynamons-7.html", "Adventure", "51917", "dynamons-7", "4.3"),
    ("roblox", "Roblox", "/apps/roblox/19900/roblox.html", "Adventure", "19900", "roblox", "4.6"),
    ("granny", "Granny", "/apps/granny/8890/granny.html", "Adventure", "8890", "granny", "4.2"),
    ("granny-3", "Granny 3", "/apps/granny-3/8895/granny-3.html", "Adventure", "8895", "granny-3", "4.1"),
    ("evil-nun", "Evil Nun", "/apps/evil-nun/8900/evil-nun.html", "Adventure", "8900", "evil-nun", "4.2"),
    # Sports
    ("upd-volleyball-legend", "UPD Volleyball Legend", "/apps/upd-volleyball-legen/19915/upd-volleyball-legen.html", "Sports", "19915", "upd-volleyball-legen", "4.5"),
    ("nba-live-mobile-basketball", "NBA LIVE Mobile Basketball", "/apps/electronic-arts/2156/nba-live-mobile-basketball.html", "Sports", "2156", "nba-live-mobile-basketball", "4.3"),
    ("retro-bowl", "Retro Bowl", "/apps/retro-bowl/51320/retro-bowl.html", "Sports", "51320", "retro-bowl", "4.5"),
    ("rocket-league-sideswipe", "Rocket League Sideswipe", "/apps/rocket-league/8910/rocket-league-sideswipe.html", "Sports", "8910", "rocket-league-sideswipe", "4.4"),
    ("golf-clash", "Golf Clash", "/apps/golf-clash/8915/golf-clash.html", "Sports", "8915", "golf-clash", "4.2"),
    ("real-cricket-20", "Real Cricket 20", "/apps/real-cricket/8920/real-cricket-20.html", "Sports", "8920", "real-cricket-20", "4.1"),
    # Arcade
    ("bloxd-io", "bloxd.io", "/apps/bloxd/51240/bloxd-io.html", "Arcade", "51240", "bloxd-io", "4.2"),
    ("solitaire-social", "Solitaire Social", "/apps/kosmos-games/51904/solitaire-social.html", "Arcade", "51904", "solitaire-social", "4.5"),
    ("subway-surfers", "Subway Surfers", "/apps/subway-surfers/51330/subway-surfers.html", "Arcade", "51330", "subway-surfers", "4.5"),
    ("red-ball-4", "Red Ball 4", "/apps/red-ball/8930/red-ball-4.html", "Arcade", "8930", "red-ball-4", "4.3"),
    ("geometry-dash-lite", "Geometry Dash Lite", "/apps/geometry-dash/8935/geometry-dash-lite.html", "Arcade", "8935", "geometry-dash-lite", "4.4"),
    ("my-singing-monsters", "My Singing Monsters", "/apps/my-singing-monsters/8940/my-singing-monsters.html", "Arcade", "8940", "my-singing-monsters", "4.3"),
    # Multiplayer
    ("among-us", "Among Us", "/apps/innersloth-llc/4047/among-us.html", "Multiplayer", "4047", "among-us", "4.5"),
    ("bedwars", "BedWars", "/apps/bedwars/19910/bedwars.html", "Multiplayer", "19910", "bedwars", "4.4"),
    ("murder-mystery-2", "Murder Mystery 2", "/apps/murder-mystery-2/19911/murder-mystery-2.html", "Multiplayer", "19911", "murder-mystery-2", "4.3"),
    ("world-of-tanks-blitz", "World of Tanks Blitz", "/apps/wargaming/8950/world-of-tanks-blitz.html", "Multiplayer", "8950", "world-of-tanks-blitz", "4.3"),
    # RPG
    ("soul-land-reloaded", "Soul Land Reloaded", "/apps/new-times-game/4075/soul-land.html", "RPG", "4075", "soul-land", "4.3"),
    ("mu-origin-3", "MU Origin 3", "/apps/fingerfun/5581/mu-origin.html", "RPG", "5581", "mu-origin", "4.2"),
    ("dragon-raja", "Dragon Raja", "/apps/dragon-raja/8960/dragon-raja.html", "RPG", "8960", "dragon-raja", "4.1"),
    ("ez-knight", "EZ Knight", "/apps/ez-knight/8965/ez-knight.html", "RPG", "8965", "ez-knight", "4.0"),
]

CATEGORIES = sorted(set(g[3] for g in GAMES))

def icon_url(icon_id, icon_slug):
    return f"https://cdn.now.gg/apps-content/{icon_id}/icon/{icon_slug}.png"

def nowgg_url(path):
    return f"https://now.gg{path}"

def nav_html(prefix=""):
    cats_main = CATEGORIES[:6]
    cats_more = CATEGORIES[6:]
    nav = ""
    for c in cats_main:
        nav += f'            <li class="nav-item"><a class="nav-link" href="{prefix}/category/{c.lower()}.html">{c}</a></li>\n'
    if cats_more:
        nav += '            <li class="nav-item dropdown"><a class="nav-link dropdown-toggle" href="#" data-bs-toggle="dropdown">More</a>\n'
        nav += '              <ul role="menu" class="dropdown-menu">\n'
        for c in cats_more:
            nav += f'                <li><a class="dropdown-item" href="{prefix}/category/{c.lower()}.html">{c}</a></li>\n'
        nav += '              </ul>\n            </li>\n'
    return nav

def game_card_grid2(g, prefix=""):
    slug, title, _, cat, icon_id, icon_slug, _ = g
    img = icon_url(icon_id, icon_slug)
    return f'''  <div class="col-lg-4 col-md-6 grid-2">
    <a href="{prefix}/play/{slug}.html">
    <div class="game-item">
      <div class="list-game">
        <div class="list-thumbnail"><img src="{img}" class="small-thumb img-rounded lazyload" alt="{title}"></div>
        <div class="list-info">
          <div class="list-title">{title}</div>
          <div class="list-category">{cat}</div>
        </div>
      </div>
    </div>
    </a>
  </div>
'''

def game_card_grid3(g, prefix=""):
    slug, title, _, cat, icon_id, icon_slug, _ = g
    img = icon_url(icon_id, icon_slug)
    return f'''<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="{prefix}/play/{slug}.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="{img}" class="small-thumb img-rounded lazyload" alt="{title}"></div>
      <div class="list-info">
        <div class="list-title">{title}</div>
      </div>
    </div>
  </div>
  </a>
</div>
'''

def page_head(title, desc, prefix="", og_image=""):
    return f'''<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
    <title>{title} - {SITE_DOMAIN}</title>
    <meta name="description" content="{desc}">
    <link rel="icon" href="{prefix}/images/favicon.png" sizes="32x32">
    <meta property="og:url" content="https://{SITE_DOMAIN}" />
    <meta property="og:title" content="{title}" />
    <meta property="og:site_name" content="{SITE_NAME}" />
    <meta property="og:description" content="{desc}" />
    <meta property="og:type" content="website" />
    {f'<meta property="og:image" content="{og_image}">' if og_image else ''}
    <link rel="stylesheet" type="text/css" href="{prefix}/css/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="{prefix}/css/style.css" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.3/font/bootstrap-icons.css" />
    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
</head>
'''

def page_nav(prefix=""):
    return f'''<body id="page-top" style="background: url('{prefix}/images/background1.png'); background-size: cover;">
    <nav class="navbar navbar-expand-lg navbar-dark top-nav" id="mainNav">
        <div class="container">
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#nav-menu" aria-controls="nav-menu" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <a class="navbar-brand js-scroll-trigger" href="/">
                <strong>{SITE_NAME}</strong>
            </a>
            <div class="navbar-collapse collapse" id="nav-menu">
            </div>
            <div class="d-none d-lg-block">
        <ul class="navbar-nav">
{nav_html(prefix)}
          </ul>
            </div>
        </div>
    </nav>
'''

def page_footer(prefix=""):
    return f'''
    <footer class="footer border-line">
        <div class="container">
            <div class="row">
                <div class="col-md-6">
                    <p>&copy; 2024 {SITE_NAME}. All rights reserved.</p>
                </div>
                <div class="col-md-6 text-end">
                    <a href="{prefix}/policy.html" class="text-white me-3">Privacy Policy</a>
                    <a href="{prefix}/term.html" class="text-white me-3">Terms</a>
                    <a href="{prefix}/dmca.html" class="text-white">DMCA</a>
                </div>
            </div>
        </div>
    </footer>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
    <script src="{prefix}/js/script.js"></script>
</body>
</html>'''

# ========== GENERATE INDEX.HTML ==========
def generate_index():
    desc = f"Play your favorite mobile games online for free on {SITE_NAME}. No downloads required - instant cloud gaming powered by now.gg!"
    html = page_head(f"{SITE_NAME} - Play Free Online Games", desc)
    html += page_nav()

    # Featured game
    html += '''
<div class="container game-wrapper">
  <div class="row">
    <div class="col-md-12">
        <div class="header-area" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
            <h1 class="masthead-title">Play Mobile Games Online - Free!</h1>
            <div class="masthead-description">
                <h3>No downloads required. Instant cloud gaming powered by now.gg. Play your favorite Android games directly in your browser!</h3>
            </div>
        </div>
    </div>
  </div>
</div>
'''

    # Popular games section
    html += '<div class="container">\n'
    html += '    <h3 class="section-title">Popular Games</h3>\n'
    html += '    <div class="row grid-container">\n'
    popular = GAMES[:12]
    for g in popular:
        html += game_card_grid2(g)
    html += '    </div>\n'

    # All games section
    html += '    <h3 class="section-title">All Games</h3>\n'
    html += '    <div class="row grid-container">\n'
    for g in GAMES:
        html += game_card_grid3(g)
    html += '    </div>\n'

    # Categories list
    html += '    <h3 class="section-title">Categories</h3>\n'
    html += '    <ul class="category-list-wrapper">\n'
    for cat in CATEGORIES:
        count = sum(1 for g in GAMES if g[3] == cat)
        html += f'        <li class="cat-item"><a href="/category/{cat.lower()}.html"><span class="cat-name">{cat}</span> <span class="cat-game-amount">({count})</span></a></li>\n'
    html += '    </ul>\n'
    html += '</div>\n'
    html += page_footer()

    with open(os.path.join(BASE, "index.html"), "w") as f:
        f.write(html)
    print("Generated index.html")

# ========== GENERATE PLAY PAGES ==========
def generate_play_pages():
    for g in GAMES:
        slug, title, nowgg_path, cat, icon_id, icon_slug, rating = g
        desc = f"Play {title} online for free on {SITE_DOMAIN}. No downloads required - instant cloud gaming powered by now.gg!"
        img = icon_url(icon_id, icon_slug)
        embed_url = nowgg_url(nowgg_path)

        html = page_head(title, desc, prefix="..", og_image=img)
        html += page_nav(prefix="..")

        html += f'''
<div class="container game-wrapper">
  <div class="row">
      <div class="col-md-9">
            <div class="game-container">
                <div class="game-content">
                    <div class="game-iframe-container" id="game-player">
                        <div id="mobile-back-button" draggable="true">
                            <i class="bi bi-x-circle-fill"></i>
                        </div>
                        <iframe class="game-iframe" id="game-area" src="{embed_url}" width="480" height="800" scrolling="none" frameborder="0" allowfullscreen></iframe>
                    </div>
                </div>
                <div class="game-info">
                    <div class="header-left">
                        <h1 class="single-title">{title}</h1>
                        <span class="tag-item">{cat}</span>
                        <span class="tag-item">Rating: {rating}/5</span>
                    </div>
                    <div class="header-right">
                        <div class="b-action2">
                            <a href="#" onclick="open_fullscreen()" class="btn btn-capsule"><i class="bi bi-arrows-fullscreen b-icon"></i>Fullscreen</a>
                            <a href="{embed_url}" target="_blank" class="btn btn-capsule"><i class="bi bi-box-arrow-up-right b-icon"></i>Play on now.gg</a>
                        </div>
                    </div>
                </div>
            </div>
      </div>
      <div class="col-md-3">
        <div class="widget">
            <h4 class="widget-title">Game Info</h4>
            <p><strong>Category:</strong> <a href="/category/{cat.lower()}.html">{cat}</a></p>
            <p><strong>Rating:</strong> {rating}/5</p>
            <p><strong>Platform:</strong> Cloud Gaming</p>
            <p>Play {title} online instantly in your browser. No downloads needed!</p>
        </div>
      </div>
  </div>
</div>
'''
        # Related games
        related = [x for x in GAMES if x[3] == cat and x[0] != slug][:6]
        if not related:
            related = [x for x in GAMES if x[0] != slug][:6]

        html += '<div class="container">\n'
        html += '    <h2 class="item-title">You might also like</h2>\n'
        html += '    <div class="row">\n'
        for r in related:
            html += game_card_grid3(r, prefix="..")
        html += '    </div>\n'
        html += '</div>\n'
        html += page_footer(prefix="..")

        filepath = os.path.join(BASE, "play", f"{slug}.html")
        with open(filepath, "w") as f:
            f.write(html)
    print(f"Generated {len(GAMES)} play pages")

# ========== GENERATE CATEGORY PAGES ==========
def generate_category_pages():
    for cat in CATEGORIES:
        cat_games = [g for g in GAMES if g[3] == cat]
        desc = f"Play the best {cat} games online for free. No downloads required - instant cloud gaming!"

        html = page_head(f"{cat} Games", desc, prefix="..")
        html += page_nav(prefix="..")

        html += f'''
<div class="container">
    <h1 class="page-title">{cat} Games</h1>
    <div class="category-description">
        <p>Play the best {cat} games online for free on {SITE_NAME}. No downloads required - all games run instantly in your browser powered by now.gg cloud gaming!</p>
    </div>
    <div class="row grid-container">
'''
        for g in cat_games:
            html += game_card_grid2(g, prefix="..")
        html += '    </div>\n'

        # Other categories
        html += '    <h3 class="section-title">Other Categories</h3>\n'
        html += '    <ul class="category-list-wrapper">\n'
        for c in CATEGORIES:
            if c != cat:
                count = sum(1 for g in GAMES if g[3] == c)
                html += f'        <li class="cat-item"><a href="/category/{c.lower()}.html"><span class="cat-name">{c}</span> <span class="cat-game-amount">({count})</span></a></li>\n'
        html += '    </ul>\n'
        html += '</div>\n'
        html += page_footer(prefix="..")

        filepath = os.path.join(BASE, "category", f"{cat.lower()}.html")
        with open(filepath, "w") as f:
            f.write(html)
    print(f"Generated {len(CATEGORIES)} category pages")

# ========== GENERATE LEGAL PAGES ==========
def generate_legal_pages():
    pages = {
        "policy.html": ("Privacy Policy", f'''
<div class="container page-content">
    <h1 class="page-title">Privacy Policy</h1>
    <div class="category-description">
        <p>Last updated: 2024</p>
        <h3>Information We Collect</h3>
        <p>{SITE_NAME} does not collect personal information from users. We may use third-party analytics services to understand how our site is used.</p>
        <h3>Cookies</h3>
        <p>We may use cookies to enhance your experience. You can disable cookies in your browser settings.</p>
        <h3>Third-Party Services</h3>
        <p>Games on this site are provided through now.gg cloud gaming. Please refer to now.gg's privacy policy for information about data they may collect during gameplay.</p>
        <h3>Changes</h3>
        <p>We may update this policy from time to time. Changes will be posted on this page.</p>
        <h3>Contact</h3>
        <p>If you have questions about this privacy policy, please contact us through our GitHub page.</p>
    </div>
</div>
'''),
        "term.html": ("Terms of Service", f'''
<div class="container page-content">
    <h1 class="page-title">Terms of Service</h1>
    <div class="category-description">
        <p>Last updated: 2024</p>
        <h3>Acceptance of Terms</h3>
        <p>By using {SITE_NAME}, you agree to these terms of service.</p>
        <h3>Use of Service</h3>
        <p>{SITE_NAME} provides links to games hosted on now.gg's cloud gaming platform. We do not host any game content directly.</p>
        <h3>Intellectual Property</h3>
        <p>All game content belongs to their respective owners. {SITE_NAME} is a directory and aggregation service.</p>
        <h3>Disclaimer</h3>
        <p>Games are provided "as is" through now.gg's platform. We make no warranties about game availability or performance.</p>
        <h3>Changes</h3>
        <p>We reserve the right to modify these terms at any time.</p>
    </div>
</div>
'''),
        "dmca.html": ("DMCA", f'''
<div class="container page-content">
    <h1 class="page-title">DMCA Policy</h1>
    <div class="category-description">
        <p>Last updated: 2024</p>
        <h3>Copyright Notice</h3>
        <p>{SITE_NAME} respects the intellectual property rights of others. If you believe that any content on our site infringes your copyright, please contact us.</p>
        <h3>How to File a DMCA Takedown Notice</h3>
        <p>To file a DMCA takedown notice, please provide:</p>
        <ul>
            <li>A description of the copyrighted work you claim has been infringed</li>
            <li>The URL of the infringing content on our site</li>
            <li>Your contact information</li>
            <li>A statement that you have a good faith belief that the use is not authorized</li>
            <li>A statement that the information in the notification is accurate</li>
        </ul>
        <h3>Contact</h3>
        <p>Please submit DMCA notices through our GitHub repository's issues page.</p>
    </div>
</div>
'''),
    }

    for filename, (title, content) in pages.items():
        desc = f"{title} - {SITE_NAME}"
        html = page_head(title, desc)
        html += page_nav()
        html += content
        html += page_footer()

        with open(os.path.join(BASE, filename), "w") as f:
            f.write(html)
    print("Generated legal pages")

if __name__ == "__main__":
    generate_index()
    generate_play_pages()
    generate_category_pages()
    generate_legal_pages()
    print("Site generation complete!")
