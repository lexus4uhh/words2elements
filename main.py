elements = [
    "h", "he", "li", "be", "b", "c", "n", "o", "f", "ne",
    "na", "mg", "al", "si", "p", "s", "cl", "ar", "k", "ca",
    "sc", "ti", "v", "cr", "mn", "fe", "co", "ni", "cu", "zn",
    "ga", "ge", "as", "se", "br", "kr", "rb", "sr", "y", "zr",
    "nb", "mo", "tc", "ru", "rh", "pd", "ag", "cd", "in", "sn",
    "sb", "te", "i", "xe", "cs", "ba", "la", "ce", "pr", "nd",
    "pm", "sm", "eu", "gd", "tb", "dy", "ho", "er", "tm", "yb",
    "lu", "hf", "ta", "w", "re", "os", "ir", "pt", "au", "hg",
    "tl", "pb", "bi", "po", "at", "rn", "fr", "ra", "ac", "th",
    "pa", "u", "np", "pu", "am", "cm", "bk", "cf", "es", "fm",
    "md", "no", "lr", "rf", "db", "sg", "bh", "hs", "mt", "ds",
    "rg", "cn", "nh", "fl", "mc", "lv", "ts", "og"]

def main(word):
    word = word.lower()
    result = []
    i = 0
    N = len(word)
    if N == 0:
        return 'no emty strings!'
    while i < N:
        if i + 1 < N and word[i:i+2] in elements:
            result.append(word[i].upper() + word[i+1])
            i += 2
        elif word[i] in elements:
            result.append(word[i].upper())
            i += 1
        else:
            return f'couldn`t interpritate, symbol: {i + 1}'
    
    return result

try:
    elem_set = main(input())
except Exception as e:
    print(f'error: {e}')
    quit()

print(elem_set)