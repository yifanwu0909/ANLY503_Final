setwd("C:/Users/yifan/Documents/ANLY 503/Final Exam/")

m <- read.csv("male_married.csv")
f <- read.csv("female_married.csv")
install.packages("gridExtra")
library("gridExtra")
library(ggplot2)
library(reshape2)

p3 = ggplot() + 
  geom_line(data = f, aes(x = year, y = NE, color = "red"), show.legend = T) + 
  geom_line(data = m, aes(x = year, y = NE, color = "black"), show.legend = T) + 
  geom_point(data = f, aes(x = year, y = NE, color = "red")) +
  geom_point(data = m, aes(x = year, y = NE, color = "black")) +
  ggtitle('US NorthEast marriage rate between genderes') +
  scale_color_discrete(name = "Gender", labels = c("Female", "Male")) + 
  xlab('year')  + 
  ylab('Percentage of Married')

p4 = ggplot() + 
  geom_line(data = f, aes(x = year, y = MW, color = "red"), show.legend = T) + 
  geom_line(data = m, aes(x = year, y = MW, color = "black"), show.legend = T) + 
  geom_point(data = f, aes(x = year, y = MW, color = "red")) +
  geom_point(data = m, aes(x = year, y = MW, color = "black")) +
  ggtitle('US MidWest marriage rate between genderes') +
  scale_color_discrete(name = "Gender", labels = c("Female", "Male")) + 
  xlab('year')  + 
  ylab('Percentage of Married')


p5 = ggplot() + 
  geom_line(data = f, aes(x = year, y = S, color = "red"), show.legend = T) + 
  geom_line(data = m, aes(x = year, y = S, color = "black"), show.legend = T) + 
  geom_point(data = f, aes(x = year, y = S, color = "red")) +
  geom_point(data = m, aes(x = year, y = S, color = "black")) +
  ggtitle('US South marriage rate between genderes') +
  scale_color_discrete(name = "Gender", labels = c("Female", "Male")) + 
  xlab('year')  + 
  ylab('Percentage of Married')
p6 = ggplot() + 
  geom_line(data = f, aes(x = year, y = W, color = "red"), show.legend = T) + 
  geom_line(data = m, aes(x = year, y = W, color = "black"), show.legend = T) + 
  geom_point(data = f, aes(x = year, y = W, color = "red")) +
  geom_point(data = m, aes(x = year, y = W, color = "black")) +
  ggtitle('US West marriage rate between genderes') +
  scale_color_discrete(name = "Gender", labels = c("Female", "Male")) + 
  xlab('year')  + 
  ylab('Percentage of Married')

grid.arrange(p3, p4, p5, p6, ncol = 2)
