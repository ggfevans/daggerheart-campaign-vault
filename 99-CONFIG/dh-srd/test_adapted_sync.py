#!/usr/bin/env python3
"""
Test script for the adapted dh_sync.py to validate functionality
"""

import sys
from pathlib import Path
import tempfile
import os

# Add the current directory to the path so we can import dh_sync
sys.path.insert(0, str(Path(__file__).parent))

from dh_sync import DHSRDSyncer, SyncTask

def test_frontmatter_generation():
    """Test the frontmatter generation with various file types"""
    
    with tempfile.TemporaryDirectory() as temp_dir:
        syncer = DHSRDSyncer(vault_root=temp_dir)
        
        test_cases = [
            ("classes/Bard.md", "class"),
            ("abilities/Battle Cry.md", "ability"), 
            ("ancestries/Human.md", "ancestry"),
            ("weapons/Longsword.md", "weapon"),
            ("adversaries/Dragon.md", "adversary"),
            ("contents/Core Rules.md", "core-rules"),
        ]
        
        print("Testing frontmatter generation:")
        print("=" * 50)
        
        for source_path, expected_tag in test_cases:
            title = Path(source_path).stem.replace('-', ' ').replace('_', ' ')
            frontmatter = syncer.create_yaml_frontmatter(source_path, title)
            
            print(f"\nSource: {source_path}")
            print(f"Expected tag: {expected_tag}")
            print("Generated frontmatter:")
            print(frontmatter)
            
            # Validate expected tag is present
            if expected_tag in frontmatter:
                print("[OK] Expected tag found")
            else:
                print("[FAIL] Expected tag missing")
            
            # Validate required fields
            required_fields = ["title:", "tags:", "source_url:", "category:", "created:"]
            for field in required_fields:
                if field in frontmatter:
                    print(f"[OK] {field} present")
                else:
                    print(f"[FAIL] {field} missing")

def test_path_preservation():
    """Test that original paths are preserved"""
    
    with tempfile.TemporaryDirectory() as temp_dir:
        syncer = DHSRDSyncer(vault_root=temp_dir)
        
        test_paths = [
            "classes/Bard.md",
            "abilities/Battle Cry.md",
            "ancestries/Human.md",
            "weapons/Longsword.md"
        ]
        
        print("\n\nTesting path preservation:")
        print("=" * 50)
        
        for path in test_paths:
            preserved = syncer.preserve_original_path(path)
            print(f"Original: {path}")
            print(f"Preserved: {preserved}")
            
            if path == preserved:
                print("[OK] Path correctly preserved")
            else:
                print("[FAIL] Path modified unexpectedly")
            print()

def test_output_path_determination():
    """Test output path determination with preserved structure"""
    
    with tempfile.TemporaryDirectory() as temp_dir:
        syncer = DHSRDSyncer(vault_root=temp_dir)
        
        test_cases = [
            SyncTask(1, "missing", "classes/Bard.md", "", "md", 1000),
            SyncTask(1, "missing", "abilities/Battle Cry.md", "", "md", 500),
        ]
        
        print("\n\nTesting output path determination:")
        print("=" * 50)
        
        for task in test_cases:
            output_path = syncer.determine_output_path(task)
            expected = f"04-RESOURCES/daggerheart-srd/{task.source_path}"
            
            print(f"Source: {task.source_path}")
            print(f"Output: {output_path}")
            print(f"Expected to contain: {expected}")
            
            if expected in str(output_path):
                print("[OK] Output path correctly structured")
            else:
                print("[FAIL] Output path structure unexpected")
            print()

if __name__ == "__main__":
    print("Testing Adapted DH Sync Script")
    print("=" * 60)
    
    test_frontmatter_generation()
    test_path_preservation() 
    test_output_path_determination()
    
    print("\n" + "=" * 60)
    print("Testing completed!")