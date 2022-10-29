#install.packages('stringi')
#install.packages('tidyverse')
#install.packages('car')
#install.packages('bestNormalize')
#install.packages('effsize')
#install.packages('stringr')
#install.packages('bestNormalize')
#install.packages('ggstatsplot')

library(effsize)
library(ggstatsplot)
library(bestNormalize)
library(stringr)
library(tidyverse)
library(ggplot2)
library(bestNormalize)
library(effsize)
library(dplyr)

df <- read_csv("/Users/quinn/Desktop/android-runner/results/complete_results_20221029.csv")
head(df)


# ======= Raw data analysis =======
summary(df)

native_apps <- df[df$AndroidApp == 1,]
web_apps <- df[df$AndroidApp == 0,]
cat('\n\n')
print(quantile(native_apps$TotalEnergyConsumption))
cat('\n\n')
print(quantile(web_apps$TotalEnergyConsumption))

outliers <- boxplot(TotalEnergyConsumption~AndroidApp, df, plot=FALSE)$out
df_no_outliers<-df[-which(df$TotalEnergyConsumption %in% outliers),]

plot(ggstatsplot::ggbetweenstats(
  data  = df,
  x     = AndroidApp,
  y     = TotalEnergyConsumption,
  pairwise.comparisons = FALSE,
))



# ======= Check for normality =======
check_normality <- function(data) {
  par(mfrow=c(1,2))
  plot(density(data$TotalEnergyConsumption))
  qqnorm(data$TotalEnergyConsumption)
  qqline(data$TotalEnergyConsumption)

  cat('\n\n')
  print(shapiro.test(data$TotalEnergyConsumption))
  par(mfrow=c(1,1))
}

check_normality(native_apps)
check_normality(web_apps)



# ======= Normalize the data =======
cols_native <- as.numeric(unlist(c(native_apps %>% select(TotalEnergyConsumption))))
order_object_native <- bestNormalize(cols_native)
p_native <- predict(order_object_native)
x2 <- predict(orderNorm_obj, newdata = p_native, inverse = TRUE)

cols_web <- as.numeric(unlist(c(web_apps %>% select(TotalEnergyConsumption))))
order_object_web <- bestNormalize(cols_web)
p_web <- predict(order_object_web)
x3 <- predict(order_object_web, newdata = p_web, inverse = TRUE)



# ======= Hypothesis testing =======
res <- t.test(x2, x3, alternative = "two.sided")
cat('\n\n')
print(res)



# ======= Effect Size Estimation =======
effect_size <- cohen.d(native_apps$TotalEnergyConsumption, web_apps$TotalEnergyConsumption)
cat('\n\n')
print(effect_size)

