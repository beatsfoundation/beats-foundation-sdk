# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Song"]


class Song(BaseModel):
    id: Optional[str] = None

    audio_url: Optional[str] = None

    song_url: Optional[str] = None

    streams: Optional[int] = None

    title: Optional[str] = None

    upvote_count: Optional[int] = None

    username: Optional[str] = None
