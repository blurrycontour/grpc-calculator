# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calculator.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x63\x61lculator.proto\x12\ncalculator\"!\n\tCalcInput\x12\t\n\x01\x61\x18\x01 \x01(\x02\x12\t\n\x01\x62\x18\x02 \x01(\x02\"\x19\n\nCalcOutput\x12\x0b\n\x03out\x18\x01 \x01(\x02\x32}\n\nCalculator\x12\x34\n\x03\x41\x64\x64\x12\x15.calculator.CalcInput\x1a\x16.calculator.CalcOutput\x12\x39\n\x08Subtract\x12\x15.calculator.CalcInput\x1a\x16.calculator.CalcOutputb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'calculator_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CALCINPUT']._serialized_start=32
  _globals['_CALCINPUT']._serialized_end=65
  _globals['_CALCOUTPUT']._serialized_start=67
  _globals['_CALCOUTPUT']._serialized_end=92
  _globals['_CALCULATOR']._serialized_start=94
  _globals['_CALCULATOR']._serialized_end=219
# @@protoc_insertion_point(module_scope)