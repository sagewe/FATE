# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: psi-model-param.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='psi-model-param.proto',
  package='com.webank.ai.fate.core.mlmodel.buffer',
  syntax='proto3',
  serialized_options=_b('B\030BoostTreeModelParamProto'),
  serialized_pb=_b('\n\x15psi-model-param.proto\x12&com.webank.ai.fate.core.mlmodel.buffer\"k\n\nFeaturePsi\x12\x14\n\x0c\x66\x65\x61ture_name\x18\x01 \x01(\t\x12\x0b\n\x03psi\x18\x02 \x03(\x01\x12\x10\n\x08interval\x18\x03 \x03(\t\x12\x13\n\x0b\x65xpect_perc\x18\x04 \x03(\x01\x12\x13\n\x0b\x61\x63tual_perc\x18\x05 \x03(\x01\"\xe1\x01\n\nPsiSummary\x12W\n\x0btotal_score\x18\x01 \x03(\x0b\x32\x42.com.webank.ai.fate.core.mlmodel.buffer.PsiSummary.TotalScoreEntry\x12G\n\x0b\x66\x65\x61ture_psi\x18\x02 \x03(\x0b\x32\x32.com.webank.ai.fate.core.mlmodel.buffer.FeaturePsi\x1a\x31\n\x0fTotalScoreEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x42\x1a\x42\x18\x42oostTreeModelParamProtob\x06proto3')
)




_FEATUREPSI = _descriptor.Descriptor(
  name='FeaturePsi',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.FeaturePsi',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_name', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeaturePsi.feature_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='psi', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeaturePsi.psi', index=1,
      number=2, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interval', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeaturePsi.interval', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expect_perc', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeaturePsi.expect_perc', index=3,
      number=4, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actual_perc', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeaturePsi.actual_perc', index=4,
      number=5, type=1, cpp_type=5, label=3,
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
  serialized_start=65,
  serialized_end=172,
)


_PSISUMMARY_TOTALSCOREENTRY = _descriptor.Descriptor(
  name='TotalScoreEntry',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.PsiSummary.TotalScoreEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.webank.ai.fate.core.mlmodel.buffer.PsiSummary.TotalScoreEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.webank.ai.fate.core.mlmodel.buffer.PsiSummary.TotalScoreEntry.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=351,
  serialized_end=400,
)

_PSISUMMARY = _descriptor.Descriptor(
  name='PsiSummary',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.PsiSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total_score', full_name='com.webank.ai.fate.core.mlmodel.buffer.PsiSummary.total_score', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_psi', full_name='com.webank.ai.fate.core.mlmodel.buffer.PsiSummary.feature_psi', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PSISUMMARY_TOTALSCOREENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=175,
  serialized_end=400,
)

_PSISUMMARY_TOTALSCOREENTRY.containing_type = _PSISUMMARY
_PSISUMMARY.fields_by_name['total_score'].message_type = _PSISUMMARY_TOTALSCOREENTRY
_PSISUMMARY.fields_by_name['feature_psi'].message_type = _FEATUREPSI
DESCRIPTOR.message_types_by_name['FeaturePsi'] = _FEATUREPSI
DESCRIPTOR.message_types_by_name['PsiSummary'] = _PSISUMMARY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeaturePsi = _reflection.GeneratedProtocolMessageType('FeaturePsi', (_message.Message,), {
  'DESCRIPTOR' : _FEATUREPSI,
  '__module__' : 'psi_model_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.FeaturePsi)
  })
_sym_db.RegisterMessage(FeaturePsi)

PsiSummary = _reflection.GeneratedProtocolMessageType('PsiSummary', (_message.Message,), {

  'TotalScoreEntry' : _reflection.GeneratedProtocolMessageType('TotalScoreEntry', (_message.Message,), {
    'DESCRIPTOR' : _PSISUMMARY_TOTALSCOREENTRY,
    '__module__' : 'psi_model_param_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.PsiSummary.TotalScoreEntry)
    })
  ,
  'DESCRIPTOR' : _PSISUMMARY,
  '__module__' : 'psi_model_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.PsiSummary)
  })
_sym_db.RegisterMessage(PsiSummary)
_sym_db.RegisterMessage(PsiSummary.TotalScoreEntry)


DESCRIPTOR._options = None
_PSISUMMARY_TOTALSCOREENTRY._options = None
# @@protoc_insertion_point(module_scope)
