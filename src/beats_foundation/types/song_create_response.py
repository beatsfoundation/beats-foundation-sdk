# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .song import Song
from .._models import BaseModel

__all__ = ["SongCreateResponse"]


class SongCreateResponse(BaseModel):
    song: Optional[Song] = None
