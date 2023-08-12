# Gross Domestic Product (GDP) and Fertility Rate Forecast For South Korea

Studying its impact of the forecasted GDP and fertility rate for the future of South Korea using Time series Analysis

#
**Languages Used:**

- Python

#
**Models Used:**
- Deep Learning Time Series (Neural Prophet by Meta)

#
**Business Problem**

South Korea has enjoyed the booming economy and made unprecedented technological advancements by such global companies as Samsung and LG. Despite these success stories, South Korea's fertility rate of 0.78 ranks the lowest in the world. This current project will analyze South Korea's GDP (per capita) trend and fertility rate over the course of the last twenty years. And then, I will forecast its GDP and fertility rate for the next 20 years to see if we can find any meaningful insights and possible recommendations for its policy makers.

#
**Data**

I retrieved timeseries datasets from the World Bank's DataBank. Specifically, I obtained a GDP timeseries data for South Korea and other G7 countries such as U.S. and Germany. Also, I was able to get a fertility rate timeseries dataset for South Korea and other G7 countries. Lastly, I found a timeseries meta data for various categories, including adolescent fertility rate, and many others for analyzing factors that may contribute to lower fertility rate. But for our main analysis, I have used the following two variables in the datasets.

- Gross domestic product (GDP) per capita (current US%) is gross domestic product divided by mid-year population.
- Fertility rate, total births per woman, or (TFR) is used to estimate the average number of children that a woman would have over her childbearing years (age 15-44) based on current birth trends.


#
**Methods**

Since the datasets from DataBank are already formatted with a series of annual data on GDP per capita, fertility rate, and others horizontally, I did not need to clean up much of the data. However, to use them for timeseries analysis using Neural Prophet library from Meta, I had to melt the data frames to two columns vertically (date and values). Then, I made a forecast of South Korea's GDP per capita and fertility rate. After that, more importantly, I was able to produce the forecasted data of the two variables into two new data frames and then merged them into one forecasted dataset for regression analysis to draw insights that can possibly help policy makers. In addition, I repeated the same process to make a plot for Germany's GDP per capita and fertility rate and made forecasted (or predicted) data.

#
**Analysis & Results**

In 2010, South Korea's GDP per capita reached over $23,000, and by the end of 2022, it was over $32,0000. The GDP predictive trend almost parallels that of Germany, which is an encouraging sign.

Given this upward trend of the GDP per capita, I made a forecast (prediction) of the country's GDP per capita over the next twenty years, using Neural Prophet, a Meta's timeseries forecasting library. Remarkably, South Korea's GDP per capita's upward climb would continue, and my forecast model predicted that the country's GDP per capita would be over $45,000 by 2045.

However, for South Korea's fertility rate (birth rate), the downward trend continued from 2000 to 2023. Two observations are noteworthy. South Korea's fertility rate fluctuated from 2002 to 2015, and after the country reached the rate at over 1.2 in 2015, the fertility rate rapidly declined to 0.8 in 2021. As for the fertility rate for Germany, its lowest point reached 1.33 in 2006, but it subsequently rebounded and reached its peak of 1.6 over the last years in 2016.

When my forecasting model predicted what the fertility rate for South Korea would be over the next 20 years, it would be plummeted to zero in 2026 and reached well below 0 to an extremely dangerous level of -0.50 after 2032.

In addition, there is a strong negative correlation between the predicted GDP and predicted fertility rate for South Korea. After running OLS regression analysis, the negative correlation is further supported by the R squared value of 0.739. That means as the country's fertility rate decreases, its GDP per capita increases, which is a predicament for South Korea's future and is also a reflection of the reality the country is currently facing, as more women choose a career over having children early in life.

#
**Future Uses/Additional Applications**

This project can generate actionable insights with both a positive prediction for South Korea's GDP per capita and a grim outlook for its fertility rate. For the South Korean government policy makers, they can analyze the trend for such key metrics like these and allocate resources in a manner that will help the country sustain GDP per capita's upward trend. Also, they can dedicate more resources to couples and families so that they can have a confidence in having more babies with readily available benefits, such as longer parental leave term especially for women who have jobs and raising paternity allowance to two-thirds of income like Germany (Martin, 2018).

#
**Recommendations**

Germany had experienced a decline in its fertility rate for decades. And yet, in 2018, Germany recorded its highest fertility rates since 1973 (Martin, 2018). It would be prudent for South Korea to study and analyze Germany's data not only for the fertility rate but also for GDP per capita since Germany has been able to recover from the demographic deficit while making steady economic growths.

For this project, that was a main reason to include a similar time series analysis section for Germany for a comparison purpose. Also, we will need to investigate why the fertility prediction for Germany also looks like it is about to erase all the gains in the fertility rate when making a prediction for the next twenty years. Lastly, both countries may need to consider a more flexible immigration policy to allow more qualified migrants to legally come to their countries while providing them with opportunities to work and start having family.
