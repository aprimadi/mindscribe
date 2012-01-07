import sys
import json
sys.path.append('./gen-py')

from mindscribe import Mindscribe
from mindscribe.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TNonblockingServer

from mindscribe_handler import MindscribeHandler

class DummyHandler(object):
    def __init__(self):
        pass

    def log(self, messages):
        for m in messages:
            print m.category
            print m.message
        
        return ResultCode.OK

def print_usage():
	print 'Usage: python mindscribe_server.py <config-file>'
    
def read_config(config_file):
    f = open(config_file)
    config = json.load(f)
    return config

def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(2)
        
    config_file = sys.argv[1]
    config = read_config(config_file)
    
    # asynchronous server
    handler = MindscribeHandler(config)
    processor = Mindscribe.Processor(handler)
    transport = TSocket.TServerSocket(config['port'])
    server = TNonblockingServer.TNonblockingServer(processor, transport)
    
    print 'Starting the server on port: ' + config['port']
    server.serve()
    print 'done.'

if __name__ == '__main__':
	main()
