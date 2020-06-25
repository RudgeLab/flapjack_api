from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter

from .consumers import RegistryConsumer
websockets = URLRouter([
    path(
        "upload", RegistryConsumer,
        name="registry-ws",
    ),
])
