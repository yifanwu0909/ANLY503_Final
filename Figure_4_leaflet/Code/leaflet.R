#Leaflet

library(maps)
library(leaflet)
library(leaflet)
library(sp)
library(mapproj)
library(maps)
library(mapdata)
library(maptools)
library(htmlwidgets)
library(magrittr)
library(XML)
library(plyr)
library(rgdal)
library(WDI)
library(raster)
library(noncensus)
library(stringr)
library(tidyr)
library(tigris)
library(rgeos)
library(ggplot2)
library(scales)

us.map <- tigris::counties(cb = TRUE, year = 2017)
us.map <- us.map[!us.map$STATEFP %in% c("02", "15", "72", "66", "78", "60", "69",
                                        "64", "68", "70", "74"),]
us.map <- us.map[!us.map$STATEFP %in% c("81", "84", "86", "87", "89", "71", "76",
                                        "95", "79"),]


mar_leaf <- read.csv("leaflet_mar.csv")
div_leaf <- read.csv("leaflet_div.csv")

mar_leaf$GEOID <- formatC(mar_leaf$GEOID, width = 5, format = "d", flag = "0")
div_leaf$GEOID <- formatC(div_leaf$GEOID, width = 5, format = "d", flag = "0")

mar_map <- merge(us.map, mar_leaf, by = c("GEOID"))
popup_mar <- paste0("<strong>County: </strong>", 
                    mar_map$county, 
                    "<br><strong>Marriage Rate : </strong>", 
                    mar_map$mar_rate,
                    "%")
popup_div <- paste0("<strong>County: </strong>", 
                   div_leaf$county, 
                   "<br><strong>Divorce Rate if > 16% : </strong>", 
                   div_leaf$div_rate,
                   "%")
pal <- colorQuantile("YlOrRd", NULL, n = 9)

gmap <- leaflet(data = mar_map) %>%
  # Base groups
  addTiles() %>%
  setView(lng = -105, lat = 40, zoom = 4) %>% 
  addPolygons(fillColor = ~pal(mar_rate), 
              fillOpacity = 0.8, 
              color = "#BDBDC3", 
              weight = 1,
              popup = popup_mar,
              group="Marriage Rate by Counties") %>% 
  # Overlay groups
  addMarkers(data = div_leaf, lat = ~lat, lng = ~long, popup = popup_div, group = "Divorce Rate > 16% by Counties") %>% 
  addLayersControl(
    baseGroups = c("Marriage Rate by Counties"),
    overlayGroups = c("Divorce Rate > 16% by Counties"),
    options = layersControlOptions(collapsed = FALSE)
  )

gmap
saveWidget(gmap, 'leaflet.html', selfcontained = T)
