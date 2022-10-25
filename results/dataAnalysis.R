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

check_normality <- function(data) { 
  par(mfrow=c(1,2)) 
  plot(density(data$EnergyConsumption)) 
  #car::qqPlot(data) 

  #qqplot(data1$Name,data1$EnergyConsumption, xlab =  "x",  ylab = "", main = "")
  qqnorm(data$EnergyConsumption)
  qqline(data$EnergyConsumption)

  print(shapiro.test(data$EnergyConsumption)) 
  par(mfrow=c(1,1)) 
} 

# Mutate data  
df = df %>% 
  mutate( 
    cons_log = log(EnergyConsumption), 
    cons_sqrt = sqrt(EnergyConsumption), 
    cons_reciprocal = 1/EnergyConsumption 
  ) 

check_normality(df[df$AndroidApp == 1,]) 
check_normality(df[df$AndroidApp == 0,]) 

native_app <- df %>%
  filter(AndroidApp == "1") %>%
  pull(EnergyConsumption)
web_app <- df %>%
  filter(AndroidApp == "0") %>%
  pull(EnergyConsumption)

res <- t.test(native_app, web_app)
print(res)
