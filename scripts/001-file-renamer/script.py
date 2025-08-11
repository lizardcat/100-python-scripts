from pathlib import Path

old_file_name = Path("./samples/dog_breeds.txt")
new_file_name = Path("./samples/canine_breeds.txt")

old_file_name.rename(new_file_name)