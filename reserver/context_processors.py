from .reserver import Reserver



def reserver(request):
    return{'reserver': Reserver(request)}