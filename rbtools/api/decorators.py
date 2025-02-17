"""Decorators for API requests."""

from __future__ import annotations

from housekeeping import func_moved

from rbtools.api.resource.base import request_method
from rbtools.deprecation import RemovedInRBTools80Warning


@func_moved(RemovedInRBTools80Warning,
            request_method)
def request_method_decorator(f):
    """Wrap a method returned from a resource to capture HttpRequests.

    When a method which returns HttpRequests is called, it will
    pass the method and arguments off to the transport to be executed.

    This wrapping allows the transport to skim arguments off the top
    of the method call, and modify any return values (such as executing
    a returned HttpRequest).

    However, if called with the ``internal`` argument set to True,
    the method itself will be executed and the value returned as-is.
    Thus, any method calls embedded inside the code for another method
    should use the ``internal`` argument to access the expected value.
    """
    return request_method(f)
