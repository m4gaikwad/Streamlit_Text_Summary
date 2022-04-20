# Core pkgs
import streamlit as st
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
#import seaborn as sns



#Local Pkgs
import lex_rank_sum
import nltk_summarize
import evaluate
from chart import chart

def default_text():
    f = open('default_text.txt','r',encoding='utf-8')
    text = f.read()
    f.close()
    return text
    
def about():
    st.info("Created By :")
    st.success("Mayur Gaikwad")
def main():
    st.title("Summarizer App")
    menu = ["Home","About"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Home":
        st.subheader("Summarization")
       # with st.form(key='summarize'):
        raw_text = st.text_area("Paste Text Here",value = default_text())
        if st.button("Summarize"):
            with st.expander("Original Text"):
                st.write(raw_text)
            
            #layout
            c1,c2 = st.columns(2)
            with c1:
                with st.expander("LexRank Summary"):
                    lex_sum = lex_rank_sum.sumy_summarizer(raw_text,5)
                    st.write(lex_sum)
                    evaluate.evaluate_summary(lex_sum,raw_text)
                    #st.write(lex_eval)
                    chart(raw_text, lex_sum)
            
            with c2:
                with st.expander("NLTK Summmary"):
                    summarize = nltk_summarize.nltk_summarize(raw_text)
                    st.write(summarize)
                    evaluate.evaluate_summary(summarize,raw_text)
                    #st.write(nltk_eval)
                    chart(raw_text, summarize)
                    
                    
            
            
    else:
        st.subheader("About")
        about()
            

if __name__ == "__main__":
    main()