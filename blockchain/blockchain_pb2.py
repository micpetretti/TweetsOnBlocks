# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: blockchain.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='blockchain.proto',
  package='chain',
  syntax='proto2',
  serialized_pb=_b('\n\x10\x62lockchain.proto\x12\x05\x63hain\"\x94\x01\n\nBlockChain\x12\'\n\x06\x62locks\x18\x01 \x03(\x0b\x32\x17.chain.BlockChain.Block\x1a]\n\x05\x42lock\x12\r\n\x05index\x18\x01 \x02(\x05\x12\x15\n\rprevious_hash\x18\x02 \x02(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x02(\t\x12\x12\n\ntime_stamp\x18\x04 \x02(\t\x12\x0c\n\x04hash\x18\x05 \x02(\t')
)




_BLOCKCHAIN_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='chain.BlockChain.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='chain.BlockChain.Block.index', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='previous_hash', full_name='chain.BlockChain.Block.previous_hash', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='chain.BlockChain.Block.data', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_stamp', full_name='chain.BlockChain.Block.time_stamp', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hash', full_name='chain.BlockChain.Block.hash', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=176,
)

_BLOCKCHAIN = _descriptor.Descriptor(
  name='BlockChain',
  full_name='chain.BlockChain',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='blocks', full_name='chain.BlockChain.blocks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_BLOCKCHAIN_BLOCK, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=176,
)

_BLOCKCHAIN_BLOCK.containing_type = _BLOCKCHAIN
_BLOCKCHAIN.fields_by_name['blocks'].message_type = _BLOCKCHAIN_BLOCK
DESCRIPTOR.message_types_by_name['BlockChain'] = _BLOCKCHAIN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BlockChain = _reflection.GeneratedProtocolMessageType('BlockChain', (_message.Message,), dict(

  Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), dict(
    DESCRIPTOR = _BLOCKCHAIN_BLOCK,
    __module__ = 'blockchain_pb2'
    # @@protoc_insertion_point(class_scope:chain.BlockChain.Block)
    ))
  ,
  DESCRIPTOR = _BLOCKCHAIN,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:chain.BlockChain)
  ))
_sym_db.RegisterMessage(BlockChain)
_sym_db.RegisterMessage(BlockChain.Block)


# @@protoc_insertion_point(module_scope)