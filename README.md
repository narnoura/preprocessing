# preprocessing
Scripts to preprocess and tokenize text for sentiment analysis

# To clean tweets, run this script:

python clean_tweets.py <input_file> <output_file>

# To perform simple tokenization of the text, run this script:

perl tokenizer.perl -l <language_code> < <input_file> > <output_file>

e.g:

perl tokenizer.perl -l en < english_tweets.cleaned.txt > english_tweets.cleaned.tok.txt

If the language code is not accepted, it will default to English (this is fine).

NOTE that this script is taken from the Moses tokenizer; some punctuations have been added or excluded in order to deal with our data.
https://github.com/moses-smt/mosesdecoder/blob/master/scripts/tokenizer/tokenizer.perl
