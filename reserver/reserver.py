class Reserver:
    def __init__(self, request):
        self.session = request.session
        
        
        reserver = self.session.get('session_key')
        
        #if the user is new
        if 'session_key' not in request.session:
            reserver = self.session['session_key'] = {}
            
    #Make sure is available on all pages of site
        self.reserver = reserver