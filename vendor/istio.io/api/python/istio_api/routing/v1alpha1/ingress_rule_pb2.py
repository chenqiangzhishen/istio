# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: routing/v1alpha1/ingress_rule.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from routing.v1alpha1 import route_rule_pb2 as routing_dot_v1alpha1_dot_route__rule__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='routing/v1alpha1/ingress_rule.proto',
  package='istio.routing.v1alpha1',
  syntax='proto3',
  serialized_pb=_b('\n#routing/v1alpha1/ingress_rule.proto\x12\x16istio.routing.v1alpha1\x1a!routing/v1alpha1/route_rule.proto\"\x8e\x02\n\x0bIngressRule\x12\x0c\n\x04port\x18\x01 \x01(\x05\x12\x12\n\ntls_secret\x18\x02 \x01(\t\x12\x12\n\nprecedence\x18\x03 \x01(\x05\x12\x35\n\x05match\x18\x04 \x01(\x0b\x32&.istio.routing.v1alpha1.MatchCondition\x12\x39\n\x0b\x64\x65stination\x18\x05 \x01(\x0b\x32$.istio.routing.v1alpha1.IstioService\x12\x1a\n\x10\x64\x65stination_port\x18\x06 \x01(\x05H\x00\x12\x1f\n\x15\x64\x65stination_port_name\x18\x07 \x01(\tH\x00\x42\x1a\n\x18\x64\x65stination_service_portB\x1fZ\x1distio.io/api/routing/v1alpha1b\x06proto3')
  ,
  dependencies=[routing_dot_v1alpha1_dot_route__rule__pb2.DESCRIPTOR,])




_INGRESSRULE = _descriptor.Descriptor(
  name='IngressRule',
  full_name='istio.routing.v1alpha1.IngressRule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='port', full_name='istio.routing.v1alpha1.IngressRule.port', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tls_secret', full_name='istio.routing.v1alpha1.IngressRule.tls_secret', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='precedence', full_name='istio.routing.v1alpha1.IngressRule.precedence', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='match', full_name='istio.routing.v1alpha1.IngressRule.match', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destination', full_name='istio.routing.v1alpha1.IngressRule.destination', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destination_port', full_name='istio.routing.v1alpha1.IngressRule.destination_port', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destination_port_name', full_name='istio.routing.v1alpha1.IngressRule.destination_port_name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='destination_service_port', full_name='istio.routing.v1alpha1.IngressRule.destination_service_port',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=99,
  serialized_end=369,
)

_INGRESSRULE.fields_by_name['match'].message_type = routing_dot_v1alpha1_dot_route__rule__pb2._MATCHCONDITION
_INGRESSRULE.fields_by_name['destination'].message_type = routing_dot_v1alpha1_dot_route__rule__pb2._ISTIOSERVICE
_INGRESSRULE.oneofs_by_name['destination_service_port'].fields.append(
  _INGRESSRULE.fields_by_name['destination_port'])
_INGRESSRULE.fields_by_name['destination_port'].containing_oneof = _INGRESSRULE.oneofs_by_name['destination_service_port']
_INGRESSRULE.oneofs_by_name['destination_service_port'].fields.append(
  _INGRESSRULE.fields_by_name['destination_port_name'])
_INGRESSRULE.fields_by_name['destination_port_name'].containing_oneof = _INGRESSRULE.oneofs_by_name['destination_service_port']
DESCRIPTOR.message_types_by_name['IngressRule'] = _INGRESSRULE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IngressRule = _reflection.GeneratedProtocolMessageType('IngressRule', (_message.Message,), dict(
  DESCRIPTOR = _INGRESSRULE,
  __module__ = 'routing.v1alpha1.ingress_rule_pb2'
  # @@protoc_insertion_point(class_scope:istio.routing.v1alpha1.IngressRule)
  ))
_sym_db.RegisterMessage(IngressRule)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\035istio.io/api/routing/v1alpha1'))
# @@protoc_insertion_point(module_scope)
