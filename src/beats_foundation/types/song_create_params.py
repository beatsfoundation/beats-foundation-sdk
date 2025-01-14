# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SongCreateParams"]


class SongCreateParams(TypedDict, total=False):
    prompt: Required[str]
    """Text prompt for song generation (max 200 characters)"""

    genre: str
    """Musical genre"""

    is_instrumental: Annotated[bool, PropertyInfo(alias="isInstrumental")]
    """Whether the song should be instrumental.

    If the song is instrumental, the lyrics will be ignored.
    """

    lyrics: str
    """Optional lyrics for the song.

    If not provided, the prompt will be used to generate lyrics.
    """

    mood: str
    """Mood of the song"""
