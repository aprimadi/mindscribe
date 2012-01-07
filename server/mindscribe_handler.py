import sys
from threading import Thread
import time
sys.path.append('./gen-py')

from mindscribe import Mindscribe
from mindscribe.ttypes import *

from store import StoreFactory

MINDSCRIBE_VERSION = "1.0"

class MindscribeHandler(object):
    SLEEP_INTERVAL = 1800 # 30 minutes
    
    def __init__(self, config):
        super(MindscribeHandler, self).__init__()
        
        self.config = config  # {Dictionary}
        self.store_map = {}
        
        # initialize store map
        for store_config in config['stores']:
            c = store_config['category']
            self.store_map[c] = StoreFactory.createStore(store_config)
            
    def log(self, messages):
        for m in messages:
            print m.category + ':' + m.message
            store = self.store_map[m.category]
            #store.addMessage(m)
        
        return ResultCode.OK
    
    def getVersion(self):
        return self.config['version']

    def run(self):
        while True:
            time.sleep( MindscribeHandler.SLEEP_INTERVAL )
            self.rotateCheck()
    
    def _rotateCheck(self):
        for k, v in self.store_map:
            store = v
            if store.shouldRotate():
                store.rotateFile()
