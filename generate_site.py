#!/usr/bin/env python3
"""Generate now.gg-style games portal site."""
import os

BASE = "/Users/noahgardner/Documents/GitHub/Ngardner29"
SITE_NAME = "DaGoatGames"
SITE_DOMAIN = "dagoatgames67.github.io"

# (slug, title, nowgg_path, category, icon_id, icon_slug, rating, description)
GAMES = [
    # Sports
    ("rocket-league-sideswipe", "Rocket League Sideswipe", "/apps/psyonix-studios/4656/rocket-league.html", "Sports", "4656", "rocket-league", "4.25",
     "Rocket League Sideswipe is a sports game developed by Psyonix Studios. Play the hit car soccer game on the go! Compete in 1v1 or 2v2 matches, climb the ranks, and unlock items."),
    ("nba-live-mobile-basketball", "NBA LIVE Mobile Basketball", "/apps/electronic-arts/2156/nba-live-mobile-basketball.html", "Sports", "2156", "nba-live-mobile-basketball", "4.3",
     "Build your team, compete in seasons and dominate the court in NBA LIVE Mobile Basketball."),
    ("retro-bowl", "Retro Bowl", "/apps/retro-bowl/51320/retro-bowl.html", "Sports", "51320", "retro-bowl", "4.5",
     "Retro Bowl is a retro-style American football game. Manage your team and lead them to victory!"),
    ("upd-volleyball-legend", "UPD Volleyball Legend", "/apps/upd-volleyball-legen/19915/upd-volleyball-legen.html", "Sports", "19915", "upd-volleyball-legen", "4.5",
     "Play volleyball with friends and become a legend in UPD Volleyball Legend."),
    ("golf-clash", "Golf Clash", "/apps/golf-clash/8915/golf-clash.html", "Sports", "8915", "golf-clash", "4.2",
     "Play golf against players around the world in real-time in Golf Clash."),
    ("real-cricket-20", "Real Cricket 20", "/apps/real-cricket/8920/real-cricket-20.html", "Sports", "8920", "real-cricket-20", "4.1",
     "The most comprehensive cricket game on mobile. Play Real Cricket 20 online."),
    # Action
    ("ace-defender", "Ace Defender", "/apps/juefeng-games/9152/ace-defender.html", "Action", "9152", "ace-defender", "4.6",
     "Ace Defender is a strategic action game where you defend your base against waves of enemies."),
    ("counter-attack", "Counter Attack", "/apps/plug-in-digital/8258/counter-attack.html", "Action", "8258", "counter-attack", "3.9",
     "Counter Attack is a fast-paced multiplayer FPS game."),
    ("gangs-wars-pixel-shooter-rp", "Gangs Wars: Pixel Shooter RP", "/apps/playducky-com/8827/gangs-wars-pixel-shooter-rp.html", "Action", "8827", "gangs-wars-pixel-shooter-rp", "4.1",
     "Explore an open-world pixel environment in Gangs Wars: Pixel Shooter RP."),
    ("rumble-club", "Rumble Club", "/apps/lightfox-games-inc/8697/rumble-club.html", "Action", "8697", "rumble-club", "4.1",
     "Battle royale party game! Fight your way to the top in Rumble Club."),
    ("blox-fruit", "Blox Fruit", "/apps/Blox-fruit/19901/Blox-fruit.html", "Action", "19901", "b", "4.5",
     "Become a powerful fighter with devil fruit powers in Blox Fruit."),
    ("80-anime-vanguards", "80 Anime Vanguards", "/apps/80-anime-vanguards/19908/80-anime-vanguards.html", "Action", "19908", "80-anime-vanguards", "4.5",
     "Anime tower defense game with 80+ characters to collect and deploy."),
    ("battle-through-the-heavens", "Battle Through the Heavens", "/apps/juefeng-games/9089/battle-through-the-heavens.html", "Action", "9089", "battle-through-the-heavens", "4.4",
     "An action RPG based on the popular anime series Battle Through the Heavens."),
    ("bullet-echo", "Bullet Echo", "/apps/zeptolab/8700/bullet-echo.html", "Action", "8700", "bullet-echo", "4.3",
     "Top-down tactical shooter with stealth mechanics. Play Bullet Echo online."),
    ("super-sus", "Super Sus", "/apps/super-sus/8750/super-sus.html", "Action", "8750", "super-sus", "4.3",
     "A social deduction game in space. Find the impostor in Super Sus!"),
    # Casual
    ("impostor-rescue", "Impostor Rescue", "/apps/mobaso/8840/impostor-rescue.html", "Casual", "8840", "impostor-rescue", "4.5",
     "Solve puzzles and rescue the impostor in this fun casual puzzle game."),
    ("comfy-girl", "Comfy Girl", "/apps/plug-in-digital/8730/comfy-girl.html", "Casual", "8730", "comfy-girl", "4.2",
     "Relax and decorate your cozy space in Comfy Girl."),
    ("paws-go", "Paws Go!", "/apps/sofish-games/8826/paws-go.html", "Casual", "8826", "paws-go", "4.0",
     "A fun casual game featuring adorable pets on an adventure."),
    ("gacha-life-2", "Gacha Life 2", "/apps/lunime/5691/gacha-life-2.html", "Casual", "5691", "gacha-life-2", "4.4",
     "Create your own anime-styled characters and stories in Gacha Life 2."),
    ("gacha-club", "Gacha Club", "/apps/lunime/2132/gacha-club.html", "Casual", "2132", "gacha-club", "4.4",
     "Customize characters, create scenes, and battle in Gacha Club."),
    ("gacha-life", "Gacha Life", "/apps/lunime/5767/gacha-life.html", "Casual", "5767", "gacha-life", "4.3",
     "The original Gacha Life - create your own characters and dress them up!"),
    ("animal-run", "Animal Run!", "/apps/animal-run/8760/animal-run.html", "Casual", "8760", "animal-run", "4.1",
     "Run, jump, and dash through obstacles with cute animals."),
    # Simulation
    ("cat-from-hell-cat-simulator", "Cat From Hell - Cat Simulator", "/apps/nolodin/10613/cat-from-hell-cat-simulator.html", "Simulation", "10613", "cat-from-hell-cat-simulator", "4.4",
     "Cause chaos as a mischievous cat in this hilarious simulator."),
    ("adopt-me", "Adopt Me", "/apps/adopt-me/19912/adopt-me.html", "Simulation", "19912", "adopt-me", "4.5",
     "Adopt and raise adorable pets, decorate your home, and explore in Adopt Me."),
    ("brookhaven", "Brookhaven", "/apps/Brookhaven/19905/Brookhaven.html", "Simulation", "19905", "Brookhaven", "4.5",
     "Live your dream life in Brookhaven - roleplay, explore, and hang out with friends."),
    ("grow-a-garden", "Grow a Garden", "/apps/Grow-a-Garden/19903/Grow-a-Garden.html", "Simulation", "19903", "Grow-a-Garden", "4.5",
     "Plant seeds, grow beautiful flowers, and build your dream garden."),
    ("idle-prison-empire-tycoon", "Idle Prison Empire Tycoon", "/apps/wazzapps-global-limited/8695/idle-prison-empire-tycoon.html", "Simulation", "8695", "idle-prison-empire-tycoon", "4.7",
     "Build and manage your own prison empire in this idle tycoon game."),
    ("roller-coaster-life-theme-park", "Roller Coaster Life Theme Park", "/apps/sparkling-society-park-building-island-v/8698/roller-coaster-life-theme-park.html", "Simulation", "8698", "roller-coaster-life-theme-park", "4.4",
     "Design and build the ultimate theme park with incredible roller coasters."),
    ("dragon-city-mobile", "Dragon City Mobile", "/apps/dragon-city/8790/dragon-city-mobile.html", "Simulation", "8790", "dragon-city-mobile", "4.3",
     "Collect and breed dragons, build your dragon city, and battle other players."),
    # Racing
    ("indian-bikes-driving-3d", "Indian Bikes Driving 3D", "/apps/rohit-gaming-studio/8822/indian-bikes-driving-3d.html", "Racing", "8822", "indian-bikes-driving-3d", "4.1",
     "Drive bikes through Indian cities in this realistic 3D driving game."),
    ("mr-racer-car-racing", "MR RACER - Car Racing", "/apps/chennaigames-studio-private-limited/51921/mr-racer-car-racing.html", "Racing", "51921", "mr-racer-car-racing", "4.1",
     "High-speed car racing with stunning graphics. Race against traffic!"),
    ("smash-karts", "Smash Karts", "/apps/tall-team/51304/smash-karts.html", "Racing", "51304", "smash-karts", "4.2",
     "3D multiplayer kart battle arena. Race, fight, and win in Smash Karts!"),
    ("hill-climb-racing-2", "Hill Climb Racing 2", "/apps/fingersoft/8830/hill-climb-racing-2.html", "Racing", "8830", "hill-climb-racing-2", "4.4",
     "Race and climb hills in this physics-based driving game sequel."),
    ("happy-wheels", "Happy Wheels", "/apps/happy-wheels/51310/happy-wheels.html", "Racing", "51310", "happy-wheels", "4.3",
     "The classic ragdoll physics racing game. Choose your character and survive!"),
    # Puzzle
    ("polybuzz", "PolyBuzz", "/apps/cloud-whale-interactive-technology-llc/10386/polybuzz.html", "Puzzle", "10386", "polybuzz", "4.2",
     "A creative puzzle game with unique mechanics and colorful visuals."),
    ("ink-game", "Ink Game", "/apps/ink-game/19906/ink-game.html", "Puzzle", "19906", "ink-game", "4.5",
     "Paint and solve puzzles in this artistic ink-themed game."),
    ("escape-lockdown", "Escape Lockdown", "/apps/spatial-io/51907/escape-lockdown.html", "Puzzle", "51907", "escape-lockdown", "4.5",
     "Solve puzzles, find clues, and escape from locked rooms."),
    ("paranormal-inc", "Paranormal Inc.", "/apps/plug-in-digital/8264/paranormal-inc.html", "Puzzle", "8264", "paranormal-inc", "4.5",
     "Investigate paranormal activities and solve mysteries in Paranormal Inc."),
    # Strategy
    ("war-master", "War Master", "/apps/nese-dijital/8692/war-master.html", "Strategy", "8692", "war-master", "4.2",
     "Command your troops and conquer territories in War Master."),
    ("army-tycoon-idle-base", "Army Tycoon: Idle Base", "/apps/hello-games-team/8688/army-tycoon-idle-base.html", "Strategy", "8688", "army-tycoon-idle-base", "4.6",
     "Build and upgrade your military base in this idle strategy game."),
    ("state-of-survival", "State of Survival", "/apps/state-of-survival/8870/state-of-survival.html", "Strategy", "8870", "state-of-survival", "4.3",
     "Survive the zombie apocalypse, build settlements, and fight for survival."),
    ("clash-royale", "Clash Royale", "/apps/supercell/8885/clash-royale.html", "Strategy", "8885", "clash-royale", "4.5",
     "Real-time multiplayer battles with your favorite Clash characters. Collect and upgrade cards!"),
    # Adventure
    ("99-nights", "99 Nights in the Forest", "/apps/99-Nights/19902/99-Nights.html", "Adventure", "19902", "99-Nights", "4.5",
     "Survive 99 nights in a mysterious forest full of dangers and secrets."),
    ("poppy-playtime", "Poppy Playtime", "/apps/mob-games-studio/1293/poppy-playtime.html", "Adventure", "1293", "poppy-playtime", "4.4",
     "Explore an abandoned toy factory and uncover its dark secrets in Poppy Playtime."),
    ("dynamons-7", "Dynamons 7", "/apps/azerion-casual-games/51917/dynamons-7.html", "Adventure", "51917", "dynamons-7", "4.3",
     "Catch, train, and battle Dynamons in this creature-collecting adventure."),
    ("roblox", "Roblox", "/apps/roblox/19900/roblox.html", "Adventure", "19900", "roblox", "4.6",
     "Join millions of players in Roblox. Play, create, and share experiences with friends."),
    ("granny", "Granny", "/apps/granny/8890/granny.html", "Adventure", "8890", "granny", "4.2",
     "Escape from Granny's house! Solve puzzles and avoid getting caught."),
    # Arcade
    ("bloxd-io", "bloxd.io", "/apps/bloxd/51240/bloxd-io.html", "Arcade", "51240", "bloxd-io", "4.2",
     "Block-style multiplayer browser game with multiple game modes."),
    ("solitaire-social", "Solitaire Social", "/apps/kosmos-games/51904/solitaire-social.html", "Arcade", "51904", "solitaire-social", "4.5",
     "Classic solitaire with a social twist. Compete against real players!"),
    ("subway-surfers", "Subway Surfers", "/apps/subway-surfers/51330/subway-surfers.html", "Arcade", "51330", "subway-surfers", "4.5",
     "Dash through the subway and dodge trains in the iconic endless runner."),
    ("geometry-dash-lite", "Geometry Dash Lite", "/apps/geometry-dash/8935/geometry-dash-lite.html", "Arcade", "8935", "geometry-dash-lite", "4.4",
     "Jump and fly through danger in this rhythm-based platformer."),
    ("my-singing-monsters", "My Singing Monsters", "/apps/my-singing-monsters/8940/my-singing-monsters.html", "Arcade", "8940", "my-singing-monsters", "4.3",
     "Collect and breed musical monsters to create your own songs."),
    # Multiplayer
    ("among-us", "Among Us", "/apps/innersloth-llc/4047/among-us.html", "Multiplayer", "4047", "among-us", "4.5",
     "Play with 4-15 players online. Complete tasks or find the impostor in Among Us!"),
    ("bedwars", "BedWars", "/apps/bedwars/19910/bedwars.html", "Multiplayer", "19910", "bedwars", "4.4",
     "Protect your bed and destroy others in this multiplayer strategy game."),
    ("murder-mystery-2", "Murder Mystery 2", "/apps/murder-mystery-2/19911/murder-mystery-2.html", "Multiplayer", "19911", "murder-mystery-2", "4.3",
     "Who is the murderer? Solve the mystery or eliminate everyone in Murder Mystery 2."),
    # RPG
    ("soul-land-reloaded", "Soul Land Reloaded", "/apps/new-times-game/4075/soul-land.html", "RPG", "4075", "soul-land", "4.3",
     "An epic RPG based on the Soul Land anime universe. Collect heroes and battle!"),
    ("mu-origin-3", "MU Origin 3", "/apps/fingerfun/5581/mu-origin.html", "RPG", "5581", "mu-origin", "4.2",
     "The next chapter of the classic MU Online franchise. An MMORPG experience."),
]

CATEGORIES = sorted(set(g[3] for g in GAMES))

def icon_url(icon_id, icon_slug):
    return f"https://cdn.now.gg/apps-content/{icon_id}/icon/{icon_slug}.png"

def banner_url(icon_id, icon_slug):
    return f"https://cdn.now.gg/apps-content/{icon_id}/banner/desktop/{icon_slug}.jpg"

def nowgg_url(path):
    return f"https://now.gg{path}"

def nav_html(prefix=""):
    links = ""
    for c in CATEGORIES:
        links += f'        <li><a href="{prefix}/category/{c.lower()}.html">{c}</a></li>\n'
    return links

def page_head(title, desc, prefix=""):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title} - {SITE_NAME}</title>
    <meta name="description" content="{desc}">
    <link rel="icon" href="{prefix}/images/favicon.png" sizes="32x32">
    <link rel="stylesheet" href="{prefix}/css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
'''

def page_nav(prefix=""):
    return f'''<body>
    <nav class="navbar">
        <div class="container">
            <a href="{prefix}/" class="logo"><span>{SITE_NAME}</span></a>
            <div class="search-bar">
                <span class="search-icon">&#128269;</span>
                <input type="text" placeholder="Search" id="search-input" onkeyup="filterGames()">
            </div>
            <ul class="nav-links">
{nav_html(prefix)}
            </ul>
        </div>
    </nav>
    <div class="main-container">
'''

def page_footer(prefix=""):
    return f'''
    </div>
    <footer class="footer">
        <div>{SITE_NAME} &copy; 2024</div>
        <div style="margin-top:8px">
            <a href="{prefix}/policy.html">Privacy</a>
            <a href="{prefix}/term.html">Terms</a>
            <a href="{prefix}/dmca.html">DMCA</a>
        </div>
    </footer>
    <script src="{prefix}/js/script.js"></script>
</body>
</html>'''

def game_card(g, prefix=""):
    slug, title, _, cat, icon_id, icon_slug, rating, *_ = g
    img = icon_url(icon_id, icon_slug)
    return f'''<a href="{prefix}/play/{slug}.html" class="game-card" data-title="{title.lower()}">
    <img src="{img}" alt="{title}" class="game-card-img" loading="lazy">
    <div class="game-card-title">{title}</div>
</a>
'''

# ========== INDEX ==========
def generate_index():
    desc = f"Play your favorite mobile games online for free. No downloads required - instant cloud gaming!"
    html = page_head(f"Play Online Games for Free", desc)
    html += page_nav()

    # Top Games
    html += '<div class="section-header"><h2 class="section-title">Top Games</h2></div>\n'
    html += '<div class="game-grid" id="game-list">\n'
    for g in GAMES[:12]:
        html += game_card(g)
    html += '</div>\n'

    # Popular Games
    html += '<div class="section-header"><h2 class="section-title">Popular Games</h2></div>\n'
    html += '<div class="game-grid">\n'
    for g in GAMES[12:24]:
        html += game_card(g)
    html += '</div>\n'

    # More Games
    html += '<div class="section-header"><h2 class="section-title">More Games</h2></div>\n'
    html += '<div class="game-grid">\n'
    for g in GAMES[24:]:
        html += game_card(g)
    html += '</div>\n'

    # Categories
    html += '<div class="section-header"><h2 class="section-title">Explore by Categories</h2></div>\n'
    html += '<div class="category-grid">\n'
    for cat in CATEGORIES:
        count = sum(1 for g in GAMES if g[3] == cat)
        html += f'<a href="/category/{cat.lower()}.html" class="category-card"><h3>{cat}</h3><span>{count} games</span></a>\n'
    html += '</div>\n'

    html += page_footer()
    with open(os.path.join(BASE, "index.html"), "w") as f:
        f.write(html)
    print("Generated index.html")

# ========== PLAY PAGES ==========
def generate_play_pages():
    for g in GAMES:
        slug, title, nowgg_path, cat, icon_id, icon_slug, rating, desc_text = g
        img = icon_url(icon_id, icon_slug)
        banner = banner_url(icon_id, icon_slug)
        play_url = nowgg_url(nowgg_path)

        html = page_head(f"Play {title} Online for Free", desc_text, prefix="..")
        html += page_nav(prefix="..")

        html += f'''
<div class="game-page-header">
    <img src="{banner}" alt="{title}" class="game-banner" onerror="this.style.background='linear-gradient(135deg,#2d1b4e,#1a0a2e)';this.style.height='200px'">
</div>

<div class="game-page-content">
    <div class="game-page-main">
        <div class="game-page-info">
            <img src="{img}" alt="{title}" class="game-page-icon">
            <div class="game-page-details">
                <h1>{title}</h1>
                <div class="game-page-meta">
                    <span class="rating">&#11088; {rating}</span>
                    <span>|</span>
                    <a href="/category/{cat.lower()}.html">{cat} Games</a>
                </div>
            </div>
        </div>

        <div class="game-tags">
            <span class="game-tag">{cat}</span>
            <span class="game-tag">Free</span>
            <span class="game-tag">Online</span>
            <span class="game-tag">Multiplayer</span>
        </div>

        <a href="{play_url}" target="_blank" class="btn-play">Play in browser</a>

        <div class="game-description">
            <p>{desc_text}</p>
            <p style="margin-top:12px">Play {title} instantly in your browser without downloading. Enjoy lag-free, high-quality gaming with {SITE_NAME}.</p>
        </div>
    </div>
</div>
'''
        # Related games
        related = [x for x in GAMES if x[3] == cat and x[0] != slug][:6]
        if len(related) < 6:
            related += [x for x in GAMES if x[0] != slug and x not in related][:6-len(related)]

        html += '<div class="section-header"><h2 class="section-title">You might also like</h2></div>\n'
        html += '<div class="game-grid">\n'
        for r in related:
            html += game_card(r, prefix="..")
        html += '</div>\n'

        html += page_footer(prefix="..")
        with open(os.path.join(BASE, "play", f"{slug}.html"), "w") as f:
            f.write(html)
    print(f"Generated {len(GAMES)} play pages")

# ========== CATEGORY PAGES ==========
def generate_category_pages():
    for cat in CATEGORIES:
        cat_games = [g for g in GAMES if g[3] == cat]
        desc = f"Play the best {cat} games online for free. No downloads required!"

        html = page_head(f"{cat} Games", desc, prefix="..")
        html += page_nav(prefix="..")

        html += f'<div class="section-header"><h2 class="section-title">{cat} Games</h2></div>\n'
        html += '<div class="game-grid game-grid-wide">\n'
        for g in cat_games:
            html += game_card(g, prefix="..")
        html += '</div>\n'

        html += '<div class="section-header" style="margin-top:40px"><h2 class="section-title">Other Categories</h2></div>\n'
        html += '<div class="category-grid">\n'
        for c in CATEGORIES:
            if c != cat:
                count = sum(1 for g in GAMES if g[3] == c)
                html += f'<a href="/category/{c.lower()}.html" class="category-card"><h3>{c}</h3><span>{count} games</span></a>\n'
        html += '</div>\n'

        html += page_footer(prefix="..")
        with open(os.path.join(BASE, "category", f"{cat.lower()}.html"), "w") as f:
            f.write(html)
    print(f"Generated {len(CATEGORIES)} category pages")

# ========== LEGAL PAGES ==========
def generate_legal_pages():
    pages = {
        "policy.html": ("Privacy Policy", f"<div class='game-description'><h2 style='color:#fff;margin-bottom:16px'>Privacy Policy</h2><p>{SITE_NAME} does not collect personal information. Games are provided through now.gg cloud gaming. Refer to now.gg's privacy policy for data they may collect during gameplay.</p></div>"),
        "term.html": ("Terms of Service", f"<div class='game-description'><h2 style='color:#fff;margin-bottom:16px'>Terms of Service</h2><p>{SITE_NAME} provides links to games on now.gg's cloud gaming platform. All game content belongs to their respective owners. Games are provided 'as is'.</p></div>"),
        "dmca.html": ("DMCA", f"<div class='game-description'><h2 style='color:#fff;margin-bottom:16px'>DMCA Policy</h2><p>{SITE_NAME} respects intellectual property rights. If you believe content infringes your copyright, please submit a notice through our GitHub repository.</p></div>"),
    }
    for filename, (title, content) in pages.items():
        html = page_head(title, f"{title} - {SITE_NAME}")
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
    print("Done!")
