# Text Obfuscator — Simple Encryption & Decryption (Python)

A lightweight Python script that obfuscates text by shifting characters and adding random 6-letter prefixes and suffixes. Intended for learning and light obfuscation — not cryptographic security.

## How it works
- Words of length **6 or less** are reversed.
- Words longer than 6:
  - Move the first character to the end.
  - Add a random 6-letter prefix and a random 6-letter suffix.
  - Example: `hello` → `elloh` → `AbcdefellohUVwXyz`

## Files
- `encrypt.py` — contains `Generate_Random`, `encrypt`, `encrypt_sentence`.
- `decrypt.py` — contains `decrypt`.

## Functions
- `Generate_Random(n)` — returns a random string of `n` ASCII letters.
- `encrypt(word)` — encrypts a single word according to the rules.
- `encrypt_sentence(sentence)` — encrypts each word in a sentence.
- `decrypt(text)` — decrypts a single encrypted word.

## Usage
Run encryption:
```bash
python encrypt.py
# Input: Hello world
# Output: Encrypted Text : AbcdefellohUVwXyz stuxyzorldPqRGHi (example)
