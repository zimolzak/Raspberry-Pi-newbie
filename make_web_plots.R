#!/usr/bin/env Rscript
library("RSQLite")
library(ggplot2)

con = dbConnect(RSQLite::SQLite(), "/var/www/database/temperature.db")

joined = dbGetQuery(con, 'select * from temperature left join roomdetails on roomdetails.id = temperature.roomid where roomid > 1')
fixdate = cbind(joined, data.frame(posix_t = strptime(joined$datetime, '%Y-%m-%d %H:%M:%S', tz="GMT")))

k = 6
horizon = Sys.time() - 3600 * k
last_k_hours = fixdate[fixdate$posix_t > horizon,]
radiator = last_k_hours[last_k_hours$roomid == 2,]
catbed = last_k_hours[last_k_hours$roomid == 3,]
outside = last_k_hours[last_k_hours$roomid == 4,]

R = qplot(posix_t, temperature, data=radiator, xlab="Time (UTC)", main="Radiator")
C = qplot(posix_t, temperature, data=catbed, xlab="Time (UTC)", main="Cat bed")
O = qplot(posix_t, temperature, data=outside, xlab="Time (UTC)", main="Outdoors")

# localize all of these to WWW
ggsave(R, file="~/Desktop/radiator.png")
ggsave(C, file="~/Desktop/catbed.png")
ggsave(O, file="~/Desktop/outside.png")
