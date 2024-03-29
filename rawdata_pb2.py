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
  package='pb',
  syntax='proto3',
  serialized_options=b'Z%github.com/v-rogg/xx_communication/pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rrawdata.proto\x12\x02pb\"\"\n\nCoordinate\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\"J\n\x10TransformRequest\x12&\n\x0erawCoordinates\x18\x01 \x03(\x0b\x32\x0e.pb.Coordinate\x12\x0e\n\x06radian\x18\x02 \x01(\x02\"C\n\x11TransformResponse\x12.\n\x16transformedCoordinates\x18\x01 \x03(\x0b\x32\x0e.pb.Coordinate\"F\n\x04Zone\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12-\n\x15zoneObjectCoordinates\x18\x02 \x03(\x0b\x32\x0e.pb.Coordinate\";\n\x04Scan\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\"\n\nscanPoints\x18\x02 \x03(\x0b\x32\x0e.pb.Coordinate\"a\n\x0cTrackRequest\x12\x17\n\x05zones\x18\x01 \x03(\x0b\x32\x08.pb.Zone\x12\x17\n\x05scans\x18\x02 \x03(\x0b\x32\x08.pb.Scan\x12\x0b\n\x03\x65ps\x18\x03 \x01(\x02\x12\x12\n\nminSamples\x18\x04 \x01(\x03\"0\n\rTrackResponse\x12\x1f\n\x07persons\x18\x01 \x03(\x0b\x32\x0e.pb.Coordinate2|\n\x07RawData\x12:\n\tTransform\x12\x14.pb.TransformRequest\x1a\x15.pb.TransformResponse\"\x00\x12\x35\n\x0cTrackPersons\x12\x10.pb.TrackRequest\x1a\x11.pb.TrackResponse\"\x00\x42\'Z%github.com/v-rogg/xx_communication/pbb\x06proto3'
)




_COORDINATE = _descriptor.Descriptor(
  name='Coordinate',
  full_name='pb.Coordinate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='pb.Coordinate.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='pb.Coordinate.y', index=1,
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
  serialized_start=21,
  serialized_end=55,
)


_TRANSFORMREQUEST = _descriptor.Descriptor(
  name='TransformRequest',
  full_name='pb.TransformRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rawCoordinates', full_name='pb.TransformRequest.rawCoordinates', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='radian', full_name='pb.TransformRequest.radian', index=1,
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
  serialized_start=57,
  serialized_end=131,
)


_TRANSFORMRESPONSE = _descriptor.Descriptor(
  name='TransformResponse',
  full_name='pb.TransformResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transformedCoordinates', full_name='pb.TransformResponse.transformedCoordinates', index=0,
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
  serialized_start=133,
  serialized_end=200,
)


_ZONE = _descriptor.Descriptor(
  name='Zone',
  full_name='pb.Zone',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='pb.Zone.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='zoneObjectCoordinates', full_name='pb.Zone.zoneObjectCoordinates', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=202,
  serialized_end=272,
)


_SCAN = _descriptor.Descriptor(
  name='Scan',
  full_name='pb.Scan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='pb.Scan.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scanPoints', full_name='pb.Scan.scanPoints', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=274,
  serialized_end=333,
)


_TRACKREQUEST = _descriptor.Descriptor(
  name='TrackRequest',
  full_name='pb.TrackRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='zones', full_name='pb.TrackRequest.zones', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scans', full_name='pb.TrackRequest.scans', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='eps', full_name='pb.TrackRequest.eps', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='minSamples', full_name='pb.TrackRequest.minSamples', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=335,
  serialized_end=432,
)


_TRACKRESPONSE = _descriptor.Descriptor(
  name='TrackResponse',
  full_name='pb.TrackResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='persons', full_name='pb.TrackResponse.persons', index=0,
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
  serialized_start=434,
  serialized_end=482,
)

_TRANSFORMREQUEST.fields_by_name['rawCoordinates'].message_type = _COORDINATE
_TRANSFORMRESPONSE.fields_by_name['transformedCoordinates'].message_type = _COORDINATE
_ZONE.fields_by_name['zoneObjectCoordinates'].message_type = _COORDINATE
_SCAN.fields_by_name['scanPoints'].message_type = _COORDINATE
_TRACKREQUEST.fields_by_name['zones'].message_type = _ZONE
_TRACKREQUEST.fields_by_name['scans'].message_type = _SCAN
_TRACKRESPONSE.fields_by_name['persons'].message_type = _COORDINATE
DESCRIPTOR.message_types_by_name['Coordinate'] = _COORDINATE
DESCRIPTOR.message_types_by_name['TransformRequest'] = _TRANSFORMREQUEST
DESCRIPTOR.message_types_by_name['TransformResponse'] = _TRANSFORMRESPONSE
DESCRIPTOR.message_types_by_name['Zone'] = _ZONE
DESCRIPTOR.message_types_by_name['Scan'] = _SCAN
DESCRIPTOR.message_types_by_name['TrackRequest'] = _TRACKREQUEST
DESCRIPTOR.message_types_by_name['TrackResponse'] = _TRACKRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Coordinate = _reflection.GeneratedProtocolMessageType('Coordinate', (_message.Message,), {
  'DESCRIPTOR' : _COORDINATE,
  '__module__' : 'rawdata_pb2'
  # @@protoc_insertion_point(class_scope:pb.Coordinate)
  })
_sym_db.RegisterMessage(Coordinate)

TransformRequest = _reflection.GeneratedProtocolMessageType('TransformRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMREQUEST,
  '__module__' : 'rawdata_pb2'
  # @@protoc_insertion_point(class_scope:pb.TransformRequest)
  })
_sym_db.RegisterMessage(TransformRequest)

TransformResponse = _reflection.GeneratedProtocolMessageType('TransformResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMRESPONSE,
  '__module__' : 'rawdata_pb2'
  # @@protoc_insertion_point(class_scope:pb.TransformResponse)
  })
_sym_db.RegisterMessage(TransformResponse)

Zone = _reflection.GeneratedProtocolMessageType('Zone', (_message.Message,), {
  'DESCRIPTOR' : _ZONE,
  '__module__' : 'rawdata_pb2'
  # @@protoc_insertion_point(class_scope:pb.Zone)
  })
_sym_db.RegisterMessage(Zone)

Scan = _reflection.GeneratedProtocolMessageType('Scan', (_message.Message,), {
  'DESCRIPTOR' : _SCAN,
  '__module__' : 'rawdata_pb2'
  # @@protoc_insertion_point(class_scope:pb.Scan)
  })
_sym_db.RegisterMessage(Scan)

TrackRequest = _reflection.GeneratedProtocolMessageType('TrackRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRACKREQUEST,
  '__module__' : 'rawdata_pb2'
  # @@protoc_insertion_point(class_scope:pb.TrackRequest)
  })
_sym_db.RegisterMessage(TrackRequest)

TrackResponse = _reflection.GeneratedProtocolMessageType('TrackResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRACKRESPONSE,
  '__module__' : 'rawdata_pb2'
  # @@protoc_insertion_point(class_scope:pb.TrackResponse)
  })
_sym_db.RegisterMessage(TrackResponse)


DESCRIPTOR._options = None

_RAWDATA = _descriptor.ServiceDescriptor(
  name='RawData',
  full_name='pb.RawData',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=484,
  serialized_end=608,
  methods=[
  _descriptor.MethodDescriptor(
    name='Transform',
    full_name='pb.RawData.Transform',
    index=0,
    containing_service=None,
    input_type=_TRANSFORMREQUEST,
    output_type=_TRANSFORMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TrackPersons',
    full_name='pb.RawData.TrackPersons',
    index=1,
    containing_service=None,
    input_type=_TRACKREQUEST,
    output_type=_TRACKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RAWDATA)

DESCRIPTOR.services_by_name['RawData'] = _RAWDATA

# @@protoc_insertion_point(module_scope)
