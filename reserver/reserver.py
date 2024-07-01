from serena_app.models import Product

class Reserver:
    def __init__(self, request):
        self.session = request.session
        
        
        reserver = self.session.get('session_key')
        
        #if the user is new
        if 'session_key' not in request.session:
            reserver = self.session['session_key'] = {}
            
    #Make sure is available on all pages of site
        self.reserver = reserver
        
    def add(self, product):
        product_id = str(product.id)
        #logic
        if product_id in self.reserver:
            pass
        else:
            self.reserver[product_id] = {'price': str(product.price)}
        
        self.session.modified = True
        
        
    def __len__(self):
        return len(self.reserver)
    
    def get_prods(self):
        product_ids = self.reserver.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products