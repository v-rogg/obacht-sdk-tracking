# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rawdata.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rawdata.proto',
  package='protobuf',
  syntax='proto3',
  serialized_options=b'Z+github.com/v-rogg/xx_communication/protobuf',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rrawdata.proto\x12\x08protobuf\"\"\n\nCoordinate\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\"O\n\x10TransformRequest\x12+\n\rrawCoordinate\x18\x01 \x03(\x0b\x32\x14.protobuf.Coordinate\x12\x0e\n\x06radian\x18\x02 \x01(\x02\"F\n\x0fTransformAnswer\x12\x33\n\x15transformedCoordinate\x18\x01 \x03(\x0b\x32\x14.protobuf.Coordinate2O\n\x07RawData\x12\x44\n\tTransform\x12\x1a.protobuf.TransformRequest\x1a\x19.protobuf.TransformAnswer\"\x00\x42-Z+github.com/v-rogg/xx_communication/protobufb\x06proto3'
)




_COORDINATE = _descriptor.Descriptor(
  name='Coordinate',
  full_name='protobuf.Coordinate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='protobuf.Coordinate.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='protobuf.Coordinate.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=61,
)


_TRANSFORMREQUEST = _descriptor.Descriptor(
  name='TransformRequest',
  full_name='protobuf.TransformRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rawCoordinate', full_name='protobuf.TransformRequest.rawCoordinate', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='radian', full_name='protobuf.TransformRequest.radian', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=142,
)


_TRANSFORMANSWER = _descriptor.Descriptor(
  name='TransformAnswer',
  full_name='protobuf.TransformAnswer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transformedCoordinate', full_name='protobuf.TransformAnswer.transformedCoordinate', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=144,
  serialized_end=214,
)

_TRANSFORMREQUEST.fields_by_name['rawCoordinate'].message_type = _COORDINATE
_TRANSFORMANSWER.fields_by_name['transformedCoordinate'].message_type = _COORDINATE
DESCRIPTOR.message_types_by_name['Coordinate'] = _COORDINATE
DESCRIPTOR.message_types_by_name['TransformRequest'] = _TRANSFORMREQUEST
DESCRIPTOR.message_types_by_name['TransformAnswer'] = _TRANSFORMANSWER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Coordinate = _reflection.GeneratedProtocolMessageType('Coordinate', (_message.Message,), {
  'DESCRIPTOR' : _COORDINATE,
  '__module__' : 'rawdata_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.Coordinate)
  })
_sym_db.RegisterMessage(Coordinate)

TransformRequest = _reflection.GeneratedProtocolMessageType('TransformRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMREQUEST,
  '__module__' : 'rawdata_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.TransformRequest)
  })
_sym_db.RegisterMessage(TransformRequest)

TransformAnswer = _reflection.GeneratedProtocolMessageType('TransformAnswer', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMANSWER,
  '__module__' : 'rawdata_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.TransformAnswer)
  })
_sym_db.RegisterMessage(TransformAnswer)


DESCRIPTOR._options = None

_RAWDATA = _descriptor.ServiceDescriptor(
  name='RawData',
  full_name='protobuf.RawData',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=216,
  serialized_end=295,
  methods=[
  _descriptor.MethodDescriptor(
    name='Transform',
    full_name='protobuf.RawData.Transform',
    index=0,
    containing_service=None,
    input_type=_TRANSFORMREQUEST,
    output_type=_TRANSFORMANSWER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RAWDATA)

DESCRIPTOR.services_by_name['RawData'] = _RAWDATA

# @@protoc_insertion_point(module_scope)
