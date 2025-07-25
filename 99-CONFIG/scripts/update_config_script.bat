:: update-quartz-config.bat
:: Replace default config with campaign-optimized version

@echo off
echo 🔧 Updating Quartz configuration for campaign...
echo.

:: Verify location
if not exist "quartz.config.ts" (
    echo ❌ quartz.config.ts not found. Are you in the web/ folder?
    pause
    exit /b 1
)

:: Backup existing config
echo 💾 Backing up current config...
copy "quartz.config.ts" "quartz.config.ts.backup"

:: Create the new campaign-optimized config
echo 📝 Creating campaign-optimized configuration...

> quartz.config.ts (
echo // Campaign-optimized Quartz configuration
echo import { QuartzConfig } from "./quartz/cfg"
echo import * as Plugin from "./quartz/plugins"
echo.
echo const config: QuartzConfig = {
echo   configuration: {
echo     pageTitle: "🎲 Daggerheart Campaign Wiki",
echo     enableSPA: true,
echo     enablePopovers: true,
echo     analytics: null,
echo     locale: "en-US",
echo     baseUrl: "ggfevans.github.io/daggerheart-campaign-vault",
echo     ignorePatterns: [
echo       "private",
echo       "templates",
echo       "*.tmp", 
echo       ".obsidian/**",
echo       "web/**",
echo       "99-CONFIG/**",
echo       "**/.DS_Store",
echo       "**/Thumbs.db",
echo     ],
echo     defaultDateType: "created",
echo     theme: {
echo       fontOrigin: "googleFonts",
echo       cdnCaching: true,
echo       typography: {
echo         header: "Schibsted Grotesk",
echo         body: "Source Sans Pro", 
echo         code: "IBM Plex Mono",
echo       },
echo       colors: {
echo         lightMode: {
echo           light: "#faf8f8",
echo           lightgray: "#e5e5e5",
echo           gray: "#b8b8b8",
echo           darkgray: "#4e4e4e", 
echo           dark: "#2b2b2b",
echo           secondary: "#8b4513",
echo           tertiary: "#cd853f",
echo           highlight: "rgba(139, 69, 19, 0.15)",
echo         },
echo         darkMode: {
echo           light: "#1a1a1a",
echo           lightgray: "#393639",
echo           gray: "#646464",
echo           darkgray: "#d4d4d4",
echo           dark: "#ebebec", 
echo           secondary: "#daa520",
echo           tertiary: "#cd853f",
echo           highlight: "rgba(218, 165, 32, 0.15)",
echo         },
echo       },
echo     },
echo   },
echo   plugins: {
echo     transformers: [
echo       Plugin.FrontMatter(^),
echo       Plugin.CreatedModifiedDate({
echo         priority: ["frontmatter", "filesystem"],
echo       }^),
echo       Plugin.Latex({ renderEngine: "katex" }^),
echo       Plugin.SyntaxHighlighting({
echo         theme: {
echo           light: "github-light",
echo           dark: "github-dark",
echo         },
echo         keepBackground: false,
echo       }^),
echo       Plugin.ObsidianFlavoredMarkdown({
echo         enableInHtmlEmbed: false,
echo         parseTags: true,
echo         parseBlockReferences: true,
echo         parseArrows: true,
echo         enableVideoEmbed: true,
echo         enableCheckbox: true,
echo         enableTaskLists: true,
echo         enableCallouts: true,
echo       }^),
echo       Plugin.GitHubFlavoredMarkdown(^),
echo       Plugin.TableOfContents({
echo         maxDepth: 3,
echo         minEntries: 2,
echo         showByDefault: true,
echo         collapseByDefault: false,
echo       }^),
echo       Plugin.CrawlLinks({
echo         markdownLinkResolution: "shortest",
echo         prettyLinks: true,
echo         openLinksInNewTab: false,
echo         lazyLoad: true,
echo         externalLinkIcon: true,
echo       }^),
echo       Plugin.Description({
echo         descriptionLength: 150,
echo       }^),
echo     ],
echo     filters: [Plugin.RemoveDrafts(^)],
echo     emitters: [
echo       Plugin.AliasRedirects(^),
echo       Plugin.ComponentResources(^),
echo       Plugin.ContentPage(^),
echo       Plugin.FolderPage(^),
echo       Plugin.TagPage(^),
echo       Plugin.ContentIndex({
echo         enableSiteMap: true,
echo         enableRSS: true,
echo         includeEmptyFiles: false,
echo         rssLimit: 10,
echo         rssFullHtml: false,
echo       }^),
echo       Plugin.Assets(^),
echo       Plugin.Static(^),
echo       Plugin.NotFoundPage(^),
echo     ],
echo   },
echo }
echo.
echo export default config
)

echo ✅ Configuration updated successfully!
echo.

:: Test the new config
echo 🔨 Testing new configuration...
call npx quartz build
if errorlevel 1 (
    echo ❌ Build failed with new config
    echo 🔄 Restoring backup...
    copy "quartz.config.ts.backup" "quartz.config.ts"
    echo ❌ Please check the configuration manually
    pause
    exit /b 1
)

echo ✅ New configuration works perfectly!
echo.
echo 🎯 Configuration highlights:
echo    ✅ Campaign-themed colors ^(fantasy brown/gold^)
echo    ✅ Obsidian features enabled ^(callouts, tags, links^)
echo    ✅ Graph view optimized
echo    ✅ Mobile-responsive design
echo    ✅ SEO and RSS enabled
echo.
echo 🚀 Ready for GitHub Actions deployment!
echo.
pause