#!/usr/bin/env Rscript
library(RSQLite)
library(ggplot2)

con = dbConnect(RSQLite::SQLite(), "~/Desktop/local/Raspberry-Pi-newbie/temperature.db")

query_base = 'select * from temperature left join roomdetails on roomdetails.id = temperature.roomid where roomid > 1 and datetime >'
date_str = substr(Sys.time() - 3600 * 4 * 24, 1, 10)
quoted_date_str = paste("'", date_str, "'", sep="")

joined = dbGetQuery(con, paste(query_base, quoted_date_str))

fixdate = cbind(joined, data.frame(posix_t = strptime(joined$datetime, '%Y-%m-%d %H:%M:%S', tz="GMT")))

### One plot, 3 lines, last 2.5 days ###

d = 2.5
horizon = Sys.time() - 3600 * d * 24
last_d_days = fixdate[fixdate$posix_t > horizon,]

A = qplot(c(posix_t), temperature, data=last_d_days, colour=as.factor(room), xlab="Time (local)", geom="line")

ggsave(A, file="~/Desktop/probes_60h_line.png")
