#install.packages('tidyverse') 
#install.packages('car') 
#install.packages('bestNormalize') 
#install.packages('effsize')

library(tidyverse)
library(ggplot2)
#library(car) 
library(bestNormalize) 
library(effsize) 

df <- read_csv("/Users/quinn/Desktop/android-runner/data/complete_results_20221022.csv")
head(df)

levels(df$Name)
levels(df$AndroidApp)

summary(df)


df %>% group_by(Name) %>% 
  summarize(mean_cons = mean(EnergyConsumption), 
  sd_cons = sd(EnergyConsumption))

boxplot(EnergyConsumption~AndroidApp, df) 

check_normality <- function(data, data1) { 
  par(mfrow=c(1,2)) 
  plot(density(data)) 
  car::qqPlot(data) 
  print(shapiro.test(data)) 
  par(mfrow=c(1,1)) 
} 

check_normality(df$EnergyConsumption, data) 