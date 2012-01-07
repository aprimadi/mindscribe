import time
import os
from threading import Lock
from mfile import StandardFile, HdfsFile

class Store(object):
    def __init__(self, config):
        self.lock = Lock()
        self.file = None
        self.file_path = config['file_path']         # {String}
        self.base_filename = config['base_filename'] # {String}
        self.max_size = config['max_size']           # {int}
        self.rotate_period = config['rotate_period'] # {String}
        self.rotate_hour = config['rotate_hour']     # {int}
        self.rotate_minute = config['rotate_minute'] # {int}
        self.last_rotate_timestamp = None
        
        self.createFile()
    
    """
    @param message -- {mindscribe.ttypes.LogEntry}
    """
    def addMessage(self, message):
        self.lock.acquire()
        
        self.file.writeMessage(message)
        
        self.lock.release()
    
    # virtual
    def createFile(self):
        pass
    
    def rotateFile(self):
        self.lock.acquire()
        
        self.file.close()
        self.createFile()
        
        self.lock.release()
    
    def shouldRotate(self):
        if self.file.getSize() >= self.max_size:
            return True
        
        # TODO check rotate period
        
        return False
    
    def filename(self):
        timestamp = int(time.time())
        return self.base_filename + "_" + str(timestamp)
    
    # virtual
    def filepath(self):
        pass
    
class StandardStore(Store):
    def __init__(self, config):
        super(StandardStore, self).__init__(config)
    
    def createFile(self):
        if self.file:
            self.file.flush()
            self.file.close()
            
        # create directory if not exists
        filepath = self.filepath()
        dirpath = os.path.dirname( filepath )
        if not os.path.isdir(dirpath):
            os.makedirs(dirpath, 0755)
        
        self.file = StandardFile( self.filepath() )
    
    def filepath(self):
        return self.file_path + self.filename()

class HdfsStore(Store):
    def __init__(self, config):
        super(HdfsStore, self).__init__(config)
    
    def createFile(self):
        # TODO
        pass
    
    def filepath(self):
        # TODO
        pass
    
class StoreFactory(object):
    FS_TYPE = ['hdfs', 'std']
    
    def __init__(self):
        pass

    @classmethod
    def createStore(cls, config):
        if config['fs_type'] == 'hdfs':
            return HdfsStore(config)
        else:
            return StandardStore(config)
