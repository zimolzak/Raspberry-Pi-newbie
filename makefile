pride_and_prejudice.txt : pg1342.txt
	tail --lines=+31 pg1342.txt | head --lines=-365 > pride_and_prejudice.txt

pg1342.txt :
	curl -O 'http://www.gutenberg.org/cache/epub/1342/pg1342.txt'
	perl -pi -e 's/\r\n/\n/g' pg1342.txt

clean :
	rm pg1342.txt
