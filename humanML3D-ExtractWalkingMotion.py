import os
import shutil
import re  # Import regex for extracting numbers

# Define source and destination directories
SOURCE_FOLDER = "./texts"  # Change this to your actual folder
DEST_FOLDER = "./walking_texts"  # Change this to your filtered folder
OUTPUT_FILE = "./filtered_filenames.txt"  # Output filename list

# Ensure destination folder exists
os.makedirs(DEST_FOLDER, exist_ok=True)

# Walking motion-related keywords
WALKING_KEYWORDS = [
    "walk", "walking", "step", "stepping", "stride", "striding", "stroll", "pace",
    "march", "hike", "roam", "wander", "wandering", "tread", "footstep", "move forward",
    "casual walk", "brisk walk", "tiptoe", "shuffle", "ambling", "saunter", "trotting",
    "approach", "advancing", "proceeding", "move toward", "move away", "step forward",
    "step backward", "sidestep", "pivot step", "jog", "jogging", "run", "running",
    "skip", "hopping", "leap", "jumping", "lunge", "glide", "walk forward", "walk backward",
    "walk sideways", "walk in circles", "walk while looking", "walk while holding",
    "walk carrying", "walk while talking", "limping", "hobbling", "staggering",
    "take a step", "walk steadily", "walk cautiously", "stride confidently", "step and turn"
]


# Function to check if content contains walking-related words
def contains_walking_motion(content):
    content = content.lower()  # Convert to lowercase for case-insensitive matching
    return any(keyword in content for keyword in WALKING_KEYWORDS)


# List to store extracted filenames without ".txt"
matched_filenames = []

# Process each file in the source directory
for filename in os.listdir(SOURCE_FOLDER):
    if filename.endswith(".txt"):  # Only process text files
        filepath = os.path.join(SOURCE_FOLDER, filename)

        try:
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()

                # Check if file contains walking-related keywords
                if contains_walking_motion(content):
                    shutil.copy(filepath, os.path.join(DEST_FOLDER, filename))  # Copy file

                    # Remove only the ".txt" extension from the filename
                    filename_without_extension = os.path.splitext(filename)[0]
                    matched_filenames.append(filename_without_extension)  # Store filename without extension

                    print(f"✔ Copied: {filename}")  # Log progress

        except Exception as e:
            print(f"Error processing {filename}: {e}")

# Save extracted filenames to a text file (one per row)
if matched_filenames:
    with open(OUTPUT_FILE, "w", encoding="utf-8") as output:
        output.write("\n".join(matched_filenames))
    print(f"\nExtracted filenames saved to: {OUTPUT_FILE}")

print("\nFiltering process complete!")
