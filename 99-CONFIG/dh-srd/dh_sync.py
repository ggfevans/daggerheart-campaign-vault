#!/usr/bin/env python3
"""
Daggerheart SRD Sync Automation
Reads todo.csv and automatically downloads, transforms, and saves GitHub files
with proper YAML front-matter and attribution.
"""

import csv
import requests
import os
import re
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from datetime import datetime
import json

@dataclass
class SyncTask:
    """Represents a single file sync task"""
    priority: int
    status: str
    source_path: str
    output_path: str
    file_type: str
    size: int

@dataclass
class SyncResult:
    """Represents the result of a sync operation"""
    success: bool
    output_path: str
    error_message: Optional[str] = None

class DHSRDSyncer:
    """Main class for syncing GitHub files to local dh-srd collection"""
    
    def __init__(self, repo_owner: str = "seansbox", repo_name: str = "daggerheart-srd", 
                 vault_root: str = ".", log_dir: str = "."):
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.base_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"
        self.vault_root = Path(vault_root)
        self.log_dir = Path(log_dir)
        self.target_dir = Path("04-RESOURCES/dh-srd")
        
        # Set up logging
        self.setup_logging()
        
    def setup_logging(self) -> None:
        """Configure logging to file and console"""
        log_file = self.log_dir / f"dh_sync_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        self.log_dir.mkdir(parents=True, exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file, encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"Starting DH-SRD sync session - Log file: {log_file}")
        
    
    def read_todo_markdown(self, md_path: str = "dh-srd-pull-todo.md") -> List[SyncTask]:
        """Read todo from markdown table format (fallback if CSV doesn't exist)"""
        md_file = Path(md_path)
        if not md_file.exists():
            self.logger.error(f"Todo markdown file not found: {md_path}")
            return []
            
        tasks = []
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
            # Find the table start (skip header and separator)
            table_start = None
            for i, line in enumerate(lines):
                if line.strip().startswith('|') and 'Priority' in line:
                    table_start = i + 2  # Skip header and separator
                    break
                    
            if table_start is None:
                self.logger.error("Could not find table in markdown file")
                return []
                
            # Parse table rows
            for line in lines[table_start:]:
                line = line.strip()
                if not line.startswith('|') or len(line) < 10:
                    continue
                    
                # Parse table row
                cols = [col.strip() for col in line.split('|')[1:-1]]  # Remove empty first/last
                if len(cols) >= 6:
                    try:
                        task = SyncTask(
                            priority=int(cols[0]),
                            status=cols[1],
                            source_path=cols[2],
                            output_path=cols[3],
                            file_type=cols[4],
                            size=int(cols[5])
                        )
                        tasks.append(task)
                    except (ValueError, IndexError) as e:
                        self.logger.warning(f"Skipping malformed row: {line} - {e}")
                        
            self.logger.info(f"Loaded {len(tasks)} tasks from markdown table")
            return tasks
            
        except Exception as e:
            self.logger.error(f"Error reading todo markdown: {e}")
            return []
    
    def download_raw_content(self, source_path: str) -> Optional[str]:
        """Download raw file content from GitHub"""
        raw_url = f"https://raw.githubusercontent.com/{self.repo_owner}/{self.repo_name}/main/{source_path}"
        
        try:
            response = requests.get(raw_url, timeout=30)
            response.raise_for_status()
            self.logger.debug(f"Downloaded {source_path} ({len(response.text)} chars)")
            return response.text
            
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to download {source_path}: {e}")
            return None
    
    def generate_slug(self, source_path: str) -> str:
        """Generate a dh-{slug} filename from the source path"""
        # Extract filename without extension
        filename = Path(source_path).stem
        
        # Split path and clean up
        path_parts = source_path.replace('.md', '').split('/')
        
        # Remove common prefixes
        if path_parts[0] in ['contents', 'docs']:
            path_parts = path_parts[1:]
        
        # Create slug from path parts
        if len(path_parts) > 1:
            # Include parent directory for context
            slug_parts = path_parts[-2:]  # Last 2 parts
        else:
            slug_parts = [filename]
            
        # Clean and join
        clean_parts = []
        for part in slug_parts:
            clean_part = re.sub(r'[^a-zA-Z0-9\-_\s]', '', part)
            clean_part = re.sub(r'\s+', '-', clean_part)
            clean_part = re.sub(r'-+', '-', clean_part)
            clean_part = clean_part.strip('-').lower()
            if clean_part:
                clean_parts.append(clean_part)
        
        slug = '-'.join(clean_parts)
        return f"dh-{slug}.md"
    
    def create_yaml_frontmatter(self, source_path: str, title: str = None) -> str:
        """Create YAML front-matter for the file"""
        if title is None:
            title = Path(source_path).stem.replace('-', ' ').replace('_', ' ').title()
        
        # Determine tags based on source path
        tags = ["daggerheart", "srd"]
        path_lower = source_path.lower()
        
        if "classes/" in path_lower:
            tags.append("class")
        elif "ancestries/" in path_lower:
            tags.append("ancestry")
        elif "abilities/" in path_lower:
            tags.append("ability")
        elif "weapons/" in path_lower:
            tags.append("weapon")
        elif "armor/" in path_lower:
            tags.append("armor")
        elif "domains/" in path_lower:
            tags.append("domain")
        elif "subclasses/" in path_lower:
            tags.append("subclass")
        elif "adversaries/" in path_lower:
            tags.append("adversary")
        elif "environments/" in path_lower:
            tags.append("environment")
        elif "contents/" in path_lower:
            tags.append("core-rules")
        
        source_url = f"https://github.com/{self.repo_owner}/{self.repo_name}/blob/main/{source_path}"
        
        frontmatter = f"""---
title: "{title}"
tags: {json.dumps(tags)}
source_url: "{source_url}"
license: "CC BY 4.0"
created: "{datetime.now().isoformat()}"
---

"""
        return frontmatter
    
    def create_attribution_block(self, source_path: str) -> str:
        """Create attribution block for the bottom of the file"""
        source_url = f"https://github.com/{self.repo_owner}/{self.repo_name}/blob/main/{source_path}"
        
        attribution = f"""

---

## Attribution

This content is from the [Daggerheart SRD]({source_url}) by [Darrington Press](https://darringtonpress.com/), licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

**Source:** `{source_path}`  
**Repository:** [{self.repo_owner}/{self.repo_name}](https://github.com/{self.repo_owner}/{self.repo_name})  
**Downloaded:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

"""
        return attribution
    
    def process_content(self, raw_content: str, source_path: str) -> str:
        """Process and clean up the raw markdown content"""
        # Basic cleanup - remove any existing front-matter if present
        content = raw_content
        
        # Remove existing YAML front-matter if it exists
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                content = parts[2].strip()
        
        # Clean up extra whitespace
        content = re.sub(r'\n{3,}', '\n\n', content)
        content = content.strip()
        
        return content
    
    def determine_output_path(self, task: SyncTask) -> Path:
        """Determine the full output path, creating subdirectories as needed"""
        # Use the output_path from the task, but ensure it's relative to vault root
        output_path = task.output_path
        
        # If it doesn't start with the target directory, prepend it
        if not output_path.startswith('04-RESOURCES/dh-srd/'):
            slug = self.generate_slug(task.source_path)
            output_path = f"04-RESOURCES/dh-srd/{slug}"
        
        full_path = self.vault_root / output_path
        
        # Create directory structure if needed
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        return full_path
    
    def sync_file(self, task: SyncTask) -> SyncResult:
        """Sync a single file from GitHub to local storage"""
        self.logger.info(f"Syncing: {task.source_path}")
        
        try:
            # Skip if already done (unless forcing)
            if task.status == "done":
                output_path = self.determine_output_path(task)
                if output_path.exists():
                    self.logger.info(f"Skipping {task.source_path} (already done)")
                    return SyncResult(success=True, output_path=str(output_path))
            
            # Download raw content
            raw_content = self.download_raw_content(task.source_path)
            if raw_content is None:
                return SyncResult(success=False, output_path="", 
                                error_message="Failed to download content")
            
            # Process content
            processed_content = self.process_content(raw_content, task.source_path)
            
            # Create components
            title = Path(task.source_path).stem.replace('-', ' ').replace('_', ' ')
            frontmatter = self.create_yaml_frontmatter(task.source_path, title)
            attribution = self.create_attribution_block(task.source_path)
            
            # Combine everything
            final_content = frontmatter + processed_content + attribution
            
            # Determine output path
            output_path = self.determine_output_path(task)
            
            # Write file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(final_content)
            
            self.logger.info(f"Successfully synced: {task.source_path} -> {output_path}")
            return SyncResult(success=True, output_path=str(output_path))
            
        except Exception as e:
            error_msg = f"Error syncing {task.source_path}: {e}"
            self.logger.error(error_msg)
            return SyncResult(success=False, output_path="", error_message=error_msg)
    
    def sync_all(self, todo_source: str = None, filter_status: List[str] = None, 
                 max_files: int = None) -> List[SyncResult]:
        """Sync all files from the todo list"""
        
        # Read from markdown todo file
        if todo_source and Path(todo_source).exists():
            tasks = self.read_todo_markdown(todo_source)
        else:
            # Use default markdown todo file
            tasks = self.read_todo_markdown()
        
        if not tasks:
            self.logger.error("No tasks found to sync")
            return []
        
        # Filter tasks if requested
        if filter_status:
            tasks = [task for task in tasks if task.status in filter_status]
            self.logger.info(f"Filtered to {len(tasks)} tasks with status: {filter_status}")
        
        # Limit number of files if requested
        if max_files:
            tasks = tasks[:max_files]
            self.logger.info(f"Limited to first {max_files} tasks")
        
        self.logger.info(f"Starting sync of {len(tasks)} files")
        
        results = []
        successful_files = []
        
        for i, task in enumerate(tasks, 1):
            self.logger.info(f"Processing {i}/{len(tasks)}: {task.source_path}")
            
            result = self.sync_file(task)
            results.append(result)
            
            if result.success:
                successful_files.append(result.output_path)
            
            # Progress update every 10 files
            if i % 10 == 0:
                success_count = sum(1 for r in results if r.success)
                self.logger.info(f"Progress: {i}/{len(tasks)} processed, {success_count} successful")
        
        # Final summary
        success_count = sum(1 for r in results if r.success)
        failure_count = len(results) - success_count
        
        self.logger.info(f"Sync completed: {success_count} successful, {failure_count} failed")
        
        # Log successful files for post-processing
        if successful_files:
            success_log = self.log_dir / f"successful_files_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(success_log, 'w', encoding='utf-8') as f:
                for file_path in successful_files:
                    f.write(f"{file_path}\n")
            self.logger.info(f"List of successful files saved to: {success_log}")
        
        return results
    
    def get_newly_written_files(self, results: List[SyncResult]) -> List[str]:
        """Extract list of newly written files for post-processing"""
        return [result.output_path for result in results if result.success]

def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Sync Daggerheart SRD files from GitHub")
    parser.add_argument("--todo", default=None, 
                       help="Path to todo markdown file")
    parser.add_argument("--status", nargs="+", default=["missing"], 
                       help="Filter by status (e.g., missing, done)")
    parser.add_argument("--max-files", type=int, default=None,
                       help="Maximum number of files to process")
    parser.add_argument("--vault-root", default="../..", 
                       help="Root directory of vault (default: ../.. from dh-srd)")
    parser.add_argument("--repo-owner", default="seansbox",
                       help="GitHub repository owner")
    parser.add_argument("--repo-name", default="daggerheart-srd",
                       help="GitHub repository name")
    
    args = parser.parse_args()
    
    # Create syncer
    syncer = DHSRDSyncer(
        repo_owner=args.repo_owner,
        repo_name=args.repo_name,
        vault_root=args.vault_root
    )
    
    # Run sync
    results = syncer.sync_all(
        todo_source=args.todo,
        filter_status=args.status,
        max_files=args.max_files
    )
    
    # Get newly written files
    new_files = syncer.get_newly_written_files(results)
    
    print(f"\nSync completed!")
    print(f"Successfully processed: {len(new_files)} files")
    print(f"Failed: {len(results) - len(new_files)} files")
    
    if new_files:
        print(f"\nNewly written files:")
        for file_path in new_files[:10]:  # Show first 10
            print(f"  - {file_path}")
        if len(new_files) > 10:
            print(f"  ... and {len(new_files) - 10} more")
    
    return new_files

if __name__ == "__main__":
    main()
