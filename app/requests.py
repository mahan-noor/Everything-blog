import urllib.request,json
from .models import Quote

base_url = None


def configure_request(app):

      base_url = app.config['QUOTE_BASE_URL']

def get_quotes():
    '''
    Function that gets the json response to our url request
    '''
    get_quotes_url = base_url.format()

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quotes_results = None

        if get_quotes_response["results"]:
           quotes_results_list = get_quotes_response["results"]
           quotes_results = process_results(quotes_results_list)

    return quotes_results








