import os

from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
import django

from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django.setup()

from api.v1.urls import websocket_urlpatterns

django_asgi_app = get_asgi_application()


application = ProtocolTypeRouter(
    {
        'http': django_asgi_app,
        'websocket': AllowedHostsOriginValidator(URLRouter(websocket_urlpatterns)),
    }
)
