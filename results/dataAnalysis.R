#install.packages('stringi')
#install.packages('tidyverse')
#install.packages('car')
#install.packages('bestNormalize')
#install.packages('effsize')
#install.packages('stringr')
#install.packages('bestNormalize')
#install.packages('ggstatsplot')
#install.packages('sm')
#install.packages('cowplot')

library(cowplot)
library(sm)
attach(mtcars)
library(effsize)
library(ggstatsplot)
library(bestNormalize)
library(stringr)
library(tidyverse)
library(ggplot2)
library(bestNormalize)
library(effsize)
library(dplyr)

df <- read_csv("/Users/quinn/Desktop/android-runner/data/complete_results_20221029.csv")
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
  data  = native_apps,
  x     = AndroidApp,
  y     = ScreenEnergyConsumption,
  pairwise.comparisons = FALSE,
))

df_no_outliers$AndroidApp[df_no_outliers$AndroidApp == 1] <- "Android"
df_no_outliers$AndroidApp[df_no_outliers$AndroidApp == 0] <- "Web"

p1 <- plot(ggstatsplot::ggbetweenstats(
        data  = df_no_outliers,
        x     = AndroidApp,
        y     = ScreenEnergyConsumption,
        pairwise.comparisons = FALSE,
        title = "Screen consumption"
      ))

p2 <- plot(ggstatsplot::ggbetweenstats(
        data  = df_no_outliers,
        x     = AndroidApp,
        y     = WiFiEnergyConsumption,
        pairwise.comparisons = FALSE,
        title = "Wifi consumption"

      ))
p3 <- plot(ggstatsplot::ggbetweenstats(
        data  = df_no_outliers,
        x     = AndroidApp,
        y     = GPSEnergyConsumption,
        pairwise.comparisons = FALSE,
        title = "GPS consumption"

      ))
p4 <- plot(ggstatsplot::ggbetweenstats(
        data  = df_no_outliers,
        x     = AndroidApp,
        y     = CPUEnergyConsumption,
        pairwise.comparisons = FALSE,
        title = "CPU consumption"
      ))

plot((p1 + p2 + p3 + p4))



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
x2 <- predict(order_object_native, newdata = p_native, inverse = TRUE)

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


#create density plot
sm.density.compare(df$TotalEnergyConsumption, df$AndroidApp, xlab="Energy consumption in (j)", display = "image", model = "none")
means <- aggregate(df$TotalEnergyConsumption ~ df$AndroidApp, FUN = mean)
abline(v = means[1,2], col = 2)
abline(v = means[2,2], col = 3, lty = 2)
legend("top", legend=c("web", "android"), col = df$AndroidApp, lty = 1:2, cex = 1.5, bty="n")



