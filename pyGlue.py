import re
import sys

import wordsegment as ws
from sacremoses import MosesTokenizer, MosesDetokenizer

punctuation = "[!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~]"


def unglue(line):
    """Unglues word function in both monolingual and bilingual corpus"""
    try:
        source_sentence, target_sentence = line.rstrip().split("\t")
    except:
        source_sentence = line
        target_sentence = []
        
    tokenized_source = mt.tokenize(source_sentence)
    word_counter = 0

    for word in tokenized_source:
        punctuation_matched = re.search(punctuation, word, re.IGNORECASE)

        # Punctuation
        if punctuation_matched:
            word_counter += 1
            continue
        # Out of vocabulary
        if word in ws.UNIGRAMS.keys():
            word_counter += 1
            continue
        
        if word not in target_sentence or target_sentence == []:
            segmented_words = ws.segment(word)
            if len(segmented_words) >= 2:
                segmented_words = restore_case(source_sentence, segmented_words)
                tokenized_source[word_counter] = " ".join(segmented_words)
            else:
                tokenized_source[word_counter] = word

        word_counter += 1

        detokenized_source = md.detokenize(tokenized_source)

    if target_sentence != []:
        result = detokenized_source + "\t" + target_sentence
    else:
        result = detokenized_source

    print(result.strip("\n"))


def restore_case(source, segmented_source):
    """Restore original case to segment words"""
    index = 0
    for s_word in segmented_source:
        matched = re.search("(" + s_word + ")", source, re.IGNORECASE)
        if matched:
            segmented_source[index] = matched.group(1)
        index += 1

        if len(segmented_source) == 0:
            return source
    return segmented_source


if __name__ == "__main__":
    # Initialize word segment object and tokenizer/detokenizer object
    ws.load()
    mt, md = MosesTokenizer(lang="en"), MosesDetokenizer(lang="en")

    for line in sys.stdin:
        unglue(line)