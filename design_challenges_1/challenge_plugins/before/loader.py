from importlib import import_module
from factory import PaymentHandlerFn

def load_plugin(plugin_name: str) -> PaymentHandlerFn:
    return import_module(f'plugins.{plugin_name}') # type: ignore