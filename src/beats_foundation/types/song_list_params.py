# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SongListParams"]


class SongListParams(TypedDict, total=False):
    limit: int
    """Number of items per page"""

    page: int
    """Page number for pagination"""
