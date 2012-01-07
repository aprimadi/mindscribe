all:
	thrift -r --gen php --gen py if/mindscribe.thrift
	cp -R gen-php/mindscribe client/lib/thrift/packages/mindscribe

clean:
	rm -Rf gen-py gen-php
	rm -Rf client/lib/thrift/packages/mindscribe