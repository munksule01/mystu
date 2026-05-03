# File Organizer CLI Tool

A Python CLI tool that scans folders, organizes files by type, and logs all actions.

## Features

- 🔍 **Scans folders** recursively for all files
- 📁 **Organizes files** by type (images, documents, code, archives, videos, audio, other)
- 📝 **Logs actions** to both console and log file
- 🧪 **Dry run mode** to preview changes before moving files

## Installation

```bash
cd cli_tool
```

No external dependencies required - uses only Python standard library.

## Usage

### Basic usage
```bash
python main.py /path/to/folder
```

### Preview changes (dry run)
```bash
python main.py /path/to/folder --dry-run
```

### Specify custom log file
```bash
python main.py /path/to/folder --log-file my_log.log
```

## File Categories

- **images**: jpg, jpeg, png, gif, bmp, svg, webp
- **documents**: pdf, doc, docx, txt, xlsx, xls, ppt, pptx
- **code**: py, js, ts, java, cpp, c, h, css, html, json
- **archives**: zip, rar, 7z, tar, gz
- **videos**: mp4, avi, mkv, mov, flv, wmv
- **audio**: mp3, wav, flac, aac, m4a, wma
- **other**: any other file type
- **no_extension**: files without an extension

## Logging

Logs are saved to `organizer.log` by default and include:
- Timestamp of each action
- Files moved by category
- Directories created
- Summary statistics

## Example

```bash
python main.py C:\Users\it\Downloads
```

Output:
```
2026-05-01 10:30:45 - INFO - Starting file organization scan in: C:\Users\it\Downloads
2026-05-01 10:30:45 - INFO - Found 15 files to organize
2026-05-01 10:30:45 - INFO -   images: 5 file(s)
2026-05-01 10:30:45 - INFO -   documents: 3 file(s)
2026-05-01 10:30:45 - INFO -   code: 7 file(s)
...
```
