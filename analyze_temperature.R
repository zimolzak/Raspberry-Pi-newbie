# http://www.r-bloggers.com/using-sqlite-in-r/
	
library("RSQLite")
con = dbConnect(RSQLite::SQLite(), "~/Desktop/temperature.db")
p1 = dbGetQuery(con, 'select * from temperature where id > 1000')
p2 = dbGetQuery(con, 'select count(*) from temperature')
p3 = dbGetQuery(con, 'select * from roomdetails')
p4 = dbGetQuery(con, 'select * from temperature where roomid > 1')

library(ggplot2)
qplot(datetime, temperature, data=p4, colour=as.factor(roomid))

joined = dbGetQuery(con, 'select * from temperature left join roomdetails on roomdetails.id = temperature.roomid where roomid > 1')

qplot(datetime, temperature, data=joined, colour=as.factor(room))

qplot(strptime(datetime, '%Y-%m-%d %H:%M:%S'), temperature, data=joined, colour=as.factor(room))
