from pathlib import Path

def read(filename: str) -> str:
    base = Path(__file__).resolve().parents[1]
    with open(f"{base}/{filename}", 'r') as file_content:
        return file_content.read()
