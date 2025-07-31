# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- Skip dot-directories and README files during enumeration and todo building
  - Dot-directories (starting with `.`) are now excluded from file enumeration to avoid processing system/hidden directories
  - README files (README, README.md, README.txt) are now excluded from file enumeration as they typically don't contain todos or relevant content for processing
  - This improves performance and reduces noise in the output by focusing on actual content files
