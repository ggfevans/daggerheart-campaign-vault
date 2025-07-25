:: test-vault-content.bat
:: Test linking vault content to verify everything works

@echo off
echo 🧪 Testing vault content integration...
echo.

:: Verify we're in web folder and parent has vault content
if not exist "..\00-CAMPAIGN" (
    echo ❌ Vault content not found in parent directory
    echo    Expected to find: ..\00-CAMPAIGN, ..\01-CHARACTERS, etc.
    echo    Are you running this from web/ folder inside your vault?
    pause
    exit /b 1
)

echo ✅ Vault content found in parent directory
echo.

:: Show what vault folders we have
echo 📁 Available vault folders:
dir ..\0* /b /ad 2>nul
echo.

:: Create test links to vault content
echo 🔗 Creating test content links...

:: Link campaign folders (the ones that exist)
for %%f in (00-CAMPAIGN 01-CHARACTERS 02-SESSIONS 03-WORLD 04-RESOURCES 05-LORE 06-RULES-MASTERY) do (
    if exist "..\%%f" (
        echo   📁 Linking %%f
        if exist "content\%%f" rd /s /q "content\%%f"
        mklink /D "content\%%f" "..\%%f" >nul
        if errorlevel 1 (
            echo      ⚠️  Symlink failed, trying junction...
            mklink /J "content\%%f" "..\%%f" >nul
        )
    ) else (
        echo   ⚠️  %%f not found, skipping
    )
)

echo.
echo 📋 Content structure:
dir content /b
echo.

:: Test build with vault content
echo 🔨 Testing build with vault content...
call npx quartz build
if errorlevel 1 (
    echo ❌ Build failed with vault content
    echo    Check the error above for details
    pause
    exit /b 1
)

echo ✅ Build successful with vault content!
echo.

:: Show what was generated
echo 📊 Generated pages:
dir public /b | findstr ".html" | head -10
echo    ... and more
echo.

echo 🌐 Testing local preview...
echo    Starting local server on http://localhost:8080
echo    Press Ctrl+C to stop the server
echo.
echo 🎯 What to test:
echo    1. Homepage loads correctly
echo    2. Navigation to character sheets works
echo    3. Internal links function properly  
echo    4. Graph view shows connections
echo    5. Mobile view is responsive
echo.

:: Start local server for testing
call npx quartz serve

echo.
echo ✅ Local testing complete!
echo.
echo 🚀 Next steps:
echo    1. If everything looks good, commit your changes
echo    2. Add GitHub Actions workflow
echo    3. Push to GitHub for automated deployment
echo.
pause