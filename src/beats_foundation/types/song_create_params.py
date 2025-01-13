# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SongCreateParams"]


class SongCreateParams(TypedDict, total=False):
    prompt: Required[str]
    """Text prompt for song generation"""

    creator_wallet_address: Annotated[str, PropertyInfo(alias="creatorWalletAddress")]
    """Wallet address of the creator"""

    genre: str
    """Musical genre"""

    is_instrumental: Annotated[bool, PropertyInfo(alias="isInstrumental")]
    """Whether the song should be instrumental"""

    lyrics: str
    """Optional lyrics for the song"""

    mood: str
    """Mood of the song"""
