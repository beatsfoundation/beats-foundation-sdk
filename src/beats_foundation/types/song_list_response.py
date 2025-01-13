# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .song import Song
from .._models import BaseModel

__all__ = ["SongListResponse", "Pagination"]


class Pagination(BaseModel):
    limit: Optional[int] = None

    page: Optional[int] = None

    total: Optional[int] = None

    total_pages: Optional[int] = FieldInfo(alias="totalPages", default=None)


class SongListResponse(BaseModel):
    pagination: Optional[Pagination] = None

    songs: Optional[List[Song]] = None
