# Byte-Pair Encoding (BPE) (subword-based tokenization) algorithm implementaions from scratch with python

## Python implementations:  
- `BPE.py`:  Byte-Pair Encoding: Subword-based tokenization algorithm

## Training and inference:  
- `test.py`: test with a paragraph of text  

The vocabulary size, i.e. the base vocabulary size + the number of merges, is a hyperparameter to choose.

BPE tokenization result of text
'Love, hate, or feel meh about Harry Potter, it’s hard to argue that J.K. Rowling filled the books with intentional writing choices. From made up words to the meanings of names to the well-scripted first and last lines of each novel, Rowling wanted to the writing to match the intricate fantasy world she created for the now-iconic boy wizard. To examine a few of these choices, I’ll be taking a closer look at the first line of Harry Potter, as well as the last lines, from all of the Harry Potter novels.'

['L', 'ov', 'e', ',', 'h', 'ate', ',', 'or', 'fe', 'el', 'me', 'h', 'about', 'H', 'ar', 'ry', 'P', 'ot', 'ter', ',', 'it', '’', 's', 'h', 'ard', 'to', 'ar', 'g', 'ue', 'that', 'J', '.', 'K', '.', 'R', 'ow', 'l', 'ing', 'f', 'ill', 'ed', 'the', 'bo', 'ok', 's', 'with', 'int', 'ent', 'ional', 'writ', 'ing', 'cho', 'ic', 'es', '.', 'F', 'rom', 'made', 'up', 'w', 'ord', 's', 'to', 'the', 'me', 'an', 'ing', 's', 'of', 'n', 'ames', 'to', 'the', 'well', '-', 'sc', 'ri', 'pt', 'ed', 'first', 'and', 'l', 'ast', 'l', 'in', 'es', 'of', 'e', 'ach', 'n', 'ov', 'el', ',', 'R', 'ow', 'l', 'ing', 'w', 'ant', 'ed', 'to', 'the', 'writ', 'ing', 'to', 'm', 'at', 'ch', 'the', 'in', 'tr', 'ic', 'ate', 'f', 'ant', 'as', 'y', 'w', 'orld', 'she', 'cre', 'ated', 'for', 'the', 'n', 'ow', '-', 'ic', 'on', 'ic', 'bo', 'y', 'w', 'iz', 'ard', '.', 'T', 'o', 'ex', 'am', 'ine', 'a', 'f', 'ew', 'of', 'the', 'se', 'cho', 'ic', 'es', ',', 'I', '’', 'l', 'l', 'be', 't', 'ak', 'ing', 'a', 'c', 'lo', 'ser', 'lo', 'ok', 'at', 'the', 'first', 'l', 'ine', 'of', 'H', 'ar', 'ry', 'P', 'ot', 'ter', ',', 'as', 'well', 'as', 'the', 'l', 'ast', 'l', 'in', 'es', ',', 'from', 'all', 'of', 'the', 'H', 'ar', 'ry', 'P', 'ot', 'ter', 'n', 'ov', 'el', 's', '.']
