import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading data files
tickerlist = pd.read_csv("tickerlist.csv")
returns = pd.read_csv("returns.csv")

#looking at date range
print("First date in dataset:", returns['Date'].min())
print("Last date in dataset:", returns['Date'].max())

#calculating average return for every stock column
avg_returns = returns.drop(columns=['Date']).mean()
print("\nTop 5 average stock returns:")
print(avg_returns.sort_values(ascending=False).head())

print("\nBottom 5 average stock returns:")
print(avg_returns.sort_values(ascending=True).head())

#visualisation of returns
top_5 = avg_returns.sort_values(ascending=False).head(5)
plt.figure(figsize=(10,5))
top_5.plot(kind="bar")
plt.title("Top 5 S&P 500 stocks by average  returns")
plt.xlabel("Stocks")
plt.ylabel("Average Returns")

bottom_5 = avg_returns.sort_values(ascending=True).head(5)
plt.figure(figsize=(10,5))
bottom_5.plot(kind="bar")
plt.title("Bottom 5 S&P 500 stocks by average returns")
plt.xlabel("Stocks")
plt.ylabel("Average Returns")


#Volatility
volatility = returns.drop(columns=["Date"]).std()

#visualisation of volatility

Top_volatility = volatility.sort_values(ascending=False).head(5)
plt.figure(figsize=(10,5))
Top_volatility.plot(kind="bar")
plt.title("Top 5  most volatile S&P 500 stocks")
plt.xlabel("Stocks")
plt.ylabel("Volatility")

plt.show()


#comparing average return with volatility
risk_return = pd.DataFrame({ "Average Return":avg_returns, "Volatility":volatility})
print("\nRisk vs Return:")
print(risk_return.head())

#Risk vs Return scatter plot
risk_return.plot(
    kind="scatter",
    x="Volatility",
    y="Average Return",
    figsize=(10,6)
    )
plt.title("Risk vs Return for S&P 500 stocks")
plt.xlabel("Volatility")
plt.ylabel("Average Return")

plt.show()




#calculating the correlation between risk and return
correlation = risk_return["Volatility"].corr(risk_return["Average Return"])
print("\nCorrelation between risk and return", correlation)

#calculating the average return across all stocks for each month
monthly_average_return = returns.drop(columns=["Date"]).mean(axis=1)
print("\nMonthly average returns:")
print(monthly_average_return.head())

monthly_analysis = pd.DataFrame({ "Date": returns["Date"], "Average Return": monthly_average_return})
print("\nMonthly analysis:")
print(monthly_analysis.head())

monthly_analysis.plot(
    kind="line",
    x="Date",
    y="Average Return",
    figsize=(10,6)
    )

plt.title("Average S&P 500 stock returns over time")
plt.show()


#correlation between individual stocks

stock_correlation = returns.drop(columns=["Date"]).corr()
print("\nStock cCorrelation")
print(stock_correlation.head())

plt.figure(figsize=(12,8))
sns.heatmap(stock_correlation.head())
plt.title("S&P 500 Stock correlation Heatmap")
plt.show()



#sector analysis
print("\nSector:" )
print(tickerlist["sector"].unique())

sector_count = tickerlist["sector"].value_counts()
print("\nCompanies per sector:")
print(sector_count)

sector_map = dict(zip(tickerlist["ticker"], tickerlist["sector"]))
print("\nSector map:")
print(list(sector_map.items())[:5])

stock_sector_returns = pd.DataFrame({ "Average Returns": avg_returns, "Sector":
                                      avg_returns.index.map(sector_map) })

print(stock_sector_returns.head())

sector_average_returns = stock_sector_returns.groupby("Sector")["Average Returns"].mean()
sector_average_returns = sector_average_returns.sort_values(ascending=False)
print("\nAverage return by sector:")
print(sector_average_returns)

plt.figure(figsize=(10,6))

sector_average_returns.sort_values().plot(kind="barh")

plt.title("Average Return by S&P 500 by Sector")
plt.xlabel("Average Return")
plt.ylabel("Sector")

plt.show()

#checking missing values

print("\nMissing values in returns:")
print(returns.isnull().sum().sum())

print("\nMissing values in ticker list:")
print(tickerlist.isnull().sum())

print("\nDuplicare rows in returns:")
print(returns.duplicated().sum())

print("\nDuplicate rows in ticker list:")
print(tickerlist.duplicated().sum())

    










































































































































































































































































































































































































































































































































































































































































































