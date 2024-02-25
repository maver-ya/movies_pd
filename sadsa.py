import os

from django.conf import settings

if os.getenv('DJANGO_SETTINGS_MODULE'):
    settings.configure(os.getenv('DJANGO_SETTINGS_MODULE'))
else:
    raise RuntimeError(
        'Settings not configured. Define `DJANGO_SETTINGS_MODULE` or call `settings.configure()` before accessing '
        '`settings`!')

print(settings.DEBUG)  # example usage of settings after configuration
