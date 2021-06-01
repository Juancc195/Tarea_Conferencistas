from django.shortcuts import render
from django.http import HttpResponse

participantes =  [
            {
                'nombre':'Juan',
                'apellido':'Lopez',
                'correo':'juan@gmail.com',
                'twitter':'juan.lopez',
            },
            {
                'nombre':'Maria',
                'apellido':'Gomez',
                'correo':'maria@gmail.com',
                'twitter':'maria.gome',
            },
            {
                'nombre':'Karla',
                'apellido':'Herrera',
                'correo':'karla.herre@gmail.com',
                'twitter':'karla.herrera',
            },
            {
                'nombre':'Juan',
                'apellido':'Cruz',
                'correo':'Juan.cruz@gmail.com',
                'twitter':'juan.cru',
            },
        ]
    
# Create your views here.
def index(request):

    #clase 24/05
    #import pdb; pdb.set_trace()
    #nombre = request.GET.get("nombre")
    #apellido = request.GET.get("apellido")
    #edad = request.GET.get("edad")

    #return HttpResponse(f'Buenas noches {nombre} {}, su edad es {edad} años???')

    #clase 25/05
    #n = request.GET.get("name")

    # variable GET          :name
    # variable de Python    :n
    # variable de plantilla :x

    # Enviar valores a la plantilla a travez del contexto
    # el nombre que se le da a un diccionario que se pasa como tercer parametro eso es contexto

    #recibir por Get los parametros para calcular la cuota de un prestamo bancario
    # monto: m, Tasa: r, plazo: n
    #m = int(request.GET.get("m"))
    #r = int(request.GET.get("r"))
    #n = int(request.GET.get("n"))

    #paso 2: preparar los datos para suministrarlos a la formula
    #r = r / 100 / 12
    #n = n * 12
    # paso 3: aplicar la formula: C = (m*r)/(1-(1+r)** -n)

    #c = (m*r)/(1-(1+r)** -n)

    #ctx = {
    #    'cuota': c
    #}

    
    if request.method == "POST":
        # Aqui vendra la informacion del formulario
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        twitter = request.POST.get('twitter')

        participantes.append({
            'nombre':nombre,
            'apellido':apellido,
            'correo':correo,
            'twitter':twitter
        })
        ctx = {
            'participantes': participantes
        }

        #return HttpResponse("El participante ha sido registrado")
        return render(request, "registro/index.html", ctx)
    else:
        # El metodo GET
        # contexto que va para la plantilla
        ctx = {
            'participantes': participantes
        }
        return render(request, "registro/index.html", ctx)
    