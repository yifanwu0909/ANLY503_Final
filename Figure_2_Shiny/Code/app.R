# Load packages
library(shiny)
library(shiny)
library(shiny)
library(shinythemes)
library(dplyr)
library(readr)
library("shiny")
library("shinyWidgets")


# Define UI
ui <- fluidPage(
  
  titlePanel("Marital Status in Different Places of Birth"),
  sidebarLayout(
    
    sidebarPanel(
      sliderTextInput("birth_place", 
                      "Birth Places:", 
                      choices = c("Born in State", "Born Other State", "Native born outside of US", "Foreign"),
                      selected = c("Born in State"),
                      grid = TRUE,
                      dragRange = TRUE,
                      force_edges = T, width = 800)
    ),
  mainPanel(
    plotOutput(outputId = "plot")
  )
))
as.integer()

# Define server function
server <- function(input, output) {
  
  output$plot <- renderPlot({
    library(stringr)
    library(ggplot2)
    s = input$birth_place
    df <- read.csv(paste(s, ".csv", sep=""))
    int_breaks <- function(x, n = 5) pretty(x, n)[pretty(x, n) %% 1 == 0]
    ggplot() + 
      geom_line(data = df, aes(x = X, y = Never.married, color = "red"), show.legend = T) + 
      geom_line(data = df, aes(x = X, y = Now.married..except.separated, color = "cyan"), show.legend = T) + 
      geom_line(data = df, aes(x = X, y = Divorced, color = "gold"), show.legend = T) + 
      geom_line(data = df, aes(x = X, y = Separated, color = "orchid1"), show.legend = T) +
      geom_line(data = df, aes(x = X, y = Widowed, color = "black"), show.legend = T) +
      ggtitle(paste('Rate for Each Marrital Status from 2005 to 2017 (Born ', s , ')')) +
      scale_color_manual(name = "Rate for Each Marriage Status", 
                         values = c("red", "cyan", "gold", "orchid1", "black"),
                         labels = c("red" = "never", "cyan" = "married", "gold" = "devorced", 
                                    "orchid1" = "seperated", "black" = "widowed")) + 
      scale_x_continuous(breaks = int_breaks) +
      xlab('Year')  + 
      ylab('Rate for Each Marriage Status') +
      ylim(0, 1) +
      coord_fixed(ratio = 10)
  })
}

# Create Shiny object
shinyApp(ui = ui, server = server)

# deploy:
library(rsconnect)
rsconnect::deployApp('C:/Users/yifan/Documents/ANLY 503/Final Exam/shinyapp')
