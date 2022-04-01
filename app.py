from datetime import date
import yfinance as yf
import streamlit as st

st.write("# Stock Price App 💵")

ticker_code = st.text_input(
    "Enter ticker symbol Below", 'GOOGL', placeholder="Ticker symbol here")

date_from = st.date_input("Start")
date_to = st.date_input("End", value=date.today())

if ticker_code:
    tickerSymbol = ticker_code

else:
    st.error("An error occured")
    st.stop()

st.write("<br /><br />", unsafe_allow_html=True)

tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start=date_from, end=date_to)

if tickerDf.to_dict('list') == {'Open': [], 'High': [], 'Low': [], 'Close': [], 'Adj Close': [], 'Volume': []}:
          st.error("Please enter valid ticker symbol")
if date_from > date_to:
          st.error("Please enter valid timeline")
try:
    st.line_chart(tickerDf.Close)
    st.line_chart(tickerDf.Volume)
except:
          st.error("Internal Server Error")

st.write("""
<br />
<br />

---

<br />
<br />

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
##### a Aadityansha Patel production
""", unsafe_allow_html=True)