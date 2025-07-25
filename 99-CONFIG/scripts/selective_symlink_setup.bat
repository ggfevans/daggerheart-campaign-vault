:: setup-content-links.bat
:: Run this from web\quartz\ directory
:: Creates selective symlinks to avoid any loop possibility

@echo off
echo 🔗 Setting up selective content symlinks...
echo.

:: Verify we're in the right location (web\quartz)
if not exist "quartz.config.ts" (
    echo ❌ Please run this from web\quartz\ directory
    echo    Looking for: quartz.config.ts
    pause
    exit /b 1
)

:: Check that vault content exists at expected location
if not exist "..\..\00-CAMPAIGN" (
    echo ❌ Vault content not found at expected location
    echo    Expected: ..\..\00-CAMPAIGN
    echo    Current directory: %CD%
    echo    Vault should be 2 levels up from here
    pause
    exit /b 1
)

echo ✅ Vault content found at correct location
echo.

:: Create content directory if it doesn't exist
if not exist "content" mkdir content
cd content

:: Remove any existing links/content (except our index.md if it exists)
for /D %%d in (*) do (
    if not "%%d"=="assets" (
        echo   🗑️ Removing old %%d
        rd /s /q "%%d" 2>nul
    )
)

:: Create index.md if it doesn't exist
if not exist "index.md" (
    echo 📝 Creating homepage...
    > index.md (
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
        echo ### 👥 [Our Party](01-CHARACTERS/^)
        echo - [🎵 Captain Howling Banjo ^(Gareth^)](01-CHARACTERS/gareth-character/captain-howling-banjo-sheet.md^)
        echo - [🧝‍♀️ Vaerenth ^(Andi^)](01-CHARACTERS/andi-character/vaerenth-character-sheet.md^)
        echo - [🌟 Aster Luferi ^(Luie^)](01-CHARACTERS/luie-character/aster-luferi-character-sheet.md^)
        echo - [📚 Augustus Penhallow ^(Mark^)](01-CHARACTERS/mark-character/augustus-penhallow-character-sheet.md^)
        echo.
        echo ### 📖 [Session Chronicles](02-SESSIONS/^)
        echo Our adventure log with key events and decisions.
        echo.
        echo ### 🌍 [World Knowledge](03-WORLD/^)
        echo Locations, NPCs, and lore we've discovered.
        echo.
        echo ### 📚 [Rules ^& References](04-RESOURCES/^)
        echo Quick access to game mechanics and references.
        echo.
        echo ### ⚔️ [Build Optimization](06-RULES-MASTERY/^)
        echo Character builds and combat tactics.
        echo.
        echo ---
        echo.
        echo ## 🕸️ Explore Connections
        echo.
        echo Use the **Graph View** to see how characters, locations, and story threads connect!
        echo.
        echo ## 💬 Contributing
        echo.
        echo Found something to add or fix? [Create an issue](https://github.com/ggfevans/daggerheart-campaign-vault/issues^) or message Banjo!
        echo.
        echo *Updated automatically when vault content changes*
    )
)

echo 🔗 Creating selective symlinks to campaign folders...

:: Link each campaign folder individually to avoid any loop possibility
:: This is the safest approach - no chance of circular references

for %%f in (00-CAMPAIGN 01-CHARACTERS 02-SESSIONS 03-WORLD 04-RESOURCES 05-LORE 06-RULES-MASTERY) do (
    if exist "..\..\..\%%f" (
        echo   📁 Linking %%f
        mklink /D "%%f" "..\..\..\%%f" >nul 2>&1
        if errorlevel 1 (
            echo      ⚠️  Symlink failed, trying junction...
            mklink /J "%%f" "..\..\..\%%f" >nul 2>&1
            if errorlevel 1 (
                echo      ❌ Both symlink and junction failed for %%f
            ) else (
                echo      ✅ Junction created for %%f
            )
        ) else (
            echo      ✅ Symlink created for %%f
        )
    ) else (
        echo   ⚠️  %%f not found in vault, skipping
    )
)

:: Return to quartz directory
cd ..

echo.
echo 📁 Final content structure:
dir content /b
echo.

:: Test build
echo 🔨 Testing build with linked content...
call npx quartz build
if errorlevel 1 (
    echo ❌ Build failed - check errors above
    pause
    exit /b 1
)

echo ✅ Build successful!
echo.
echo 🎯 What we accomplished:
echo    ✅ Selective symlinks to campaign folders only
echo    ✅ No possibility of circular references  
echo    ✅ Homepage created with campaign navigation
echo    ✅ Build test passed
echo.
echo 🚀 Ready for GitHub Actions!
echo.
echo 💡 To test locally: npx quartz serve
echo.
pause