# words2elements

`words2elements` is a small Python script that tries to spell a word using symbols of the chemical elements.

Given an input word, it attempts to decompose it into one- or two-letter element symbols (for example, `H`, `He`, `Na`, `Cl`). It searches for all valid decompositions and prints them as Python lists.

## Requirements

- Python 3.8+ (should also work with most modern Python 3 versions)

## Installation

1. Make sure Python 3 is installed and available on your `PATH`.
2. Clone or download this repository.
3. Open a terminal in the project root directory.

## Usage

From the project root, run:

```bash
python main.py
```

Then type a word and press Enter. For example:

```text
$ python main.py
bacon
[['Ba', 'Co', 'N']]
```

Another example:

```text
$ python main.py
neon
[['Ne', 'O', 'N']]
```

If a word cannot be fully represented with element symbols, the script prints an empty list:

```text
$ python main.py
xyz
[]
```

## How it works

- All valid element symbols (1- and 2-letter, in lowercase) are stored in the `elements` list in `main.py`.
- The input word is converted to lowercase.
- A depth-first search walks through the word:
  - At each position it tries to match a 1- or 2-letter element symbol.
  - For every match, it recurses on the remaining substring.
  - This produces all possible decompositions of the word into element symbols.
- Successfully matched symbols are capitalized appropriately (first letter uppercase, second letter lowercase) and returned as lists of symbols, which are then printed.

## Notes

- The script reads a single word from standard input; there is no additional argument parsing.
- Output is intended for quick experimentation and fun with the periodic table, not for production use.

## Planned improvements

- Add a simple GUI.
- Better validation of unsuitable input strings (for example, strings with spaces or special characters).
- Improve the decomposition algorithm (for example, preferring certain decompositions or limiting the number of results for very long words).
