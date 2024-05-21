This Streamlit application allows users to compare historical stock prices of two companies. By entering the stock symbols, the application fetches the past 5 years of stock data using the yfinance library. It then visualizes the closing prices of both stocks on a single interactive line chart, created with Matplotlib.
Technologies Used

Streamlit: For building the interactive web application.

yfinance: To download historical stock price data.

Matplotlib: For creating line charts to visualize the stock prices.

This application makes it easy to analyze and compare stock performance over time with a user-friendly interface.

![Screenshot 2024-05-21 at 14 26 10](https://github.com/Foxfix/stock_viewer/assets/16303236/cbe57b57-c535-486c-b7bf-8adaffece1f7)

https://stockviewer.streamlit.app/

You can clone this project

   `pip install -r requirements.txt`

and run it with the command

  `streamlit run app.py`
