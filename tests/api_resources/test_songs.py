# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beats_foundation import BeatsFoundation, AsyncBeatsFoundation
from beats_foundation.types import Song, SongListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSongs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: BeatsFoundation) -> None:
        song = client.songs.create(
            prompt="prompt",
        )
        assert_matches_type(object, song, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: BeatsFoundation) -> None:
        song = client.songs.create(
            prompt="prompt",
            creator_wallet_address="creatorWalletAddress",
            genre="genre",
            is_instrumental=True,
            lyrics="lyrics",
            mood="mood",
        )
        assert_matches_type(object, song, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: BeatsFoundation) -> None:
        response = client.songs.with_raw_response.create(
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        song = response.parse()
        assert_matches_type(object, song, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: BeatsFoundation) -> None:
        with client.songs.with_streaming_response.create(
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            song = response.parse()
            assert_matches_type(object, song, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: BeatsFoundation) -> None:
        song = client.songs.retrieve(
            "id",
        )
        assert_matches_type(Song, song, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: BeatsFoundation) -> None:
        response = client.songs.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        song = response.parse()
        assert_matches_type(Song, song, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: BeatsFoundation) -> None:
        with client.songs.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            song = response.parse()
            assert_matches_type(Song, song, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: BeatsFoundation) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.songs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: BeatsFoundation) -> None:
        song = client.songs.list()
        assert_matches_type(SongListResponse, song, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: BeatsFoundation) -> None:
        song = client.songs.list(
            limit=0,
            page=0,
        )
        assert_matches_type(SongListResponse, song, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: BeatsFoundation) -> None:
        response = client.songs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        song = response.parse()
        assert_matches_type(SongListResponse, song, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: BeatsFoundation) -> None:
        with client.songs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            song = response.parse()
            assert_matches_type(SongListResponse, song, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSongs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncBeatsFoundation) -> None:
        song = await async_client.songs.create(
            prompt="prompt",
        )
        assert_matches_type(object, song, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBeatsFoundation) -> None:
        song = await async_client.songs.create(
            prompt="prompt",
            creator_wallet_address="creatorWalletAddress",
            genre="genre",
            is_instrumental=True,
            lyrics="lyrics",
            mood="mood",
        )
        assert_matches_type(object, song, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBeatsFoundation) -> None:
        response = await async_client.songs.with_raw_response.create(
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        song = await response.parse()
        assert_matches_type(object, song, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBeatsFoundation) -> None:
        async with async_client.songs.with_streaming_response.create(
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            song = await response.parse()
            assert_matches_type(object, song, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBeatsFoundation) -> None:
        song = await async_client.songs.retrieve(
            "id",
        )
        assert_matches_type(Song, song, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBeatsFoundation) -> None:
        response = await async_client.songs.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        song = await response.parse()
        assert_matches_type(Song, song, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBeatsFoundation) -> None:
        async with async_client.songs.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            song = await response.parse()
            assert_matches_type(Song, song, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBeatsFoundation) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.songs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncBeatsFoundation) -> None:
        song = await async_client.songs.list()
        assert_matches_type(SongListResponse, song, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBeatsFoundation) -> None:
        song = await async_client.songs.list(
            limit=0,
            page=0,
        )
        assert_matches_type(SongListResponse, song, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBeatsFoundation) -> None:
        response = await async_client.songs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        song = await response.parse()
        assert_matches_type(SongListResponse, song, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBeatsFoundation) -> None:
        async with async_client.songs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            song = await response.parse()
            assert_matches_type(SongListResponse, song, path=["response"])

        assert cast(Any, response.is_closed) is True
