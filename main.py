import os

TEXT = "My wireless earbuds die mid-sentence every single day, always on the one word that mattered, then reconnect a second later just in time for me to hear my boss say, 'Sorry - what was that?'"

# One-line roast of the wireless earbuds I use every day.
def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
