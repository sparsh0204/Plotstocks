import bokeh
import numpy as np
import pandas as pd
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
#from bokeh.sampledata.stocks import AAPL, GOOG, IBM, MSFT


def datetime(x):
    return np.array(x, dtype=np.datetime64)

def make_graph():

    p1 = figure(x_axis_type="datetime", title="Stock Closing Prices")
    p1.grid.grid_line_alpha=0.3
    p1.xaxis.axis_label = 'Date'
    p1.yaxis.axis_label = 'Price'

    p1.line(datetime(AAPL['date']), AAPL['adj_close'], legend='AAPL', line_width = 2)
# p1.line(datetime(GOOG['date']), GOOG['adj_close'], color='#B2DF8A', legend='GOOG')
# p1.line(datetime(IBM['date']), IBM['adj_close'], color='#33A02C', legend='IBM')
# p1.line(datetime(MSFT['date']), MSFT['adj_close'], color='#FB9A99', legend='MSFT')
    p1.legend.location = "top_left"
    print(AAPL['date'])
    print(AAPL['adj_close'])
    #show(gridplot([[p1]], plot_width=400, plot_height=400))  # open a browser
    return p1

# aapl = np.array(AAPL['adj_close'])
# aapl_dates = np.array(AAPL['date'], dtype=np.datetime64)
#
# window_size = 30
# window = np.ones(window_size)/float(window_size)
# aapl_avg = np.convolve(aapl, window, 'same')
#
# p2 = figure(x_axis_type="datetime", title="AAPL One-Month Average")
# p2.grid.grid_line_alpha = 0
# p2.xaxis.axis_label = 'Date'
# p2.yaxis.axis_label = 'Price'
# p2.ygrid.band_fill_color = "olive"
# p2.ygrid.band_fill_alpha = 0.1
#
# p2.circle(aapl_dates, aapl, size=4, legend='close',
#           color='darkgrey', alpha=0.2)
#
# p2.line(aapl_dates, aapl_avg, legend='avg', color='navy')
# p2.legend.location = "top_left"

# output_file("stocks.html", title="stocks.py example")
#
# show(gridplot([[p1,p2]], plot_width=400, plot_height=400))  # open a browser
#make_graph()
def plot_graph(df,symbol):
    p1 = figure(x_axis_type="datetime", title="Stock Opening Prices")
    p1.grid.grid_line_alpha = 0.3
    p1.xaxis.axis_label = 'Date'
    p1.yaxis.axis_label = 'Price'

    #print(df['Open'].tolist())
    #print(df[['date']])
    #print(df['Open'].tolist())
    p1.line(datetime(df['Date'].dt.strftime('%Y-%m-%d').tolist()), df['Open'].tolist(), legend=symbol, line_width=2)
    p1.legend.location = "top_left"

    return p1