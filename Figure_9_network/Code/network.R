
#Network graph:

#install.packages("igraph")
#install.packages("network")
#install.packages("sna")
#install.packages("ndtv")

library(igraph)
library(network)
library(sna)
library(ndtv)
library(networkD3)

df <- read.csv("edge.csv")
screenName <- as.vector(df$Source)#c('q15f', 'q15g', 'q15c', 'q15b', 'q15d', 'q15f')
mention <- as.vector(df$Target)#c('q15c', 'q15h', 'q15i', 'q15d', 'q15h')
scalar <- function(x) {20 * x / sqrt(sum(x^2))}
n <- scalar(as.vector(df$Value))#c(297, 327, 125, 120, 152)
nodeFactors <- factor(sort(unique(c(screenName, mention))))
nodes <- data.frame(name = nodeFactors, group = 1)
screenName <- match(screenName, levels(nodeFactors)) - 1
mention <- match(mention, levels(nodeFactors)) - 1
links <- data.frame(screenName, mention, n)
network = forceNetwork(Links = links, Nodes = nodes, Source = 'screenName', 
             Target = 'mention', Value = 'n', NodeID = 'name', Group = 'group', zoom = T,
             opacityNoHover = 0.8, 
             linkDistance = 100,
             fontSize = 15, 
             clickAction = T)
network
saveNetwork(network, 'network.html', selfcontained = TRUE)
