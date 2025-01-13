# Songs

Types:

```python
from beats_foundation.types import Song, SongCreateResponse, SongListResponse
```

Methods:

- <code title="post /api/songs">client.songs.<a href="./src/beats_foundation/resources/songs.py">create</a>(\*\*<a href="src/beats_foundation/types/song_create_params.py">params</a>) -> <a href="./src/beats_foundation/types/song_create_response.py">object</a></code>
- <code title="get /api/songs/{id}">client.songs.<a href="./src/beats_foundation/resources/songs.py">retrieve</a>(id) -> <a href="./src/beats_foundation/types/song.py">Song</a></code>
- <code title="get /api/songs">client.songs.<a href="./src/beats_foundation/resources/songs.py">list</a>(\*\*<a href="src/beats_foundation/types/song_list_params.py">params</a>) -> <a href="./src/beats_foundation/types/song_list_response.py">SongListResponse</a></code>
