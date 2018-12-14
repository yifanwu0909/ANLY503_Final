# marriage vs income #boxplot
library(RColorBrewer)
library(ggthemes)
library(ggplot2)
marriage_income <- read.csv("income_marriage_boxplot.csv")
#write.csv(marriage_income, file = "income_marriage.csv")
marriage_income300 <- read.csv("income_marriage300_boxplot_jitter.csv")
p0 = ggplot(data = marriage_income, aes(x=MAR, y=PINCP, fill=as.factor(MAR))) +
  geom_boxplot(aes(group = MAR)) +
  geom_jitter(data = marriage_income300, aes(x = MAR, y = PINCP)) +
  scale_y_continuous(name ="Income", labels = scales::comma) +
  ggtitle("Income distribution by Different Marrital Status") +
  #theme(axis.text.x = element_text(c("a", "b", "c", "d", "e"))) +
  scale_x_discrete(name ="Marrital Status", limits=c("Married","Widowed", "Divorced", "Seperated", "Never Married")) +
  scale_fill_discrete(guide=FALSE)
# compute lower and upper whiskers
ylim1 = boxplot.stats(marriage_income$PINCP)$stats[c(1, 5)]

# scale y limits based on ylim1
p1 = p0 + coord_cartesian(ylim = ylim1*1.05) #+ theme_economist()
p1
