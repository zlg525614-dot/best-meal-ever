"""Entry for the make.fun bounty "The Best Meal You Ever Had".

Writes one sentence (at most 200 characters) about the best meal I ever
had to /output/entry.txt. Deterministic: the same sentence every run.
"""

import os

SENTENCE = (
    "The best meal I ever had was my grandmother's twice-cooked pork, eaten "
    "standing at her iron wok in her Sichuan kitchen, chili-crisp edges still "
    "sizzling as she pretended not to watch me grin."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
