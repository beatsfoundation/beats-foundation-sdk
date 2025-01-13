# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import song_list_params, song_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.song import Song
from .._base_client import make_request_options
from ..types.song_list_response import SongListResponse

__all__ = ["SongsResource", "AsyncSongsResource"]


class SongsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SongsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beatsfoundation/beats-foundation-sdk#accessing-raw-response-data-eg-headers
        """
        return SongsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SongsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beatsfoundation/beats-foundation-sdk#with_streaming_response
        """
        return SongsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        prompt: str,
        creator_wallet_address: str | NotGiven = NOT_GIVEN,
        genre: str | NotGiven = NOT_GIVEN,
        is_instrumental: bool | NotGiven = NOT_GIVEN,
        lyrics: str | NotGiven = NOT_GIVEN,
        mood: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Generate a new AI song based on provided parameters.

        Rate limited to 2 calls per
        hour per API key.

        Args:
          prompt: Text prompt for song generation

          creator_wallet_address: Wallet address of the creator

          genre: Musical genre

          is_instrumental: Whether the song should be instrumental

          lyrics: Optional lyrics for the song

          mood: Mood of the song

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/songs",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "creator_wallet_address": creator_wallet_address,
                    "genre": genre,
                    "is_instrumental": is_instrumental,
                    "lyrics": lyrics,
                    "mood": mood,
                },
                song_create_params.SongCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Song:
        """
        Retrieve details of a specific song

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/songs/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Song,
        )

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SongListResponse:
        """
        Retrieve a paginated list of songs

        Args:
          limit: Number of items per page

          page: Page number for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/songs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    song_list_params.SongListParams,
                ),
            ),
            cast_to=SongListResponse,
        )


class AsyncSongsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSongsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beatsfoundation/beats-foundation-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSongsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSongsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beatsfoundation/beats-foundation-sdk#with_streaming_response
        """
        return AsyncSongsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        prompt: str,
        creator_wallet_address: str | NotGiven = NOT_GIVEN,
        genre: str | NotGiven = NOT_GIVEN,
        is_instrumental: bool | NotGiven = NOT_GIVEN,
        lyrics: str | NotGiven = NOT_GIVEN,
        mood: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Generate a new AI song based on provided parameters.

        Rate limited to 2 calls per
        hour per API key.

        Args:
          prompt: Text prompt for song generation

          creator_wallet_address: Wallet address of the creator

          genre: Musical genre

          is_instrumental: Whether the song should be instrumental

          lyrics: Optional lyrics for the song

          mood: Mood of the song

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/songs",
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "creator_wallet_address": creator_wallet_address,
                    "genre": genre,
                    "is_instrumental": is_instrumental,
                    "lyrics": lyrics,
                    "mood": mood,
                },
                song_create_params.SongCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Song:
        """
        Retrieve details of a specific song

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/songs/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Song,
        )

    async def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SongListResponse:
        """
        Retrieve a paginated list of songs

        Args:
          limit: Number of items per page

          page: Page number for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/songs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    song_list_params.SongListParams,
                ),
            ),
            cast_to=SongListResponse,
        )


class SongsResourceWithRawResponse:
    def __init__(self, songs: SongsResource) -> None:
        self._songs = songs

        self.create = to_raw_response_wrapper(
            songs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            songs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            songs.list,
        )


class AsyncSongsResourceWithRawResponse:
    def __init__(self, songs: AsyncSongsResource) -> None:
        self._songs = songs

        self.create = async_to_raw_response_wrapper(
            songs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            songs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            songs.list,
        )


class SongsResourceWithStreamingResponse:
    def __init__(self, songs: SongsResource) -> None:
        self._songs = songs

        self.create = to_streamed_response_wrapper(
            songs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            songs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            songs.list,
        )


class AsyncSongsResourceWithStreamingResponse:
    def __init__(self, songs: AsyncSongsResource) -> None:
        self._songs = songs

        self.create = async_to_streamed_response_wrapper(
            songs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            songs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            songs.list,
        )
