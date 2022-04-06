library(readxl)
Mobiles <- read_excel("~/Documents/GitHub/Consumer-trust-In-E-Commerce-In-India/Data/Clean Data/1_Mobiles.xlsx")
Mobiles$Category <- "Mobiles"
Laptops <- read_excel("~/Documents/GitHub/Consumer-trust-In-E-Commerce-In-India/Data/Clean Data/2_Laptops.xlsx")
Laptops$Category <- "Laptops"
Sports <- read_excel("~/Documents/GitHub/Consumer-trust-In-E-Commerce-In-India/Data/Clean Data/3_Sports.xlsx")
Sports$Category <- "Sports"
Bottles <- read_excel("~/Documents/GitHub/Consumer-trust-In-E-Commerce-In-India/Data/Clean Data/4_Bottles.xlsx")
Bottles$Category <- "Category"
Baby <- read_excel("~/Documents/GitHub/Consumer-trust-In-E-Commerce-In-India/Data/Clean Data/5_Baby Products.xlsx")
Baby$Category <- "Baby"
Tools <- read_excel("~/Documents/GitHub/Consumer-trust-In-E-Commerce-In-India/Data/Clean Data/6_Tools.xlsx")
Tools$Category <- "Tools"
Gym <- read_excel("~/Documents/GitHub/Consumer-trust-In-E-Commerce-In-India/Data/Clean Data/7_Gym.xlsx")
Gym$Category <- "Gym"
Books <- read_excel("~/Documents/GitHub/Consumer-trust-In-E-Commerce-In-India/Data/Clean Data/8_Books.xlsx")
Books$Category <- "Books"
Groceries <- read_excel("~/Documents/GitHub/Consumer-trust-In-E-Commerce-In-India/Data/Clean Data/9_Groceries.xlsx")
Groceries$Category <- "Groceries"
Furnishing <- read_excel("~/Documents/GitHub/Consumer-trust-In-E-Commerce-In-India/Data/Clean Data/10_Home Furnishing.xlsx")
Furnishing$Category <- "Furnishing"
Products <- list(Baby, Books, Bottles, Furnishing, Groceries, Gym, Laptops, Mobiles, Sports, Tools)
Products <- as.data.frame(do.call(rbind, Products))
rm(list=setdiff(ls(), "Products"))
library(psych)
describeBy(Products$Trust, group = Products$Category, mat = TRUE)
library(readxl)
SampledProducts <- read_excel("Documents/GitHub/Consumer-trust-In-E-Commerce-In-India/Products.xlsx")
