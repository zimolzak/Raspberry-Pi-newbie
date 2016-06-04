split_plots : update
	./make_web_plots.R

all : nonletters.txt split_plots

update :
	./auto_rsync.pl
	mv temperature.db temperature.bak
	cp temperature.new temperature.db
	ls -lS temperature.*

unbackup :
	mv temperature.bak temperature.db

nonletters.txt : pride_and_prejudice.txt
	./nonletters.pl pride_and_prejudice.txt |sort | uniq -c | sort -nr > nonletters.txt

pride_and_prejudice.txt : pg1342.txt
	tail --lines=+31 pg1342.txt | head --lines=-365 > pride_and_prejudice.txt
#fixme --lines, for OS X

pg1342.txt :
	curl -O 'http://www.gutenberg.org/cache/epub/1342/pg1342.txt'
	perl -pi -e 's/\r\n/\n/g' pg1342.txt

clean :
	rm pg1342.txt
