from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from bokeh.embed import components
from . import plotstockdata, stockdata


# Create your views here.



def index(request):
    if request.method=="GET":
        return render(request,'stocks/homepage.html')
    elif request.method=="POST":
        symbol = request.POST['symbol']
        print(symbol)
        return redirect(reverse('graph_view') + '?u=%s' % symbol)

    else:
        pass


def graph_view(request):
    symbol = request.GET.get('u', None)
    df = stockdata.get_stock_data(symbol)
    plot = plotstockdata.plot_graph(df,symbol)
    script, div = components(plot)
    #print(script,div)

    #return render(request,'stocks/view_graph.html',{'symbol':symbol,'script' : script , 'div' : div})
    return render(request,'stocks/graph_view.html',{'symbol':symbol,'script' : script , 'div' : div})


