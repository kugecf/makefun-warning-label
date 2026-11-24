import os

# Set file creation permissions
os.umask(0o022)

# The chosen warning label line
LINE = "WARNING: Side effects include overconfidence, poor sleep decisions, and questionable fashion choices. User assumes all risks."

# Create output directory
os.makedirs("/output", exist_ok=True)

# Write the line to entry.txt
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

# Set file permissions
os.chmod("/output/entry.txt", 0o644)