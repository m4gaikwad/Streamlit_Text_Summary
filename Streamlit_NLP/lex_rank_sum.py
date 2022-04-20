# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 14:46:06 2022

@author: Mayur
"""
#Summarization pkgs LEX RANK
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

def sumy_summarizer(raw_text,num=2):
    parser = PlaintextParser.from_string(raw_text, Tokenizer('english'))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document,num)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    
    return result

