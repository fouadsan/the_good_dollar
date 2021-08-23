from .models import Departement

def get_context(request):
    departements = Departement.objects.all()

    context = {
        'departements': departements,
    }

    return context