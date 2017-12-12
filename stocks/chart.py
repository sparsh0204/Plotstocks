from bokeh.charts import Bar, Scatter, BoxPlot, Histogram, output_file, show
from bokeh.sampledata.autompg import autompg as df
from bokeh.plotting import figure, output_file, show
from bokeh.resources import CDN
from bokeh.embed import components
import pandas as pd
import numpy as np


from math import pi

import pandas as pd

from bokeh.plotting import figure, show, output_file

#from bokeh.sampledata.stocks import MSFT


def datetime(x):
    return np.array(x, dtype=np.datetime64)
# prepare some data, a Pandas GroupBy object in this case
def create_chart(df,symbol,chart_type):
    if chart_type=="Line Graph":
        plot = line_chart(df, symbol)
    elif chart_type=="Scatter Plot":
        plot = scatter(df,xaxis,yaxis,xaxis+" vs "+yaxis)
    elif chart_type == "Bar Chat":
        plot = BoxPlotchart(df,xaxis,yaxis,xaxis+" vs "+yaxis)
    elif chart_type == "Candlesticks":
        plot = candlesticks_chart(df, symbol)
    else:
        pass
    return plot

def line_chart(df,symbol):

    p1 = figure(x_axis_type="datetime", title=symbol + " Stock Price Distribution")
    p1.grid.grid_line_alpha = 0.3
    p1.xaxis.axis_label = 'Date'
    p1.yaxis.axis_label = 'Price'

    #print(df['Open'].tolist())
    #print(df[['date']])
    #print(df['Open'].tolist())
    p1.line(datetime(df['Date'].dt.strftime('%Y-%m-%d').tolist()), df['Open'].tolist(), legend=symbol, line_width=2)
    p1.legend.location = "top_left"

    return p1

def candlesticks_chart(df, symbol):
#    print(df)
#    df = pd.DataFrame(MSFT)[:50]
#    df = pd.DataFrame(MSFT)[:50]
    df["Date"] = pd.to_datetime(df["Date"])

    mids = (df.Open + df.Close) / 2
    spans = abs(df.Close - df.Open)

    inc = df.Close > df.Open
    dec = df.Open > df.Close
    w = 12 * 60 * 60 * 1000  # half day in ms

    TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

    p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title=symbol + " Stock Price Distribution")
    p.xaxis.major_label_orientation = pi / 4
    p.grid.grid_line_alpha = 0.3

    p.segment(df.Date, df.High, df.Date, df.Low, color="black")
    p.rect(df.Date[inc], mids[inc], w, spans[inc], fill_color="#D5E1DD", line_color="black")
    p.rect(df.Date[dec], mids[dec], w, spans[dec], fill_color="#F2583E", line_color="black")
    return p
    #output_file("candlestick.html", title="candlestick.py example")

    #show(p)  # open a browser
#plot = figure(title= title , xlabel= 'X-Axis', ylabel= 'Y- Axis', plot_width =400, plot_height =400)
#plot.line(domain, y, legend= 'f(x)', line_width = 2)


# create a scatter chart
def lineplot(df,x_axis,y_axis,title):
    print(df[x_axis])
    plot = figure(title= title ,x_axis_type="datetime", x_axis_label=x_axis , y_axis_label= y_axis, plot_width =400, plot_height =400)
    #x=df[x_axis].values.tolist()
    #y=df[y_axis].values.tolist()
    plot.line(datetime(df[x_axis]), df[y_axis], line_width = 2)
    return plot

def scatter(df,x_axis,y_axis,title):
    plot = Scatter(df, x=x_axis, y=y_axis, color=x_axis,
            title=title,
            legend='top_right',
            xlabel=x_axis,
            ylabel=y_axis)
    return plot

def Bar(df,x_axis,y_axis,title):
    plot = Bar(df, label=x_axis, values=y_axis, title=title, color=x_axis)
#    script, div = components(plot)
    return plot

def BoxPlotchart(df,x_axis,y_axis,title):
    print(x_axis,y_axis,title)
    plot = BoxPlot(df, values=y_axis, label=x_axis, title=title, color=x_axis, xlabel= x_axis, outliers=True,
            ylabel= y_axis,  whisker_color=x_axis)
#    script, div = components(plot)
    return plot

def Histograms():
    plot = Histogram(df, values= value, color=value,
              title=title, legend='top_right')
#    script, div = components(plot)
    return plot

