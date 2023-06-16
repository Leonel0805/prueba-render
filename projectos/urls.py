#rest framework ya nos da las rutas de el crud basico para las url con router
from rest_framework import routers
from .api import ProjectoViewSet
router = routers.DefaultRouter()

#usamos ese router
#lo que hace es generar 4 rutas, GET POST PUT DELETE
router.register('api/projectos', ProjectoViewSet, 'projectos')

urlpatterns = router.urls