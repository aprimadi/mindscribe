<?php
$GLOBALS['THRIFT_ROOT'] = 'lib/thrift';

require_once $GLOBALS['THRIFT_ROOT'].'/Thrift.php';
require_once $GLOBALS['THRIFT_ROOT'].'/protocol/TBinaryProtocol.php';
require_once $GLOBALS['THRIFT_ROOT'].'/transport/TSocket.php';
require_once $GLOBALS['THRIFT_ROOT'].'/transport/THttpClient.php';
require_once $GLOBALS['THRIFT_ROOT'].'/transport/TBufferedTransport.php';
require_once $GLOBALS['THRIFT_ROOT'].'/transport/TFramedTransport.php';

require_once $GLOBALS['THRIFT_ROOT'].'/packages/mindscribe/Mindscribe.php';

$socket = new TSocket('localhost', 9091);
$transport = new TFramedTransport($socket, 1024, 1024);
$protocol = new TBinaryProtocol($transport);
$client = new mindscribe_MindscribeClient($protocol);

try {
  
    $transport->open();
    $log_entries = array();
    $log = new mindscribe_LogEntry();
    $log->category = 'test';
    $log->message = 'Hello World';
    $log_entries[] = $log;
    $result_code = $client->log($log_entries);
    echo $result_code . "\n";
    
} catch (TException $e) {
    echo $e->getMessage() . "\n";
}

?>
