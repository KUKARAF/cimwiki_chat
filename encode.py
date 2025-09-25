from memvid import MemvidEncoder
import os

encoder = MemvidEncoder()

# Recursively index all markdown files
for root, _, files in os.walk("~/vimwiki"):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    encoder.add_text(f.read(), metadata={"file": file_path})
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

encoder.build_video("docs.mp4", "index.json")
