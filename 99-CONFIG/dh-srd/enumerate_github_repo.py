#!/usr/bin/env python3
"""
GitHub Repository Enumerator and Task Queue Builder
Enumerates all files in the seansbox/daggerheart-srd repository and compares
with existing dh-*.md files to create a prioritized todo list.
"""

import requests
import json
import os
import re
from pathlib import Path
from typing import List, Dict, Any
from dataclasses import dataclass

@dataclass
class RepoFile:
    path: str
    type: str
    size: int
    download_url: str = ""

@dataclass
class TodoItem:
    source_path: str
    output_path: str
    status: str
    priority: int
    file_type: str
    size: int

class GitHubRepoEnumerator:
    def __init__(self, repo_owner: str, repo_name: str):
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.base_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"
        self.files: List[RepoFile] = []
        
    def get_repo_contents(self, path: str = "") -> List[Dict[str, Any]]:
        """Get contents of a repository path"""
        url = f"{self.base_url}/contents/{path}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    
    def enumerate_all_files(self, path: str = "") -> None:
        """Recursively enumerate all files in the repository"""
        print(f"Enumerating path: {path}")
        contents = self.get_repo_contents(path)
        
        for item in contents:
            if item['type'] == 'file':
                repo_file = RepoFile(
                    path=item['path'],
                    type=item['type'],
                    size=item['size'],
                    download_url=item.get('download_url', '')
                )
                self.files.append(repo_file)
                print(f"  File: {item['path']} ({item['size']} bytes)")
            elif item['type'] == 'dir':
                print(f"  Directory: {item['path']}")
                # Recursively process subdirectories
                self.enumerate_all_files(item['path'])
    
    def save_to_json(self, filename: str) -> None:
        """Save enumerated files to JSON"""
        data = [
            {
                'path': f.path,
                'type': f.type,
                'size': f.size,
                'download_url': f.download_url
            }
            for f in self.files
        ]
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        print(f"Saved {len(self.files)} files to {filename}")

class TaskQueueBuilder:
    def __init__(self, repo_files: List[RepoFile], vault_path: str):
        self.repo_files = repo_files
        self.vault_path = Path(vault_path)
        self.existing_files = self.find_existing_dh_files()
        
    def find_existing_dh_files(self) -> List[str]:
        """Find all existing dh-*.md files in the vault"""
        existing = []
        for file_path in self.vault_path.rglob("dh-*.md"):
            existing.append(str(file_path.relative_to(self.vault_path)))
        return existing
    
    def determine_priority(self, file_path: str, file_type: str) -> int:
        """Determine priority based on file path and type (1=highest, 5=lowest)"""
        path_lower = file_path.lower()
        
        # Priority 1: Core gameplay files
        if any(term in path_lower for term in [
            'contents/the basics', 'contents/core gameplay', 'contents/character creation',
            'contents/combat', 'contents/making moves', 'contents/attacking'
        ]):
            return 1
            
        # Priority 2: Classes, ancestries, and core mechanics
        if any(term in path_lower for term in [
            'classes/', 'ancestries/', 'contents/classes', 'contents/ancestries',
            'contents/stress', 'contents/conditions', 'contents/leveling'
        ]):
            return 2
            
        # Priority 3: Equipment, abilities, and spells
        if any(term in path_lower for term in [
            'abilities/', 'weapons/', 'armor/', 'contents/weapons', 'contents/armor',
            'domains/', 'contents/domains'
        ]):
            return 3
            
        # Priority 4: Adversaries, environments, and advanced content
        if any(term in path_lower for term in [
            'adversaries/', 'environments/', 'communities/', 'subclasses/',
            'contents/adversaries', 'contents/environments'
        ]):
            return 4
            
        # Priority 5: Everything else (build files, config, etc.)
        return 5
    
    def generate_output_path(self, repo_path: str) -> str:
        """Generate the output dh-*.md filename based on repo path"""
        # Convert repo path to a suitable filename
        path_parts = repo_path.replace('.md', '').split('/')
        
        # Remove common prefixes and clean up
        if path_parts[0] in ['contents', 'docs']:
            path_parts = path_parts[1:]
            
        # Join with hyphens and add dh- prefix
        clean_name = '-'.join(path_parts)
        clean_name = re.sub(r'[^a-zA-Z0-9\-_]', '-', clean_name)
        clean_name = re.sub(r'-+', '-', clean_name)  # Remove duplicate hyphens
        clean_name = clean_name.strip('-')
        
        return f"04-RESOURCES/dh-srd/dh-{clean_name}.md"
    
    def build_todo_list(self) -> List[TodoItem]:
        """Build the prioritized todo list"""
        todo_items = []
        
        # Only process markdown files from key directories
        relevant_files = [
            f for f in self.repo_files 
            if f.path.endswith('.md') and any(
                f.path.startswith(prefix) for prefix in [
                    'contents/', 'classes/', 'ancestries/', 'abilities/', 
                    'weapons/', 'armor/', 'adversaries/', 'environments/',
                    'communities/', 'domains/', 'subclasses/', 'consumables/',
                    'items/', 'frames/'
                ]
            )
        ]
        
        for repo_file in relevant_files:
            output_path = self.generate_output_path(repo_file.path)
            priority = self.determine_priority(repo_file.path, repo_file.type)
            
            # Check if file already exists
            status = "missing"
            full_output_path = self.vault_path / output_path
            if full_output_path.exists():
                status = "done"
            
            todo_item = TodoItem(
                source_path=repo_file.path,
                output_path=output_path,
                status=status,
                priority=priority,
                file_type=repo_file.type,
                size=repo_file.size
            )
            todo_items.append(todo_item)
        
        # Sort by priority, then by status (missing first), then by size (larger first)
        todo_items.sort(key=lambda x: (x.priority, x.status == "done", -x.size))
        
        return todo_items
    
    def save_todo_markdown(self, todo_items: List[TodoItem], filename: str) -> None:
        """Save todo list to a markdown file"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("# Task Queue: dh-srd Pull\n\n")
            f.write("| Priority | Status | Source Path | Output Path | File Type | Size |\n")
            f.write("|----------|--------|-------------|-------------|-----------|------|\n")
            for item in todo_items:
                f.write(f"| {item.priority} | {item.status} | {item.source_path} | {item.output_path} | {item.file_type} | {item.size} |\n")
        
        print(f"Saved {len(todo_items)} todo items to {filename}")
        
        # Print summary
        missing_count = sum(1 for item in todo_items if item.status == "missing")
        done_count = sum(1 for item in todo_items if item.status == "done")
        print(f"Summary: {missing_count} missing, {done_count} done")
    

def main():
    # Configuration
    repo_owner = "seansbox"
    repo_name = "daggerheart-srd"
    vault_path = "../.."  # Go up to vault root from 99-CONFIG/dh-srd
    
    print(f"Enumerating GitHub repository: {repo_owner}/{repo_name}")
    
    # Step 1: Enumerate repository contents
    enumerator = GitHubRepoEnumerator(repo_owner, repo_name)
    try:
        enumerator.enumerate_all_files()
    except requests.exceptions.RequestException as e:
        print(f"Error accessing GitHub API: {e}")
        return
    
    # Save full file list
    enumerator.save_to_json("github_repo_files.json")
    
    # Step 2: Build todo list
    print("\nBuilding prioritized todo list...")
    builder = TaskQueueBuilder(enumerator.files, vault_path)
    todo_items = builder.build_todo_list()
    
    # Save todo list
    builder.save_todo_markdown(todo_items, "dh-srd-pull-todo.md")
    
    print(f"\nTask completed successfully!")
    print(f"- Repository files enumerated: {len(enumerator.files)}")
    print(f"- Todo items generated: {len(todo_items)}")
    print(f"- Todo list saved to: dh-srd-pull-todo.md")

if __name__ == "__main__":
    main()

