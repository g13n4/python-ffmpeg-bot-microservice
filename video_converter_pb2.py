# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: video_converter.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15video_converter.proto\"`\n\tVideoInfo\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x15\n\rfile_encoding\x18\x02 \x01(\t\x12\x17\n\x0foutput_encoding\x18\x03 \x01(\t\x12\x10\n\x08video_id\x18\x04 \x01(\x03\"m\n\x0eVideoToConvert\x12\x1e\n\nvideo_info\x18\x01 \x01(\x0b\x32\n.VideoInfo\x12\x13\n\x0b\x63hunk_index\x18\x02 \x01(\x05\x12\x12\n\nlast_chuck\x18\x03 \x01(\x08\x12\x12\n\nvideo_feed\x18\x04 \x01(\x0c\"f\n\x0e\x43onvertedVideo\x12\x17\n\nvideo_feed\x18\x01 \x01(\x0cH\x00\x88\x01\x01\x12\x0e\n\x06sucess\x18\x02 \x01(\x08\x12\x12\n\x05\x65rror\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\r\n\x0b_video_feedB\x08\n\x06_error2F\n\x0eVideoConverter\x12\x34\n\x0c\x43onvertVideo\x12\x0f.VideoToConvert\x1a\x0f.ConvertedVideo(\x01\x30\x01\x42\x43ZAgithub.com/g13n4/go-ffmpeg-converter-microservice/video-converterb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'video_converter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZAgithub.com/g13n4/go-ffmpeg-converter-microservice/video-converter'
  _globals['_VIDEOINFO']._serialized_start=25
  _globals['_VIDEOINFO']._serialized_end=121
  _globals['_VIDEOTOCONVERT']._serialized_start=123
  _globals['_VIDEOTOCONVERT']._serialized_end=232
  _globals['_CONVERTEDVIDEO']._serialized_start=234
  _globals['_CONVERTEDVIDEO']._serialized_end=336
  _globals['_VIDEOCONVERTER']._serialized_start=338
  _globals['_VIDEOCONVERTER']._serialized_end=408
# @@protoc_insertion_point(module_scope)
