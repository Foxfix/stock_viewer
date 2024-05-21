import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

st.title('Stock Price Viewer')
stock_symbol1 = st.text_input('Enter the symbol of the first stock (for example, AAPL for Apple)')
stock_symbol2 = st.text_input('Enter the symbol of another promotion (for example, MSFT for Microsoft)')

if stock_symbol1 and stock_symbol2:
    stock_data1 = yf.download(stock_symbol1, period='5y')
    stock_data2 = yf.download(stock_symbol2, period='5y')

    if not stock_data1.empty and not stock_data2.empty:
        st.write('Financial data for the first share', stock_data1.head())
        st.write('Financial data for another promotion', stock_data2.head())

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(stock_data1.index, stock_data1['Close'], label=f'Share price {stock_symbol1}')
        ax.plot(stock_data2.index, stock_data2['Close'], label=f'Share price {stock_symbol2}')
        ax.set_title('Share price chart')
        ax.set_xlabel('Date')
        ax.set_ylabel('Share price (USD)')
        ax.grid(True)
        ax.legend()

        st.pyplot(fig)
    else:
        st.error('No data found for the promotion symbols entered. ')
