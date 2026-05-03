#!/usr/bin/env python3
"""
File Organizer CLI Tool
Scans a folder, organizes files by type, and logs actions.
"""

import argparse
import sys
from pathlib import Path
from file_organizer import FileOrganizer


def main():
    parser = argparse.ArgumentParser(
        description="Organize files in a directory by file type"
    )
    parser.add_argument(
        "path",
        type=str,
        help="Path to the directory to organize"
    )
    parser.add_argument(
        "--log-file",
        type=str,
        default="organizer.log",
        help="Path to log file (default: organizer.log)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without moving files"
    )

    args = parser.parse_args()

    # Validate path
    target_path = Path(args.path)
    if not target_path.exists():
        print(f"Error: Path '{args.path}' does not exist")
        sys.exit(1)

    if not target_path.is_dir():
        print(f"Error: Path '{args.path}' is not a directory")
        sys.exit(1)

    # Create organizer and run
    organizer = FileOrganizer(target_path, args.log_file)
    
    if args.dry_run:
        print("🔍 DRY RUN MODE - No files will be moved\n")
        organizer.scan(dry_run=True)
    else:
        organizer.scan(dry_run=False)


if __name__ == "__main__":
    main()
