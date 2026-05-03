"""
Core file organization logic
"""

import logging
from pathlib import Path
from collections import defaultdict
from datetime import datetime


class FileOrganizer:
    """Scans folders and organizes files by type"""

    def __init__(self, target_path: Path, log_file: str = "organizer.log"):
        self.target_path = Path(target_path)
        self.log_file = log_file
        self.files_moved = 0
        self.folders_created = 0

        # Setup logging
        self.logger = self._setup_logger()

    def _setup_logger(self) -> logging.Logger:
        """Configure logging"""
        logger = logging.getLogger("FileOrganizer")
        logger.setLevel(logging.INFO)

        # File handler
        fh = logging.FileHandler(self.log_file)
        fh.setLevel(logging.INFO)

        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # Formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

        return logger

    def _get_file_category(self, file_path: Path) -> str:
        """Determine file category by extension"""
        extension = file_path.suffix.lower().lstrip(".")

        if not extension:
            return "no_extension"

        # Common categories
        categories = {
            "images": ["jpg", "jpeg", "png", "gif", "bmp", "svg", "webp"],
            "documents": ["pdf", "doc", "docx", "txt", "xlsx", "xls", "ppt", "pptx"],
            "code": ["py", "js", "ts", "java", "cpp", "c", "h", "css", "html", "json"],
            "archives": ["zip", "rar", "7z", "tar", "gz"],
            "videos": ["mp4", "avi", "mkv", "mov", "flv", "wmv"],
            "audio": ["mp3", "wav", "flac", "aac", "m4a", "wma"],
        }

        for category, extensions in categories.items():
            if extension in extensions:
                return category

        return "other"

    def scan(self, dry_run: bool = False):
        """Scan and organize files"""
        self.logger.info(f"Starting file organization scan in: {self.target_path}")
        self.logger.info(f"Dry run mode: {dry_run}")

        # Group files by category
        files_by_category = defaultdict(list)

        # Scan directory
        for item in self.target_path.rglob("*"):
            if item.is_file() and not item.name.startswith("."):
                category = self._get_file_category(item)
                files_by_category[category].append(item)

        # Log findings
        total_files = sum(len(files) for files in files_by_category.values())
        self.logger.info(f"Found {total_files} files to organize")

        for category in sorted(files_by_category.keys()):
            files = files_by_category[category]
            self.logger.info(f"  {category}: {len(files)} file(s)")

        # Create directories and move files
        for category, files in files_by_category.items():
            category_path = self.target_path / category
            
            if not dry_run and not category_path.exists():
                category_path.mkdir(parents=True, exist_ok=True)
                self.logger.info(f"[CREATED] Directory: {category}")
                self.folders_created += 1

            for file_path in files:
                relative_path = file_path.relative_to(self.target_path)
                
                if file_path.parent != category_path:
                    if dry_run:
                        self.logger.info(f"[DRY RUN] Would move: {relative_path} -> {category}/")
                    else:
                        try:
                            file_path.rename(category_path / file_path.name)
                            self.logger.info(f"[MOVED] {relative_path} -> {category}/")
                            self.files_moved += 1
                        except Exception as e:
                            self.logger.error(f"[ERROR] Failed to move {relative_path}: {e}")

        # Summary
        self.logger.info("=" * 50)
        self.logger.info("Organization Summary:")
        self.logger.info(f"  Files moved: {self.files_moved}")
        self.logger.info(f"  Directories created: {self.folders_created}")
        self.logger.info("=" * 50)
