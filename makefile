all : nonletters.txt temperature.db

all_temps_plot : update
	./analyze_temperature.R

update :
	mv temperature.db temperature.bak
	rsync pi@192.168.1.4:/var/www/database/temperature.db . 2> /dev/null

temperature.db :
	rsync --no-motd pi@192.168.1.4:/var/www/database/temperature.db .

nonletters.txt : pride_and_prejudice.txt
	./nonletters.pl pride_and_prejudice.txt |sort | uniq -c | sort -nr > nonletters.txt

pride_and_prejudice.txt : pg1342.txt
	tail --lines=+31 pg1342.txt | head --lines=-365 > pride_and_prejudice.txt

pg1342.txt :
	curl -O 'http://www.gutenberg.org/cache/epub/1342/pg1342.txt'
	perl -pi -e 's/\r\n/\n/g' pg1342.txt

clean :
	rm pg1342.txt
