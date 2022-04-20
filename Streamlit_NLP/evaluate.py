# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 15:04:22 2022

@author: Mayur
"""
import streamlit as st
from rouge import Rouge

from nltk.translate.bleu_score import sentence_bleu
import pandas as pd

def evaluate_summary(summ,raw_txt):

    st.info('Score')
    eval_score = sentence_bleu(raw_txt,summ) # BLEU SCORE
    st.write(eval_score)
    
    # r = Rouge()
    # r_score = r.get_scores(summ,raw_txt)
    # st.write(r_score)                     # ROUGE Score