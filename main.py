"""Write an assembled vacation reply to the requested output directory."""

import os
from ooo.reply import build_reply


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    reply = build_reply()
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as entry_file:
        entry_file.write(reply)


if __name__ == "__main__":
    main()
