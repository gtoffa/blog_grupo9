import threading
from django.utils.deprecation import MiddlewareMixin
# Creamos un objeto local enhebrado para almacenar el usuario actual
_thread_locals = threading.local()


def get_current_user():
    return getattr(_thread_locals, 'user', None)

class CurrentUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Obtener el usuario actual desde el objeto de solicitud
        user = getattr(request, 'user', None)

        # Almacenar el usuario en la instancia de solicitud
        _thread_locals.user = getattr( request, 'user', None )
    
 
 