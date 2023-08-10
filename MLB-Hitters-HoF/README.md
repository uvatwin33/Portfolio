# MLB-Hitters-HoF
ML Model to Predict Future Hall of Fame Hitters in MLB 

**Predicting Major League Baseball Hall of Fame Hitters**

Can MLB General Managers predict future Hall of Fame hitters?

**Languages Used**

- Python

**Overview**

For any baseball fans, it is exciting to see All-Star caliber type of players on their favorite teams to cheer on any given night. If those players are worthy of the future Hall of Fame induction, the same fans would be gone wild and love to follow their careers because those Hall of Famers significantly contribute to their teams winning.

Thus, it is paramount to each team's General Manager to find future Hallo of Famers within their team pipeline or elsewhere. So, a GM, can you predict if hitters on your team can make the Hall of Fame in Cooperstown, NY?

**Data**

I obtained datasets from Sean Lahman's baseball database as well as WAR (Wins Above Replacement) data from Baseball-Reference.com. Data was cleaned and used to create dictionaries. And then, the dictionaries were converted into dataframes, data featuring and engineering were performed to create categories such as batting average and OPS (on-base percentage), and eventually the datasets were merged to create a hitters dataframe (df\_hitters).

- **Master.csv** – tells you more about the player names, Date of Birth (DOB), and biographical information
- **Batting.csv** – shows the batting statistics
- **Fielding.csv** – shows the fielding statistics
- **AwardsPlayers.csv** – contains data on the various awards won by players
- **AllstarFull.csv** – contains data on all the All-Star appearances by players
- **HallOfFame.csv** – contains voting data for the Hall of Fame
- **Appearances**.csv – provides you with details on the positions at which a player appeared
- **WAR** (wins above replacement) – contains data on the WAR statistics

**Results**

High Level Takeaways:

- The classifier model (logistic regression) generated a very high accuracy of 99% on testing in terms of predicting players who got into the Hall of Fame based on the data for players who retired 15 years or longer and played over 10 seasons in the leagues, which is a requirement for the eligibility.
- Other models such as Decision Tree and Random Forest also produced a similar accuracy.
- After the data was PCA-scaled, the accuracy decreased to 96% but is still high.
- When the model was tested on the data for active or eligible players (df\_eligible) who did get into the Hall of Fame over the last ten years, it generated a correct list of Vladimir Guerrero, Jim Thome, Frank Thomas, Ken Griffey Jr., Chipper Jones, and Derek Jeter.

**Assumptions:**

One of the assumptions is that those players who have been linked to the human growth hormones or steroids have been in the pool of the eligible players. However, there is no indication that they will be inducted any time soon.

The data seems imbalanced, but when the data was resampled or oversampled for the target variable (HoF = 1), the accuracy result came out to be slightly over 99%, which was very similar to the result before the data resampling to address the imbalance. More investigation will need to be done or the data would need to be oversampled with SMOTE method for another verification of the accuracy result.
