"""Resource definitions for draft screenshots.

Version Added:
    6.0:
    This was moved from :py:mod:`rbtools.api.resource`.
"""

from __future__ import annotations

from rbtools.api.resource.base import (
    ItemResource,
    ListResource,
    resource_mimetype,
)
from rbtools.api.resource.mixins import ScreenshotUploadMixin


@resource_mimetype('application/vnd.reviewboard.org.draft-screenshot')
class DraftScreenshotItemResource(ItemResource):
    """Item resource for draft screenshots.

    Version Added:
        6.0
    """

    ######################
    # Instance variables #
    ######################

    #: The absolute URL of the screenshot file, for downloading purposes.
    absolute_url: str

    #: The screenshot's descriptive caption.
    caption: str

    #: The name of the screenshot file.
    filename: str

    #: The numeric ID of the screenshot.
    id: int

    #: The path of the screenshot's image file.
    #:
    #: This is relative to the configured media directory on the Review Board
    #: server.
    path: str

    #: The URL to the review UI for this screenshot
    review_url: str

    #: The URL of the screenshot's thumbnail file.
    #:
    #: If this is not an absolute URL, it is relative to the Review Board
    #: server URL.
    thumbnail_url: str

    #: The URL of the screenshot file.
    #:
    #: This is deprecated in favor of the ``absolute_url`` attribute.
    url: str


@resource_mimetype('application/vnd.reviewboard.org.draft-screenshots')
class DraftScreenshotListResource(ScreenshotUploadMixin,
                                  ListResource[DraftScreenshotItemResource]):
    """List resource for draft screenshots."""
