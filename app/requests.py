import requests,json
from .models import Quote

# Getting the quote base url
base_url=None

def configure_request(app):
    global base_url
    base_url = app.config['BASE_URL']
    
def getQuotes(): 
    # request.urlopen(base_url):
        
        find = requests.get(base_url).json()
       
        v=[]
        id = find.get('id')
        author = find.get('author')
        quote = find.get('quote')

        quoteObject = Quote(id,author,quote)
        v.append(quoteObject)
        return v