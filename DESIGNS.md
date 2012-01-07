What is MindScribe?
===================

It is a non-distributed log server written in Python used at MindTalk. Many of the
design decision is borrowed from Facebook Scribe.

Store
=====

A Store is a class that handles storage related function. It
encapsulates the following information:

category -- category that this store is related to
file_path -- absolute path where to store this log
base_filename -- the log filename is #{base_filename + '_' + timestamp}
max_size -- max log file size before being rotated
fs_type -- {std,hdfs}
rotate_period -- {daily}
rotate_hour -- {0-23}
rotate_minute -- {0-59}

StoreQueue
==========

Store queue buffer messages in memory before being sinked to disk.
