# AI Transcriber (Whisper Batch Transcription)

This project transcribes audio/video files in bulk using OpenAI Whisper and saves each transcript as a `.txt` file.

The script:
- Loads a Whisper model once.
- Scans a folder for supported audio/video formats.
- Auto-detects language (for example English and Swahili).
- Writes one transcript file per input file into a `transcripts/` folder.

## Supported Input Formats

- `.m4a`
- `.mp3`
- `.wav`
- `.mp4`
- `.ogg`
- `.flac`

## Prerequisites

1. Python 3.9+ (3.10 or 3.11 recommended)
2. `pip`
3. `ffmpeg` installed and available in your PATH

Whisper relies on `ffmpeg` to decode audio/video files.

## 1) Clone or Copy the Project

If using Git:

```bash
git clone <your-repo-url>
cd audio
```

If you received the folder directly, just open a terminal in the folder containing `main.py`.

## 2) Create and Activate a Virtual Environment

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows (PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## 3) Install Dependencies

```bash
pip install --upgrade pip
pip install openai-whisper
```

Note: `openai-whisper` will install PyTorch as a dependency.

## 4) Install ffmpeg

### Ubuntu / Debian

```bash
sudo apt update
sudo apt install -y ffmpeg
```

### Fedora

```bash
sudo dnf install -y ffmpeg
```

### Arch

```bash
sudo pacman -S ffmpeg
```

### macOS (Homebrew)

```bash
brew install ffmpeg
```

### Windows

Install from https://ffmpeg.org/download.html and ensure `ffmpeg` is in PATH.

You can verify:

```bash
ffmpeg -version
```

## 5) Add Audio Files

Put your audio/video files in the same folder as `main.py` (default behavior), or change the `AUDIO_FOLDER` value in the script.

## 6) Run the Transcriber

```bash
python main.py
```

## Configuration

Open `main.py` and edit these values:

- `MODEL_SIZE`: `tiny | base | small | medium | large`
- `AUDIO_FOLDER`: where input files are read from (default `.`)
- `OUTPUT_FOLDER`: where transcripts are written (default `transcripts`)
- `AUDIO_EXTENSIONS`: file extensions to scan

### Model Size Guidance

- `tiny` / `base`: fastest, lower accuracy
- `small`: balanced (default)
- `medium` / `large`: better accuracy, slower and heavier

## Output

The script creates `transcripts/` and writes one `.txt` file per input file.

Each transcript file includes:
- Original file name
- Detected language
- Model used
- Transcribed text

Example output file:

```text
File     : meeting1.m4a
Language : en
Model    : small
============================================================

Hello everyone, welcome to today's meeting...
```

## Troubleshooting

### `No audio files found`

- Make sure your files are inside the configured `AUDIO_FOLDER`.
- Confirm file extensions match `AUDIO_EXTENSIONS`.

### `ffmpeg` not found / decode errors

- Install `ffmpeg`.
- Confirm `ffmpeg -version` works in your terminal.

### Slow transcription

- Use a smaller model (`tiny`, `base`, or `small`).
- Transcribe fewer/lighter files at once.

### Out of memory

- Switch to a smaller model.
- Process files in smaller batches.

## Optional: Freeze Dependencies

If you want fully reproducible installs:

```bash
pip freeze > requirements.txt
```

Then others can install with:

```bash
pip install -r requirements.txt
```

## Quick Start (Linux/macOS)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install openai-whisper
sudo apt update && sudo apt install -y ffmpeg
python main.py
```
