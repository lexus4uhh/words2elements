# words2elements

`words2elements` is a small Python script that tries to write a word using symbols of the chemical elements.

Given an input word, it scans from left to right and splits it into one- or two-letter element symbols (e.g. `H`, `He`, `Na`, `Cl`). If the entire word can be represented using element symbols, it prints a list of those symbols; otherwise, it prints an error message explaining where it failed.

## Requirements

- Python 3.8+ (should also work with most modern Python 3 versions)

## Usage

From the project root, run:

```bash
python main.py
```

Then type a word and press Enter. For example:

```text
$ python main.py
bacon
['Ba', 'Co', 'N']
```

Another example:

```text
$ python main.py
neon
['Ne', 'O', 'N']
```

If a word cannot be fully represented with element symbols, you will see a message like:

```text
couldn`t interpritate, symbol: 3
```

## How it works

- All valid element symbols (1- and 2-letter, in lowercase) are stored in the `elements` list in `main.py`.
- Input is converted to lowercase.
- The script walks through the word:
  - It first tries to match a 2-letter symbol at the current position.
  - If that fails, it tries a 1-letter symbol.
  - If neither works, it stops and reports the position of the failing character.
- Successfully matched symbols are capitalized appropriately (first letter uppercase, second letter lowercase) and returned as a Python list.

## Notes

- The script reads a single word from standard input; there is no additional argument parsing.
- Output is intended for quick experimentation and fun with the periodic table, not for production use.
