import re

filename = input("Input filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
except FileNotFoundError:
    print(f"Unknown file with name {filename}")
else:
    change_pattern = re.compile(r"\S+@\S+(?:\.com|\.net)\b")
    changed_content = re.sub(change_pattern, "*@*", content)
    with open(filename, "a") as file:
        file.write("\n\nChanged text:\n")
        file.write(changed_content)
