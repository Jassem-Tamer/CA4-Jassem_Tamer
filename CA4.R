install.packages('ggplot2')
library(ggplot2)
setwd("/Users/jeo/Desktop/Python3")
data_analysis <- read.csv('file1.csv', header=TRUE)
summary(data_analysis)
author <- data_analysis[2]
author
date <- data_analysis[3]
date
plot(data_analysis$author, data_analysis$date)
ggplot(data=data_analysis, aes(x=author, y=date))
plot(data_analysis)

plot(data_analysis$Author, data_analysis$NumberofLines)

pairs(data_analysis)

