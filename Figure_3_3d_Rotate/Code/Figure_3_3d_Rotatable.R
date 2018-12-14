d3 = read.csv('divorce_state_cleaned.csv')
library(threejs)
library(htmlwidgets)
js = scatterplot3js(as.numeric(d3$unemployment_rate), 
                    as.numeric(d3$low_edu_rate), 
                    as.numeric(d3$below_poverty_rate), 
                    color = as.factor(d3$color), 
                    axisLabels=c("Unemployed Rate","Below Poverty Rate", "Less Than High School"))
saveWidget(js, file="3d-scatter_new.html", selfcontained = TRUE, libdir = NULL, background = "white")

