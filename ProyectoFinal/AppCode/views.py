from django.shortcuts import render
from AppCode.models import *
from django.http import HttpResponse
from AppCode.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required




# Create your views here.

def curso(self):
    curso = Curso(nombre="Desarrollo web", camada="19881")
    curso.save()
    documentoDeTexto = f"---> Curso: {curso.nombre}   Camada: {curso.camada}"
    
    
  #  return HttpResponse(documentoDeTexto)

@login_required
def inicio(request):

    #avatares = Avatar.objects.filter(user=request.user.id)
    
    return render(request, 'AppCode/index.html')#{'url': avatares[0].imagen.url})

def cursos(request):
    
    return render(request, 'AppCode/cursos.html')

def profesores(request):

    if request.method == 'POST':
        
        miFormulario = ProfesorFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], 
                                email=informacion['email'], profesion=informacion['profesion'])

            profesor.save()

            return render(request, 'AppCode/index.html')
    
    else:
        
        miFormulario = ProfesorFormulario

    
    return render(request, 'AppCode/profesorFormulario.html', {'miFormulario': miFormulario})

def estudiantes(request):
    
    return render(request, 'AppCode/estudiantes.html')


def cursoFormulario(request):
      if request.method == 'POST':
      
            curso =  Curso(request.post['curso'],(request.post['camada']))
 
            curso.save()
 
            return render(request, "AppCoder/inicio.html")
 
      return render(request,"AppCoder/cursoFormulario.html")


def apiCursoFormulario(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso =  Curso(request.POST['curso'],(request.POST['camada']))
            curso.save()
            return render(request, "AppCode/index.html")
    else:
        miFormulario = CursoFormulario()
    return render(request, "AppCode/apiCursoFormulario.html", {"miFormulario": miFormulario})

def buscar(request):
    
    if request.method == 'POST':
        miFormulario = BuscaCursoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            cursos =  Curso.objects.filter(nombre__icontains=informacion["curso"])
            return render(request, "AppCode/lista.html", {"cursos": cursos})
        else:
            print("\n\nERROR IS_VALID FALSE\n\n")
    else:
        miFormulario= BuscaCursoFormulario()
    return render(request, "AppCode/apiCursoFormulario.html", {"miFormulario": miFormulario})

def mostrar(request):
    pass

def profesorFormulario(request):
    
    if request.method == 'POST':
        
        miFormulario = ProfesorFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid():
        
            informacion = miFormulario.cleaned_data
            profesor =  Profesor(nombre=informacion["nombre"], apellido=informacion['apellido'], mail=informacion['email'], profesion=informacion['profesion'])
            profesor.save()
            return render(request, "AppCode/index.html")
        
    else:
        miFormulario= ProfesorFormulario()
    return render(request, "AppCode/profesorFormulario.html", {"miFormulario": miFormulario})

def busquedaCamada(request):
    
    return render (request, "AppCode/busquedaCamada.html")

def busqueda(request):
    respuesta = f"Estoy buscando la camada n°: {respuesta.GET['camada']}"
    
    return HttpResponse(respuesta)

def leerProfesores(request):
    
    profesores = Profesor.objects.all() #trae todos los profesores

    contexto= {"profesores":profesores} 

    return render(request, "AppCode/leerProfesores.html",contexto)

def eliminarProfesor(request, profesor_nombre):
 
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()
 
    # vuelvo al menú
    profesores = Profesor.objects.all()  # trae todos los profesores
 
    contexto = {"profesores": profesores}
 
    return render(request, "AppCode/leerProfesores.html", contexto)

def editarProfesor(request, profesor_nombre):
 
    profesor = Profesor.objects.get(nombre=profesor_nombre)

    if request.method == 'POST':

        miFormulario = ProfesorFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']

            profesor.save()

            return render(request, 'AppCode/index.html')
    
    else:

        miFormulario = ProfesorFormulario(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido, 
                                                   'email': profesor.email, 'profesion': profesor.profesion})
    
    return render(request, 'AppCode/editarProfesor.html', {'miFormulario': miFormulario, 'profesor_nombre': profesor_nombre})
 

class CursoList(ListView):

    model = Curso
    template_name = 'AppCode/curso_list.html'

class CursoDetalle(DetailView):

    model = Curso
    template_name = 'AppCode/curso_detalle.html'

class CursoCreacion(CreateView):

    model = Curso
    success_url = 'AppCode/curso/list'
    fields = ['nombre', 'camada']

class CursoUpdate(UpdateView):

    model = Curso
    success_url = 'AppCode/curso/list'
    fields = ['nombre', 'camada']

class CursoDelete(DeleteView):

    model = Curso
    success_url = 'AppCode/curso/list'



def login_request(request):

    if request.method == 'POST':
        
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data['password']

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)

                return render(request, 'AppCode/index.html', {'mensaje': f'Bienvenido {usuario}'})
            
            else:

                return render(request, 'AppCode/index.html', {'mensaje': 'Error, datos incorrectos'})
        
        else:

            return render(request, 'AppCode/index.html', {'mensaje': 'Error, formulario errroneo'}) 
        
    form = AuthenticationForm

    return render(request, 'AppCode/login.html', {'form': form})

def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render (request, 'AppCode/index.html', {'mensaje': 'Usuario creado :)'})
        
    else:

        form = UserRegisterForm()

    return render (request, 'AppCode/register.html', {'form': form})

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "AppCode/index.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppCode/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})
 

def agregarAvatar(request):


    if request.method == 'POST':

        miFormulario = AvatarFormulario(request.POST,request.FILES)

        if miFormulario.is_valid():

            u = User.objects.get(username=request.user)

            #avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen'])

            #avatar.save()

            return render(request, "AppCode/index.html")

    else:

        miFormulario = AvatarFormulario()

    return render(request, "AppCode/agregarAvatar.html", {"miFormulario": miFormulario,})
 
def postProfesor(request):
    return render(request, 'AppCode/postProfesores.html')