:: setup-web-folder.bat
:: Run this in your vault root directory to set up Quartz properly

@echo off
echo 🚀 Setting up Quartz in web folder for GitHub Actions...
echo.

:: Check if we're in vault root
if not exist "00-CAMPAIGN" (
    echo ❌ Please run this from your vault root directory
    echo    (where you can see 00-CAMPAIGN, 01-CHARACTERS, etc.)
    pause
    exit /b 1
)

:: Create web directory if it doesn't exist
if not exist "web" mkdir web
cd web

:: Clone Quartz if not already done
if not exist "package.json" (
    echo 📦 Installing Quartz...
    git init
    git remote add origin https://github.com/jackyzha0/quartz.git
    git pull origin v4
    npm install
) else (
    echo ✅ Quartz already installed
)

:: Create campaign-specific config
echo 🔧 Creating campaign configuration...

:: Create the index page that will be your homepage
if not exist "content" mkdir content
> content\index.md (
echo ---
echo title: "Daggerheart Campaign Wiki"
echo ---
echo.
echo # 🎵 Welcome to Our Campaign Wiki
echo.
echo *Maintained by Captain Howling Banjo ^(Gareth^) for our adventuring party*
echo.
echo ## 🎭 Quick Access
echo.
echo ### 👥 [Our Party](01-CHARACTERS/)
echo - [🎵 Captain Howling Banjo ^(Gareth^)](01-CHARACTERS/gareth-character/captain-howling-banjo-sheet.md^)
echo - [🧝‍♀️ Vaerenth ^(Andi^)](01-CHARACTERS/andi-character/vaerenth-character-sheet.md^)
echo - [🌟 Aster Luferi ^(Luie^)](01-CHARACTERS/luie-character/aster-luferi-character-sheet.md^)
echo - [📚 Augustus Penhallow ^(Mark^)](01-CHARACTERS/mark-character/augustus-penhallow-character-sheet.md^)
echo.
echo ### 📖 [Session Chronicles](02-SESSIONS/)
echo Our adventure log with key events and decisions.
echo.
echo ### 🌍 [World Knowledge](03-WORLD/)
echo Locations, NPCs, and lore we've discovered.
echo.
echo ### 📚 [Rules ^& References](04-RESOURCES/)
echo Quick access to game mechanics and references.
echo.
echo ### ⚔️ [Build Optimization](06-RULES-MASTERY/)
echo Character builds and combat tactics.
echo.
echo ---
echo.
echo ## 💬 Contributing
echo.
echo Found something to add or fix? [Create an issue](https://github.com/ggfevans/daggerheart-campaign-vault/issues^) or message Banjo!
echo.
echo *Updated automatically when vault content changes*
)

echo ✅ Web folder configured successfully!
echo.
echo 📁 Structure created:
echo    web/
echo    ├── quartz/           ^(Quartz engine^)
echo    ├── content/          ^(Will link to vault content^)
echo    ├── package.json      ^(Dependencies^)
echo    └── quartz.config.ts  ^(Configuration^)
echo.
echo 🚀 Next step: Add GitHub Actions workflow file
echo.
pause