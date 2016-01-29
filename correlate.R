#!/usr/bin/env Rscript

library("RSQLite")
library(ggplot2)

con = dbConnect(RSQLite::SQLite(), "~/Desktop/local/Raspberry-Pi-newbie/temperature.db")

joined = dbGetQuery(con, 'select * from temperature left join roomdetails on roomdetails.id = temperature.roomid where roomid > 1')

radiator = joined[joined$roomid == 2,]
catbed = joined[joined$roomid == 3,]
p = qplot(radiator$temperature, catbed$temperature)
ggsave(p, file="~/Desktop/scatterplot.png")
