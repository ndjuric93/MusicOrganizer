# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ServiceLocation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ServiceLocation.proto',
  package='micromusic',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15ServiceLocation.proto\x12\nmicromusic\"@\n\x0fServiceLocation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x0e\n\x06routes\x18\x03 \x03(\tb\x06proto3')
)




_SERVICELOCATION = _descriptor.Descriptor(
  name='ServiceLocation',
  full_name='micromusic.ServiceLocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='micromusic.ServiceLocation.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='micromusic.ServiceLocation.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='routes', full_name='micromusic.ServiceLocation.routes', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=37,
  serialized_end=101,
)

DESCRIPTOR.message_types_by_name['ServiceLocation'] = _SERVICELOCATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServiceLocation = _reflection.GeneratedProtocolMessageType('ServiceLocation', (_message.Message,), dict(
  DESCRIPTOR = _SERVICELOCATION,
  __module__ = 'ServiceLocation_pb2'
  # @@protoc_insertion_point(class_scope:micromusic.ServiceLocation)
  ))
_sym_db.RegisterMessage(ServiceLocation)


# @@protoc_insertion_point(module_scope)
