// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.27.1
// 	protoc        v3.19.1
// source: van.proto

package __

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type Request struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Name string `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	Age  int32  `protobuf:"varint,2,opt,name=age,proto3" json:"age,omitempty"`
}

func (x *Request) Reset() {
	*x = Request{}
	if protoimpl.UnsafeEnabled {
		mi := &file_van_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Request) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Request) ProtoMessage() {}

func (x *Request) ProtoReflect() protoreflect.Message {
	mi := &file_van_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Request.ProtoReflect.Descriptor instead.
func (*Request) Descriptor() ([]byte, []int) {
	return file_van_proto_rawDescGZIP(), []int{0}
}

func (x *Request) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *Request) GetAge() int32 {
	if x != nil {
		return x.Age
	}
	return 0
}

type Response struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Result string `protobuf:"bytes,1,opt,name=result,proto3" json:"result,omitempty"`
}

func (x *Response) Reset() {
	*x = Response{}
	if protoimpl.UnsafeEnabled {
		mi := &file_van_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Response) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Response) ProtoMessage() {}

func (x *Response) ProtoReflect() protoreflect.Message {
	mi := &file_van_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Response.ProtoReflect.Descriptor instead.
func (*Response) Descriptor() ([]byte, []int) {
	return file_van_proto_rawDescGZIP(), []int{1}
}

func (x *Response) GetResult() string {
	if x != nil {
		return x.Result
	}
	return ""
}

var File_van_proto protoreflect.FileDescriptor

var file_van_proto_rawDesc = []byte{
	0x0a, 0x09, 0x76, 0x61, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x2f, 0x0a, 0x07, 0x72,
	0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x01,
	0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x12, 0x10, 0x0a, 0x03, 0x61, 0x67,
	0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x05, 0x52, 0x03, 0x61, 0x67, 0x65, 0x22, 0x22, 0x0a, 0x08,
	0x72, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x16, 0x0a, 0x06, 0x72, 0x65, 0x73, 0x75,
	0x6c, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x06, 0x72, 0x65, 0x73, 0x75, 0x6c, 0x74,
	0x32, 0x53, 0x0a, 0x03, 0x56, 0x61, 0x6e, 0x12, 0x21, 0x0a, 0x08, 0x48, 0x65, 0x6c, 0x6c, 0x6f,
	0x56, 0x61, 0x6e, 0x12, 0x08, 0x2e, 0x72, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x09, 0x2e,
	0x72, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x00, 0x12, 0x29, 0x0a, 0x0e, 0x48, 0x65,
	0x6c, 0x6c, 0x6f, 0x53, 0x74, 0x72, 0x65, 0x61, 0x6d, 0x56, 0x61, 0x6e, 0x12, 0x08, 0x2e, 0x72,
	0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x09, 0x2e, 0x72, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73,
	0x65, 0x22, 0x00, 0x30, 0x01, 0x42, 0x03, 0x5a, 0x01, 0x2e, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x33,
}

var (
	file_van_proto_rawDescOnce sync.Once
	file_van_proto_rawDescData = file_van_proto_rawDesc
)

func file_van_proto_rawDescGZIP() []byte {
	file_van_proto_rawDescOnce.Do(func() {
		file_van_proto_rawDescData = protoimpl.X.CompressGZIP(file_van_proto_rawDescData)
	})
	return file_van_proto_rawDescData
}

var file_van_proto_msgTypes = make([]protoimpl.MessageInfo, 2)
var file_van_proto_goTypes = []interface{}{
	(*Request)(nil),  // 0: request
	(*Response)(nil), // 1: response
}
var file_van_proto_depIdxs = []int32{
	0, // 0: Van.HelloVan:input_type -> request
	0, // 1: Van.HelloStreamVan:input_type -> request
	1, // 2: Van.HelloVan:output_type -> response
	1, // 3: Van.HelloStreamVan:output_type -> response
	2, // [2:4] is the sub-list for method output_type
	0, // [0:2] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_van_proto_init() }
func file_van_proto_init() {
	if File_van_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_van_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Request); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_van_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Response); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_van_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   2,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_van_proto_goTypes,
		DependencyIndexes: file_van_proto_depIdxs,
		MessageInfos:      file_van_proto_msgTypes,
	}.Build()
	File_van_proto = out.File
	file_van_proto_rawDesc = nil
	file_van_proto_goTypes = nil
	file_van_proto_depIdxs = nil
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConnInterface

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion6

// VanClient is the client API for Van service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type VanClient interface {
	HelloVan(ctx context.Context, in *Request, opts ...grpc.CallOption) (*Response, error)
	HelloStreamVan(ctx context.Context, in *Request, opts ...grpc.CallOption) (Van_HelloStreamVanClient, error)
}

type vanClient struct {
	cc grpc.ClientConnInterface
}

func NewVanClient(cc grpc.ClientConnInterface) VanClient {
	return &vanClient{cc}
}

func (c *vanClient) HelloVan(ctx context.Context, in *Request, opts ...grpc.CallOption) (*Response, error) {
	out := new(Response)
	err := c.cc.Invoke(ctx, "/Van/HelloVan", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *vanClient) HelloStreamVan(ctx context.Context, in *Request, opts ...grpc.CallOption) (Van_HelloStreamVanClient, error) {
	stream, err := c.cc.NewStream(ctx, &_Van_serviceDesc.Streams[0], "/Van/HelloStreamVan", opts...)
	if err != nil {
		return nil, err
	}
	x := &vanHelloStreamVanClient{stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type Van_HelloStreamVanClient interface {
	Recv() (*Response, error)
	grpc.ClientStream
}

type vanHelloStreamVanClient struct {
	grpc.ClientStream
}

func (x *vanHelloStreamVanClient) Recv() (*Response, error) {
	m := new(Response)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

// VanServer is the server API for Van service.
type VanServer interface {
	HelloVan(context.Context, *Request) (*Response, error)
	HelloStreamVan(*Request, Van_HelloStreamVanServer) error
}

// UnimplementedVanServer can be embedded to have forward compatible implementations.
type UnimplementedVanServer struct {
}

func (*UnimplementedVanServer) HelloVan(context.Context, *Request) (*Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method HelloVan not implemented")
}
func (*UnimplementedVanServer) HelloStreamVan(*Request, Van_HelloStreamVanServer) error {
	return status.Errorf(codes.Unimplemented, "method HelloStreamVan not implemented")
}

func RegisterVanServer(s *grpc.Server, srv VanServer) {
	s.RegisterService(&_Van_serviceDesc, srv)
}

func _Van_HelloVan_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(VanServer).HelloVan(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/Van/HelloVan",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(VanServer).HelloVan(ctx, req.(*Request))
	}
	return interceptor(ctx, in, info, handler)
}

func _Van_HelloStreamVan_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(Request)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(VanServer).HelloStreamVan(m, &vanHelloStreamVanServer{stream})
}

type Van_HelloStreamVanServer interface {
	Send(*Response) error
	grpc.ServerStream
}

type vanHelloStreamVanServer struct {
	grpc.ServerStream
}

func (x *vanHelloStreamVanServer) Send(m *Response) error {
	return x.ServerStream.SendMsg(m)
}

var _Van_serviceDesc = grpc.ServiceDesc{
	ServiceName: "Van",
	HandlerType: (*VanServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "HelloVan",
			Handler:    _Van_HelloVan_Handler,
		},
	},
	Streams: []grpc.StreamDesc{
		{
			StreamName:    "HelloStreamVan",
			Handler:       _Van_HelloStreamVan_Handler,
			ServerStreams: true,
		},
	},
	Metadata: "van.proto",
}