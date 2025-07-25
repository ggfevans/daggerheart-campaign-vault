:: post-clone-setup.bat
:: Run this in your web/ folder after cloning Quartz

@echo off
echo 🔧 Configuring Quartz for Daggerheart Campaign...
echo.

:: Verify we're in the right place
if not exist "package.json" (
    echo ❌ Please run this from your web/ folder where package.json exists
    echo    (Should be: daggerheart-campaign-vault/web/)
    pause
    exit /b 1
)

:: Check current structure
echo 📁 Current web folder structure:
dir /b
echo.

:: Install dependencies if not done
if not exist "node_modules" (
    echo 📦 Installing npm dependencies...
    npm install
    if errorlevel 1 (
        echo ❌ npm install failed
        pause
        exit /b 1
    )
    echo ✅ Dependencies installed
) else (
    echo ✅ Dependencies already installed
)

:: Backup original config if it exists
if exist "quartz.config.ts" (
    echo 💾 Backing up original config...
    copy "quartz.config.ts" "quartz.config.ts.original"
)

:: Remove default content
echo 🧹 Cleaning default content...
if exist "content" (
    rd /s /q "content"
)
mkdir content

echo 📝 Creating campaign homepage...
:: Create the campaign index page
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
echo ### 👥 Our Party
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
echo ## 🕸️ Explore Connections
echo.
echo Use the **Graph View** ^(top right^) to see how characters, locations, and story threads connect!
echo.
echo ## 💬 Contributing
echo.
echo Found something to add or fix? [Create an issue](https://github.com/ggfevans/daggerheart-campaign-vault/issues^) or message Banjo!
echo.
echo *Updated automatically when vault content changes*
)

echo ✅ Campaign homepage created
echo.

:: Test build to make sure everything works
echo 🔨 Testing initial build...
call npx quartz build
if errorlevel 1 (
    echo ❌ Build test failed - check the error above
    pause
    exit /b 1
)

echo ✅ Build test successful!
echo.
echo 📁 Generated files:
dir public /b | head -5
echo    ... and more
echo.

echo 🎯 Next steps:
echo    1. Replace quartz.config.ts with campaign-specific config
echo    2. Test with some vault content
echo    3. Set up GitHub Actions workflow
echo    4. Push to GitHub for first deployment
echo.
pause