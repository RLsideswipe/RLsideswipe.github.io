#!/usr/bin/env python3
"""Generate DaGoatGames site - Rocket League Sideswipe."""
import os

BASE = "/Users/noahgardner/Documents/GitHub/Ngardner29"
SITE_NAME = "DaGoatGames"
SITE_DOMAIN = "dagoatgames67.github.io"

# Rocket League Sideswipe - verified CDN URLs
GAME = {
    "slug": "rocket-league-sideswipe",
    "title": "Rocket League Sideswipe",
    "nowgg_path": "/apps/psyonix-studios/4656/rocket-league.html",
    "category": "Sports",
    "rating": "4.25",
    "icon": "https://cdn.now.gg/apps-content/com.Psyonix.RL2D/icon/rocket-league-sideswipe.png",
    "banner": "https://cdn.now.gg/apps-content/com.Psyonix.RL2D/game-tiles/rocket-league-sideswipe.jpg",
    "description": "Rocket League Sideswipe is a sports game developed by Psyonix Studios. Play the hit car soccer game on the go! Compete in 1v1 or 2v2 matches, climb the ranks, and unlock items.",
}

PLAY_URL = f"https://now.gg{GAME['nowgg_path']}"


def generate_index():
    g = GAME
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{SITE_NAME} - Play {g["title"]} Online</title>
    <meta name="description" content="Play {g["title"]} online for free. No downloads required - instant cloud gaming!">
    <link rel="icon" href="/images/favicon.png" sizes="32x32">
    <link rel="stylesheet" href="/css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <a href="/" class="logo"><span>{SITE_NAME}</span></a>
        </div>
    </nav>
    <div class="main-container">

        <div class="hero-section">
            <img src="{g["banner"]}" alt="{g["title"]}" class="hero-banner" onerror="this.style.display='none'">
            <div class="hero-overlay">
                <img src="{g["icon"]}" alt="{g["title"]}" class="hero-icon">
                <div class="hero-info">
                    <h1>{g["title"]}</h1>
                    <div class="hero-meta">
                        <span class="rating">&#11088; {g["rating"]}</span>
                        <span class="game-tag">{g["category"]}</span>
                        <span class="game-tag">Free</span>
                        <span class="game-tag">Online</span>
                    </div>
                    <a href="/play/{g["slug"]}.html" class="btn-play">Play Now</a>
                </div>
            </div>
        </div>

        <div class="game-description" style="max-width:800px;margin:32px auto;">
            <h2 style="color:#fff;margin-bottom:12px">About {g["title"]}</h2>
            <p>{g["description"]}</p>
            <p style="margin-top:12px">Play instantly in your browser - no downloads needed. Powered by cloud gaming.</p>
        </div>

    </div>
    <footer class="footer">
        <div>{SITE_NAME} &copy; 2024</div>
        <div style="margin-top:8px">
            <a href="/policy.html">Privacy</a>
            <a href="/term.html">Terms</a>
            <a href="/dmca.html">DMCA</a>
        </div>
    </footer>
</body>
</html>'''
    with open(os.path.join(BASE, "index.html"), "w") as f:
        f.write(html)
    print("Generated index.html")


def generate_play_page():
    g = GAME
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Play {g["title"]} Online - {SITE_NAME}</title>
    <meta name="description" content="{g["description"]}">
    <link rel="icon" href="/images/favicon.png" sizes="32x32">
    <link rel="stylesheet" href="/css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <a href="/" class="logo"><span>{SITE_NAME}</span></a>
        </div>
    </nav>
    <div class="main-container">

        <div class="game-page-header">
            <img src="{g["banner"]}" alt="{g["title"]}" class="game-banner" onerror="this.style.background='linear-gradient(135deg,#2d1b4e,#1a0a2e)';this.style.height='200px'">
        </div>

        <div class="game-page-content">
            <div class="game-page-main">
                <div class="game-page-info">
                    <img src="{g["icon"]}" alt="{g["title"]}" class="game-page-icon">
                    <div class="game-page-details">
                        <h1>{g["title"]}</h1>
                        <div class="game-page-meta">
                            <span class="rating">&#11088; {g["rating"]}</span>
                            <span>|</span>
                            <span>{g["category"]} Games</span>
                        </div>
                    </div>
                </div>

                <div class="game-tags">
                    <span class="game-tag">{g["category"]}</span>
                    <span class="game-tag">Free</span>
                    <span class="game-tag">Online</span>
                    <span class="game-tag">Multiplayer</span>
                </div>

                <button onclick="launchGame()" class="btn-play">Play in browser</button>

                <div class="game-description">
                    <p>{g["description"]}</p>
                    <p style="margin-top:12px">Play {g["title"]} instantly in your browser without downloading. Enjoy lag-free, high-quality gaming with {SITE_NAME}.</p>
                </div>
            </div>
        </div>

    </div>

    <div class="game-iframe-container" id="game-container">
        <button class="game-iframe-close" onclick="closeGame()">&#10005;</button>
        <iframe id="game-frame" allowfullscreen allow="autoplay; fullscreen; gamepad; microphone"></iframe>
    </div>

    <footer class="footer">
        <div>{SITE_NAME} &copy; 2024</div>
        <div style="margin-top:8px">
            <a href="/policy.html">Privacy</a>
            <a href="/term.html">Terms</a>
            <a href="/dmca.html">DMCA</a>
        </div>
    </footer>
    <script>
        function launchGame() {{
            var container = document.getElementById('game-container');
            var frame = document.getElementById('game-frame');
            frame.src = "{PLAY_URL}";
            container.classList.add('active');
            document.body.style.overflow = 'hidden';
        }}
        function closeGame() {{
            var container = document.getElementById('game-container');
            var frame = document.getElementById('game-frame');
            frame.src = '';
            container.classList.remove('active');
            document.body.style.overflow = '';
        }}
        document.addEventListener('keydown', function(e) {{
            if (e.key === 'Escape') closeGame();
        }});
    </script>
</body>
</html>'''
    os.makedirs(os.path.join(BASE, "play"), exist_ok=True)
    with open(os.path.join(BASE, "play", f"{g['slug']}.html"), "w") as f:
        f.write(html)
    print("Generated play page")


def generate_legal_pages():
    pages = {
        "policy.html": ("Privacy Policy", f"<div class='game-description' style='max-width:800px;margin:32px auto'><h2 style='color:#fff;margin-bottom:16px'>Privacy Policy</h2><p>{SITE_NAME} does not collect personal information. Games are provided through now.gg cloud gaming. Refer to now.gg's privacy policy for data they may collect during gameplay.</p></div>"),
        "term.html": ("Terms of Service", f"<div class='game-description' style='max-width:800px;margin:32px auto'><h2 style='color:#fff;margin-bottom:16px'>Terms of Service</h2><p>{SITE_NAME} provides links to games on now.gg's cloud gaming platform. All game content belongs to their respective owners. Games are provided 'as is'.</p></div>"),
        "dmca.html": ("DMCA", f"<div class='game-description' style='max-width:800px;margin:32px auto'><h2 style='color:#fff;margin-bottom:16px'>DMCA Policy</h2><p>{SITE_NAME} respects intellectual property rights. If you believe content infringes your copyright, please submit a notice through our GitHub repository.</p></div>"),
    }
    for filename, (title, content) in pages.items():
        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title} - {SITE_NAME}</title>
    <meta name="description" content="{title} - {SITE_NAME}">
    <link rel="icon" href="/images/favicon.png" sizes="32x32">
    <link rel="stylesheet" href="/css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <a href="/" class="logo"><span>{SITE_NAME}</span></a>
        </div>
    </nav>
    <div class="main-container">
        {content}
    </div>
    <footer class="footer">
        <div>{SITE_NAME} &copy; 2024</div>
        <div style="margin-top:8px">
            <a href="/policy.html">Privacy</a>
            <a href="/term.html">Terms</a>
            <a href="/dmca.html">DMCA</a>
        </div>
    </footer>
</body>
</html>'''
        with open(os.path.join(BASE, filename), "w") as f:
            f.write(html)
    print("Generated legal pages")


if __name__ == "__main__":
    generate_index()
    generate_play_page()
    generate_legal_pages()
    print("Done!")
