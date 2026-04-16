import whisper
import os
import glob

# ── Configuration ────────────────────────────────────────────────
MODEL_SIZE   = "small"        # tiny | base | small | medium | large
AUDIO_FOLDER = "."            # folder where your audio files live
OUTPUT_FOLDER = "transcripts" # folder where .txt files will be saved
AUDIO_EXTENSIONS = ("*.m4a", "*.mp3", "*.wav", "*.mp4", "*.ogg", "*.flac")
# ─────────────────────────────────────────────────────────────────

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Load model once (reused for all files)
print(f"Loading Whisper '{MODEL_SIZE}' model...")
model = whisper.load_model(MODEL_SIZE)

# Collect all audio files from the folder
audio_files = []
for ext in AUDIO_EXTENSIONS:
    audio_files.extend(glob.glob(os.path.join(AUDIO_FOLDER, ext)))

if not audio_files:
    print("No audio files found. Make sure your audio files are in the same folder.")
    exit()

print(f"\nFound {len(audio_files)} audio file(s). Starting transcription...\n")
print("=" * 60)

for i, audio_path in enumerate(sorted(audio_files), start=1):
    filename = os.path.basename(audio_path)
    name_without_ext = os.path.splitext(filename)[0]
    output_path = os.path.join(OUTPUT_FOLDER, f"{name_without_ext}.txt")

    print(f"[{i}/{len(audio_files)}] Transcribing: {filename}")

    try:
        # Transcribe — language=None lets Whisper auto-detect
        # English & Swahili segments will both be captured
        result = model.transcribe(
            audio_path,
            language=None,        # auto-detect (handles English + Swahili)
            task="transcribe",    # use "translate" to force output in English
            verbose=False
        )

        transcription = result["text"].strip()
        detected_lang = result.get("language", "unknown")

        # Save to .txt file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(f"File     : {filename}\n")
            f.write(f"Language : {detected_lang}\n")
            f.write(f"Model    : {MODEL_SIZE}\n")
            f.write("=" * 60 + "\n\n")
            f.write(transcription)

        print(f"    ✓ Detected language : {detected_lang}")
        print(f"    ✓ Saved to          : {output_path}\n")

    except Exception as e:
        print(f"    ✗ Error processing {filename}: {e}\n")

print("=" * 60)
print(f"Done! All transcripts saved to → '{OUTPUT_FOLDER}/' folder")
