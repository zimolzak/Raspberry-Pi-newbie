#!/usr/bin/env Rscript

library("RSQLite")
library(ggplot2)

con = dbConnect(RSQLite::SQLite(), "~/Desktop/local/Raspberry-Pi-newbie/temperature.db")

joined = dbGetQuery(con, 'select * from temperature left join roomdetails on roomdetails.id = temperature.roomid where roomid > 1')

p = qplot(strptime(datetime, '%Y-%m-%d %H:%M:%S'), temperature, data=joined, colour=as.factor(room), xlab="Time")

ggsave(p, file="~/Desktop/temps2.png")
