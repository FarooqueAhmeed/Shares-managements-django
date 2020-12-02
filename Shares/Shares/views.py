from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Shares
from .forms import SharesForm
from django.contrib import messages
from django.core.paginator import Paginator
from tradingview_ta import TA_Handler, Interval


tesla = TA_Handler()
tesla.set_symbol_as("TSLA")
tesla.set_exchange_as_crypto_or_stock("NASDAQ")
tesla.set_screener_as_stock("america")
tesla.set_interval_as(Interval.INTERVAL_1_DAY)
print(tesla.get_analysis().summary)
# Example output: {"RECOMMENDATION": "BUY", "BUY": 8, "NEUTRAL": 6, "SELL": 3}


@login_required
def index(request, message=messages):

        all_shares = Shares.objects.filter()
        paginator = Paginator(all_shares, 10)
        page = request.GET.get('pg')
        all_shares = paginator.get_page(page)
        return render(request, 'index.html', {'all_shares': all_shares })



@login_required
def add_shares(request):
    if not request.user.is_authenticated:
        return render(request, "login.html", {
                "message": "User not logged in."
            })
    if request.method == "POST":

        # Read UI parameters
        name = request.POST["name"]
        ticker = request.POST["ticker"]
        buy_price = request.POST["buy_price"]
        number_of_shares = request.POST["number_of_shares"]




        # Create listing
        response = Shares.objects.create(
            name=name,
            ticker=ticker,
            buy_price= buy_price,
            number_of_shares=number_of_shares,


        )




        # Return to home page
        message = "Successfully created share."
        return index(request,message=message)

    else:
        return render(request, "add.html")




def delete_share(request, share_id):
    share = Shares.objects.get(pk=share_id)
    share.delete()
    return redirect('index')


''' 
@login_required
def edit_share(request, share_id):
    if request.method == "POST":
        shares = Shares.objects.get(pk=share_id)
        form = EditSharesForm(request.POST or None, instance = shares)
        if form.is_valid():
            form.save()

        messages.success(request,("Task Edited!"))
        return redirect('index')
    else:
        share = Shares.objects.get(pk=share_id)
        return render(request, 'edit.html', {'share': share})

'''
