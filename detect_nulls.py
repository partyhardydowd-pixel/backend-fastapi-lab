import pathlib

root = pathlib.Path("app")

for path in root.rglob("*.py"):
    data = path.read_bytes()
    if b"\x00" in data:
        print("NULL BYTES IN:", path)
