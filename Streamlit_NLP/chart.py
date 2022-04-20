# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 11:51:06 2022

@author: Mayur
"""
import matplotlib.pyplot as plt
import altair as alt
import streamlit as st
import pandas as pd


def chart(raw_text,summary):
    doc_len = {"Original":len(raw_text),
               "Summary":len(summary)}
    df = pd.DataFrame([doc_len])
    df = df.T
    df.reset_index(inplace=True)
    df.columns = ['Text','Words']
    #st.dataframe(df)
    # names = list(doc_len.keys())
    # values = list(doc_len.values())
    # plt.bar(range(len(doc_len)),values)
    # plt.xticks(ticks=names)
    # plt.show()
    c = alt.Chart(df).mark_bar().encode(x='Text',y='Words')
    st.altair_chart(c)