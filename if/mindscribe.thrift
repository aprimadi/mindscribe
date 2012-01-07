namespace php mindscribe

enum ResultCode
{
  OK,
  TRY_LATER
}

struct LogEntry
{
  1: string category,
  2: string message
}

service Mindscribe
{
  ResultCode log(1: list<LogEntry> messages);
  string getVersion();
}