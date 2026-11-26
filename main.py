import os
import shutil

# The elevator speaks only through entry.txt, so this file stays a plain
# copier: it moves the line to the output folder and adds nothing of its
# own, keeping the joke exactly as written.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    dst = os.path.join(out_dir, "entry.txt")
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
