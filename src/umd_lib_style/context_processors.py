import importlib.metadata
from django.conf import settings


def app_info(_request):
    package_name = getattr(settings, 'PROJECT_PACKAGE_NAME', None)
    return {
        'application_name': getattr(settings, 'APPLICATION_NAME', 'App'),
        'application_version': importlib.metadata.version(package_name) if package_name is not None else '',
        'navigation_links': getattr(settings, 'NAVIGATION_LINKS', {}),
    }
