# Portfolio allocation backtesting

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

weighting1 = {"BTC-USD": "1", "SPY": "99"}
weighting2 = {"BTC-USD": "3", "SPY": "97"}
weighting3 = {"BTC-USD": "3", "SPY": "95", "ETH-USD": "2"}

members = ["BTC-USD", "SPY", "ETH-USD"]

def PortfolioCalc(weightings, data, name):
	data[name] = sum([ int(weightings[x]) * data[x]/100 
				 for x in list(weightings.keys()) ])
	return data

basedata = yf.Ticker(members[0]).history(period="max").reset_index()[["Date", "Open"]]

basedata["Date"] = pd.to_datetime(basedata["Date"])

basedata = basedata.rename(columns = {"Open":members[0]});

print(basedata)


if(len(members)>1):
	for x in range (1, len(members)):

		newdata = yf.Ticker(members[x]).history(period="max").reset_index()[["Date", "Open"]]

		newdata["Date"] = pd.to_datetime(newdata["Date"])

		newdata = newdata.rename(columns = {"Open":members[x]});

		basedata = pd.merge(basedata, newdata, on="Date");

basedata = basedata[basedata["Date"] > "2016-01-01"]

for x in members:
	basedata[x] = basedata[x]/(basedata[x].iloc[0])
	 
basedata = PortfolioCalc(weighting1, basedata, "portfolio1")
basedata = PortfolioCalc(weighting2, basedata, "portfolio2")
basedata = PortfolioCalc(weighting3, basedata, "portfolio3")

print(basedata)

plt.plot(basedata["Date"], basedata["portfolio1"], label = "portfolio1")
plt.plot(basedata["Date"], basedata["portfolio2"], label = "portfolio2")
plt.plot(basedata["Date"], basedata["portfolio3"], label = "portfolio3")

plt.style.use("seaborn")
plt.legend(loc="upper left")
plt.show()
