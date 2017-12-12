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
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']

#        print(symbol)
        data_list = []
        data_list.append(symbol)
        data_list.append(start_date)
        data_list.append(end_date)

        return graph_view(request, data_list)
#        return redirect(reverse('graph_view') + '?smb=%s' % symbol + '?sd=%s' % start_date + '?ed=%s' % end_date)

    else:
        pass


def graph_view(request,data_list):
#    symbol = request.GET.get('smb', None)
    symbol = data_list[0]
    start_date = data_list[1]
    end_date = data_list[2]
#    start_date = request.GET.get('sd', None)
#    end_date = request.GET.get('ed', None)
#    print(start_date)
#    print(end_date)
#    print(symbol)
    df = stockdata.get_stock_data(symbol, start_date, end_date)
    plot = plotstockdata.plot_graph(df,symbol)
    script, div = components(plot)
    #print(script,div)

    #return render(request,'stocks/view_graph.html',{'symbol':symbol,'script' : script , 'div' : div})
    return render(request,'stocks/graph_view.html',{'symbol':symbol,'script' : script , 'div' : div})


