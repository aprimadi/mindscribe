import os

class BaseFile(object):
    def __init__(self, filepath):
        pass
    
    """
    @param message -- {mindscribe.ttypes.LogEntry}
    """
    def writeMessage(self, message):
        pass
    
    def getSize():
        pass

class StandardFile(object):
    def __init__(self, filepath):
        self.file = open(filepath, 'a+')             # {built-in File}
        self.file_size = os.path.getsize( filepath ) # {int}
    
    def writeMessage(self, m):
        to_write = m.category + ':' + m.message + '\n'
        self.file.write( to_write )
        self.file_size += len(to_write)
    
    def getSize(self):
        return self.file_size

class HdfsFile(object):
    def __init__(self, filepath):
        pass
    
    def writeMessage(self, message):
        pass
    
    def getSize(self):
        pass
