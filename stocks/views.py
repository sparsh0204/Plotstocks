from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from bokeh.embed import components
from . import plotstockdata, stockdata
from . import chart


# Create your views here.



def index(request):
    if request.method=="GET":
        return render(request,'stocks/homepage.html')
    elif request.method=="POST":
        symbol = request.POST['symbol']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        chart_type = request.POST['chart_type']
        return redirect(reverse('graph_view') + '?smb=%s&sd=%s&ed=%s&ct=%s' % (symbol,start_date,end_date,chart_type))

    else:
        pass


def graph_view(request):
    end_date = request.GET.get('ed', None)
    start_date = request.GET.get('sd', None)
    symbol = request.GET.get('smb', None)
    chart_type = request.GET.get('ct', None)

    df = stockdata.get_stock_data(symbol, start_date, end_date)
#    plot = plotstockdata.plot_graph(df,symbol)
    plot = chart.create_chart(df, symbol, chart_type)
    script, div = components(plot)
    return render(request,'stocks/graph_view.html',{'symbol':symbol,'script' : script , 'div' : div})


