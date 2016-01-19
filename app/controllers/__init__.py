import os

__all__ = []

for file in os.listdir('app/controllers'):
    if not file.startswith('__'):
        name, ext = file.split('.')
        __all__.append(name)
