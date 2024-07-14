from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoInfo(_message.Message):
    __slots__ = ("file_name", "file_encoding", "output_encoding", "video_id")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_ENCODING_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_ENCODING_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    file_encoding: str
    output_encoding: str
    video_id: int
    def __init__(self, file_name: _Optional[str] = ..., file_encoding: _Optional[str] = ..., output_encoding: _Optional[str] = ..., video_id: _Optional[int] = ...) -> None: ...

class VideoToConvert(_message.Message):
    __slots__ = ("video_info", "chunk_index", "last_chuck", "video_feed")
    VIDEO_INFO_FIELD_NUMBER: _ClassVar[int]
    CHUNK_INDEX_FIELD_NUMBER: _ClassVar[int]
    LAST_CHUCK_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FEED_FIELD_NUMBER: _ClassVar[int]
    video_info: VideoInfo
    chunk_index: int
    last_chuck: bool
    video_feed: bytes
    def __init__(self, video_info: _Optional[_Union[VideoInfo, _Mapping]] = ..., chunk_index: _Optional[int] = ..., last_chuck: bool = ..., video_feed: _Optional[bytes] = ...) -> None: ...

class ConvertedVideo(_message.Message):
    __slots__ = ("video_feed", "sucess", "error")
    VIDEO_FEED_FIELD_NUMBER: _ClassVar[int]
    SUCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    video_feed: bytes
    sucess: bool
    error: str
    def __init__(self, video_feed: _Optional[bytes] = ..., sucess: bool = ..., error: _Optional[str] = ...) -> None: ...
