from django.conf.urls import url

from . import views
# se coloca app_name porque en django puede muchos aplicaciones (app) y si en una vista hay 
# mucho detalle no sabria django cual es cual
app_name = 'denuncia'
urlpatterns = [
	#url(r'^$', views.index, name='index'),
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^$', views.AddView.as_view(), name='add'),
	url(r'^add/$', views.mostrar, name='mostrar'),
]
