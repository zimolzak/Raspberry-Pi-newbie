#!/usr/bin/env Rscript

library("RSQLite")
library(ggplot2)

con = dbConnect(RSQLite::SQLite(), "~/Desktop/local/Raspberry-Pi-newbie/temperature.db")

joined = dbGetQuery(con, 'select * from temperature left join roomdetails on roomdetails.id = temperature.roomid where roomid > 1')

fixdate = cbind(joined, data.frame(posix_t = strptime(joined$datetime, '%Y-%m-%d %H:%M:%S', tz="GMT")))

k = 6

horizon = Sys.time() - 3600 * k

last_k_hours = fixdate[fixdate$posix_t > horizon,]

p = qplot(posix_t, temperature, data=last_k_hours, colour=as.factor(room), xlab="Time (UTC)")

ggsave(p, file="~/Desktop/last6.png")
