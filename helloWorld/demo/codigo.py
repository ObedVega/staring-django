from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def registro(request):
    fname = request.GET.get('nombre', None)
    lname = request.GET.get('apellido', None)
    user = request.GET.get('usuario', None)
    #userType = request.GET.get('tipousuario', None)
    
    if fname == '':
        fullName = "Nombre Vacio"
    else:    
        fullName = fname +" "+ lname +" "+user
        print("resultado en el metodo: "+fullName)
    
    return HttpResponse(fullName)  