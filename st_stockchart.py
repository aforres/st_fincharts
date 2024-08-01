import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objs as go


# Define a dictionary mapping stock names to their ticker symbols
stocks = {
    "ANZ Bank": "ANZ.AX",
    "BHP": "BHP.AX",
    "Commonwealth Bank": "CBA.AX",
    "Gold (CMX)": "GC=F",
    "National Australia Bank": "NAB.AX",
    "Oil Crude (CMX)": "CL=F",
    "Rio Tinto": "RIO.AX",
    "Silver (CMX)": "SI=F",
    "Telstra": "TLS.AX",
    "Woolworths": "WOW.AX"
}

# Page title and description
st.title('Interactive Financial Chart App')
st.write('Select a stock or commodity to view its chart:')

# Dropdown menu to select stock
selected_stock = st.selectbox('Select Instrument', list(stocks.keys()))

# Display the selected stock's name and symbol
st.write(f'Instrument selected: {selected_stock} ({stocks[selected_stock]})')

# Calculate date ranges for the last 5 years
end_date = datetime.now()
start_date = end_date - timedelta(days=5*365)  # Assuming 365 days per year

# Fetch historical data from Yahoo Finance
ticker_symbol = stocks[selected_stock]
stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Display the data
st.write(stock_data)

# Plot the data with customized x-axis date format
#import plotly.graph_objs as go

fig = go.Figure()
fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], mode='lines', name='Close'))

fig.update_layout(
    title=f'{selected_stock} Price',
    xaxis_title='Date',
    yaxis_title='Price',
    xaxis_tickformat='%b %y'  # Format x-axis ticks as Day Month Year (e.g., 01 Jan 20)
)

st.plotly_chart(fig)
