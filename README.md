# preprocessing
Scripts to preprocess and tokenize text for sentiment analysis

# To clean tweets, run this script:

python clean_tweets.py <input_file> <output_file>

# To perform simple tokenization of the text, run this script:

perl tokenizer.perl -l <language_code> < <input_file> > <output_file>

e.g:

perl tokenizer.perl -l en < english_tweets.cleaned.txt > english_tweets.cleaned.tok.txt
