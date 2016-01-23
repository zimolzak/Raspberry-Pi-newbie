# http://www.r-bloggers.com/using-sqlite-in-r/
	
library("RSQLite")
library(ggplot2)

con = dbConnect(RSQLite::SQLite(), "~/Desktop/temperature.db")

joined = dbGetQuery(con, 'select * from temperature left join roomdetails on roomdetails.id = temperature.roomid where roomid > 1')

qplot(strptime(datetime, '%Y-%m-%d %H:%M:%S'), temperature, data=joined, colour=as.factor(room), xlab="Time")
