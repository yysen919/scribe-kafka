
import time
import sys
import os
from py.scribe import scribe
from thrift.transport import TTransport, TSocket
from thrift.protocol import TBinaryProtocol

socket = TSocket.TSocket(host="123.126.53.109", port=1463)
transport = TTransport.TFramedTransport(socket)
protocol = TBinaryProtocol.TBinaryProtocol(trans=transport, strictRead=False, strictWrite=False)
client = scribe.Client(iprot=protocol, oprot=protocol)
transport.open()

pcateg="test"
message="mykafka"
log_entry=scribe.LogEntry(category=pcateg, message=message)
result = client.Log(messages=[log_entry])
print result
