# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chatapp.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rchatapp.proto\"^\n\x07Request\x12\x0e\n\x06opcode\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x11\n\trecipient\x18\x03 \x01(\t\x12\x0f\n\x07message\x18\x04 \x01(\t\x12\r\n\x05regex\x18\x05 \x01(\t\"\x1c\n\x08Response\x12\x10\n\x08response\x18\x01 \x01(\t\"+\n\tResponses\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\r\n\x05\x65mpty\x18\x02 \x01(\x08\x32J\n\x07\x43hatApp\x12\x1d\n\x04Send\x12\x08.Request\x1a\t.Response\"\x00\x12 \n\x06Listen\x12\x08.Request\x1a\n.Responses\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chatapp_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUEST._serialized_start=17
  _REQUEST._serialized_end=111
  _RESPONSE._serialized_start=113
  _RESPONSE._serialized_end=141
  _RESPONSES._serialized_start=143
  _RESPONSES._serialized_end=186
  _CHATAPP._serialized_start=188
  _CHATAPP._serialized_end=262
# @@protoc_insertion_point(module_scope)
