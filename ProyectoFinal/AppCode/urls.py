from django.urls import path
from AppCode import views
from AppCode.views import cursos
from django.contrib.auth.views import LogoutView


urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #este era nuestro primer view
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),

    #path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    path('apicursoFormulario', views.apiCursoFormulario, name="apiCursoFormulario"),
    path('buscar', views.buscar, name="Buscar"),
    path('mostrar', views.mostrar, name="Mostrar"),
    path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),

    #path('busquedaCamada', views.busquedaCamada, name="BusquedaCamada"),
    path('busqueda/', views.busqueda),
    path('leerProfesores', views.leerProfesores, name = "LeerProfesores"),
    path('eliminarProfesor/<profesor_nombre>/', views.eliminarProfesor, name="EliminarProfesor"),
    path('editarProfesor/<profesor_nombre>/', views.editarProfesor, name="EditarProfesor"),
    path('curso_list', views.CursoList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name= 'Detail'),
    path(r'^nuevo$', views.CursoCreacion.as_view, name= 'New'),
    path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name= 'Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name= 'Delete'),
    path('login', views.login_request, name='Login'),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppCode/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"), 
    path('agregarAvatar', views.agregarAvatar, name="agregarAvatar"), 
    path('postProfesor', views.postProfesor, name='postProfesor')




]

