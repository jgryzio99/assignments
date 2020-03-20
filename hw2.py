from typing import List
import pandas as pd
import datetime
import os

# confirmed cases
url = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/a9f182afe873ce7e65d2307fcf91013c23a4556c" \
      f"/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"
dfC = pd.read_csv(url, error_bad_lines=False)

# deaths
url = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/a9f182afe873ce7e65d2307fcf91013c23a4556c" \
      f"/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv"
dfD = pd.read_csv(url, error_bad_lines=False)

# recovered cases
url = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/a9f182afe873ce7e65d2307fcf91013c23a4556c" \
      f"/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv"
dfR = pd.read_csv(url, error_bad_lines=False)


# Helper function (strftime not cross platform) ???
def format_date(date: datetime.date):
    if os.name == "nt":
        return date.strftime('%#m/%#d/%y')
    else:
        return date.strftime('%-m/%-d/%y')


def countries_with_no_deaths_count(date: datetime.date):
      data1 = format_date(date)
      count = 0
      for i in range(459):
            if (dfD[data1].values[i] == 0 and dfC[data1].values[i]>0):
                  count+=1
      result = count
      return result


def more_cured_than_deaths_indices(date: datetime.date):
      data1 = format_date(date)
      result = np.where(dfR[data1]>dfD[data1])
      result = list(result)
      return result
