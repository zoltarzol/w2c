from django.shortcuts import render
from requests import Session
import json
from . import forms

# Create your views here.
def api(request):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'YOUR_API_KEY'
    }
    session = Session()
    session.headers.update(headers)

    if request.method == 'POST':
        form = forms.ApiForm(request.POST)
        form.save()
        if form.is_valid():
            response = session.get(url, params=form.cleaned_data)
            info = json.loads(response.text)
            
            print(form.cleaned_data) # debug dans la console
            
            return render(
                request,
                'api_app/reponse_formulaire.html',
                context={
                    'form': form,
                    'info':info
                    }
            )
    else:
        form = forms.ApiForm()

    return render(
        request,
        'api_app/formulaire.html',
        context={'form': form}
    )
