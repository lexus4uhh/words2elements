# words2elements

Turn words into combinations of chemical element symbols.

Given an input word, this tool finds all possible ways to represent it as a sequence of periodic table element symbols, and shows each symbol along with its element name and atomic number. It comes with a simple Tkinter-based GUI.

## Short Description

A small GUI application that decomposes any word into all possible sequences of periodic table element symbols and displays each symbol with its corresponding element name and atomic number.

## Requirements

- Python 3.8+
- `mendeleev` (listed in `requirements.txt`)

## Installation

1. (Optional) Create and activate a virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the GUI application from the project root:

```bash
python gui.py
```

Then:

1. Enter a word into the input field.
2. Click the `transform` button.
3. View all possible combinations of element symbols representing your word.

If no valid decomposition exists, the app will display "No combinations found.".

## Project Structure

- `gui.py` – Tkinter-based GUI entry point for the application.
- `tool.py` – core logic for decomposing words into element symbols and enriching them with element data from `mendeleev`.
- `requirements.txt` – Python dependencies.
- `LICENSE` – project license (MIT).
- `README.md` – project documentation (this file).

## How it works

Core logic is implemented in `tool.py`:

- The `word2symbs(word)` function recursively searches for all ways to cover the word with valid element symbols.
- The `main(word)` function converts symbol sequences into descriptive strings using `mendeleev`, e.g. `H (Hydrogen, 1)`.
- The GUI in `gui.py` calls `main(word)` and shows all combinations in a scrollable text area.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
