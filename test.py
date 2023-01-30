# import the Wikipedia corpus used for training
with open('wiki_corpus.txt') as f:
    corpus = f.readlines()
    print(corpus[:5])

# set the hyperparameter of vocabulary size
vocab_size = 1000

# create a BPE tokenizer object
MyBPE = BPE(corpus=corpus, vocab_size=vocab_size)

# train BPE tokenizer with Wikipedia corpus
MyBPE.train()

# tokenize the given text
text = "Love, hate, or feel meh about Harry Potter, it’s hard to argue that J.K. Rowling filled the books with intentional writing choices. From made up words to the meanings of names to the well-scripted first and last lines of each novel, Rowling wanted to the writing to match the intricate fantasy world she created for the now-iconic boy wizard. To examine a few of these choices, I’ll be taking a closer look at the first line of Harry Potter, as well as the last lines, from all of the Harry Potter novels."
print(f"\nBPE tokenization result of text\n'{text}'")
print(MyBPE.tokenize(text))