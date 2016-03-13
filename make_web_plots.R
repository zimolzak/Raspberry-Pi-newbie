#!/usr/bin/env Rscript
library(RSQLite)
library(ggplot2)

con = dbConnect(RSQLite::SQLite(), "~/Desktop/local/Raspberry-Pi-newbie/temperature.db")

joined = dbGetQuery(con, 'select * from temperature left join roomdetails on roomdetails.id = temperature.roomid where roomid > 1')

fixdate = cbind(joined, data.frame(posix_t = strptime(joined$datetime, '%Y-%m-%d %H:%M:%S', tz="GMT")))

### Three plots of last 6 hours ###

k = 6
horizon = Sys.time() - 3600 * k
last_k_hours = fixdate[fixdate$posix_t > horizon,]
radiator = last_k_hours[last_k_hours$roomid == 2,]
catbed = last_k_hours[last_k_hours$roomid == 3,]
outside = last_k_hours[last_k_hours$roomid == 4,]

R = qplot(posix_t, temperature, data=radiator, xlab="Time (UTC)", main="Radiator")
C = qplot(posix_t, temperature, data=catbed, xlab="Time (UTC)", main="Cat bed")
O = qplot(posix_t, temperature, data=outside, xlab="Time (UTC)", main="Outdoors")

ggsave(R, file="~/Desktop/radiator.png")
ggsave(C, file="~/Desktop/catbed.png")
ggsave(O, file="~/Desktop/outside.png")

### One plot, 3 lines, last 2.5 days ###

d = 2.5
horizon = Sys.time() - 3600 * d * 24
last_d_days = fixdate[fixdate$posix_t > horizon,]

A = qplot(posix_t, temperature, data=last_d_days, colour=as.factor(room), xlab="Time (UTC)", geom="line")

ggsave(A, file="~/Desktop/probes_60h_line.png")

### Temp vs temp ###

radiator = fixdate[fixdate$roomid == 2,]
catbed = fixdate[fixdate$roomid == 3,]
outside = fixdate[fixdate$roomid == 4,]

p = qplot(radiator$temperature, catbed$temperature, geom="path", color=as.numeric(radiator$posix_t))
ggsave(p, file="~/Desktop/in_vs_rad.png")

q = qplot(outside$temperature, catbed$temperature, geom="path", color=as.numeric(outside$posix_t))
ggsave(q, file="~/Desktop/in_vs_out.png")

r = qplot(outside$temperature, radiator$temperature, geom="path", color=as.numeric(outside$posix_t))
ggsave(r, file="~/Desktop/rad_vs_out.png")
