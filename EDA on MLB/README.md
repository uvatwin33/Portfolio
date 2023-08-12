# Exploratory Data Analysis on Major League Baseball

**Languages Used**

- Python

**Packages Used for EDA**

- Thinkstats2
- Matplotlib
- Seaborn
- Numpy
- Pandas

**Statistical Functions Used**

- PMF (Probability Mass Function)
- PDF (Probability Density Function)
- CDF (Cumulative Distribution Function)

**Data Used**

- **Teams.csv (from Sean Lahman's baseball database)**

**Introduction**

A brief exploratory data analysis on Major League Baseball involves the distribution of wins, Homeruns, Strikeouts by pitchers, runs produced by hitters, etc. This EDA project also analyzes which league (American League or National League) would be a good league to start a baseball franchise in, using PMF, PDF, and CDF, while examining factors that may contribute to improving attendance using regression analysis.

**Results**

National League is likely to win more than 80 plus games given a slightly higher probability of 0.035 based on the PDF plots using Thinkstats2 library, but past the 90th game mark, American League seems slightly more likely to win games closed to 100 games, which is league championship caliber.

In terms of finding factors attributable to increasing attendance at the games, more action-inducing plays like hitting doubles are said to help. But based on the correlation analysis, there was no strong relationship between doubles and attendance nor singles and attendance.

**Further investigation for improvement**

I think the correlation analysis between action-inducing features of the game and attendance may yield different results if I resample the data or reduce the scope of the data. Even though, I removed the rows with zero attendance data, the number of games played varied over the years. It wasn't until 1980s that MLB started a 162-game season. In the early 1900s, there were some years when fewer games were played perhaps due to wars or economic depressions. Thus, a smaller population could have produced a different outcome on the correlation analysis.

**Copyright**

[**http://thinkstats2.com**](http://thinkstats2.com/) ** **** Copyright 2016 Allen B. Downey MIT License: **** ** [**https://opensource.org/licenses/MIT**](https://opensource.org/licenses/MIT)
