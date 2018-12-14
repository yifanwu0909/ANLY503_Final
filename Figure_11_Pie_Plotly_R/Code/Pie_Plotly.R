install.packages('plotly')
install.packages('xml2')
install.packages('datasets')
install.packages('htmlwidgets')
install.packages("magrittr")
library(magrittr)
library(plotly)
library(datasets)
library(xml2)
library(htmlwidgets)
Sys.setenv("plotly_username"="WuYifan")
Sys.setenv("plotly_api_key"="u2QEq8fd0TTozYHjLzXQ")

purpose <- read.csv("r_plotly_purpose_of_marriage.csv")
m <- list(
  l = 50,
  r = 50,
  b = 100,
  t = 100,
  pad = 4
)
p <- plot_ly(purpose, labels = ~Purpose, values = ~Percent, type = 'pie',
             textposition = 'inside',
             textinfo = 'label+percent',
             width = 650, 
             height = 650) %>% 
  layout(title = 'Purpose of Marriage Survey 2007',
         xaxis = list(showgrid = FALSE, zeroline = FALSE, showticklabels = FALSE),
         yaxis = list(showgrid = FALSE, zeroline = FALSE, showticklabels = FALSE),
         autosize = F, margin = m)

# Create a shareable link to your chart
# Set up API credentials: https://plot.ly/r/getting-started
chart_link = api_create(p, filename="pie-basic")
chart_link
