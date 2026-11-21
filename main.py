import os

TEXT = """
The evening sun casts a warm glow on the kitchen counter, where a single tea leaf steeps in a delicate china cup. In the silence, the world slows its pace.
"""

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w") as f:
        f.write(TEXT)
    print("Wrote entry.txt")

try:
    main()
except:
    print("Error")
exit(0)