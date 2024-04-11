import importlib.metadata
from importlib import import_module
from typing import Any

from django.conf import settings
from django.http import HttpRequest


def app_info(request: HttpRequest) -> dict[str, Any]:
    package_name = getattr(settings, 'PROJECT_PACKAGE_NAME', None)

    navigation_links = getattr(settings, 'NAVIGATION_LINKS', {})
    if isinstance(navigation_links, str):
        # this is a fully-qualified name to a function to run to get the navigation links
        # this allows applications to customize the navigation links on a per-request basis
        module_name, function_name = navigation_links.rsplit('.', 1)
        module = import_module(module_name)
        function = getattr(module, function_name)
        navigation_links = function(request)

    return {
        'application_name': getattr(settings, 'APPLICATION_NAME', 'App'),
        'application_version': importlib.metadata.version(package_name) if package_name is not None else '',
        'navigation_links': navigation_links,
    }
