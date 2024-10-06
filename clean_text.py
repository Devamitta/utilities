# Clean txt from any quotations

import re
import sys

# Get the file path from command-line arguments
file_path = sys.argv[1]

# Read the content of the file
with open(file_path, "r") as file:
    content = file.read()

# Remove all variations of quotations
content = re.sub(r'["\'`“”‘’´’-]', '', content)

# # Remove extra spaces
# content = re.sub(r'\s+', ' ', content)

# Write the modified content back to the file
with open(file_path, "w") as file:
    file.write(content)

print(f"Quotations removed from {file_path}")