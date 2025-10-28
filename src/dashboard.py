import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📰 News Headlines Sentiment Dashboard")

df = pd.read_csv("output/sentiment_results.csv")

st.write("### Sentiment Distribution")
fig1 = px.histogram(df, x='sentiment', color='sentiment', title='Sentiment Distribution')
st.plotly_chart(fig1)

if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'])
    daily_sentiment = df.groupby(df['date'].dt.date)['sentiment'].value_counts().unstack().fillna(0)
    st.write("### Sentiment Over Time")
    fig2 = px.line(daily_sentiment, x=daily_sentiment.index, y=daily_sentiment.columns,
                   title='Sentiment Over Time')
    st.plotly_chart(fig2)
