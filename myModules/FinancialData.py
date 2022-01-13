import pandas as pd
from myModules.Error import *


class FinancialData:

    def __init__(self):
        self.df = None
        try:
            self.errorOnLoad = None

            self.file = 'data/finanzas2020.csv'

            self.getDataFrameFromCSV()

            self.prepareDataFrame()

            self.checkTwelveColumnsInDataFrame()
            self.checkAllMonthsHaveData()
            self.checkValues()

            self.maxOutcomingAmount = self.getMaxOutcomingAmount()
            self.maxOutcomingMonth = self.getMaxOutcomingMonth()

            self.minOutcomingAmount = self.getMinOutcomingAmount()
            self.minOutcomingMonth = self.getMinOutcomingMonth()

            self.outcomingAverage = self.getOutcomingAverage()

            self.totalOutcoming = self.getTotalOutcoming()
            self.totalIncoming = self.getTotalIncoming()
        except Error as e:
            print(e)

    def getDataFrameFromCSV(self):
        try:
            self.df = pd.read_csv(self.file, sep='\t')
        except Exception as e:
            raise FinnancialFileNotFound(e)

    def prepareDataFrame(self):
        try:
            self.df = pd.DataFrame(self.df)
        except Exception as e:
            raise CantCreateDataFrame(e)

    def checkTwelveColumnsInDataFrame(self):
        if len(self.df.columns) != 12:
            raise CSVHasNotTwelveColumns(self.file)

    def checkAllMonthsHaveData(self):
        for i in self.df.index:
            for c in self.df.columns:
                if pd.isna(self.df.loc[i, c]):
                    self.df.loc[i, c] = 0

    def checkValues(self):
        for i in self.df.index:
            for c in self.df.columns:
                value = self.df.loc[i, c]
                if type(value) == str:
                    try:
                        value = float(value)
                    except Exception:
                        value = 0
                    finally:
                        self.df.loc[i, c] = value

    def getMaxOutcomingAmount(self):
        try:
            return self.df.sum().sort_values(ascending=False).head(n=1).iloc[0]
        except Exception as e:
            raise CantGetMaxOutcomingAmount(e)

    def getMaxOutcomingMonth(self):
        try:
            return self.df.sum().sort_values(ascending=False).head(n=1).index[0]
        except Exception as e:
            raise CantGetMaxOutcomingMonth(e)

    def getMinOutcomingAmount(self):
        try:
            return self.df.sum().sort_values(ascending=True).head(n=1).iloc[0]
        except Exception as e:
            raise CantGetMinOutcomingAmount(e)

    def getMinOutcomingMonth(self):
        try:
            return self.df.sum().sort_values(ascending=True).head(n=1).index[0]
        except Exception as e:
            raise CantGetMinOutcomingMonth(e)

    def getOutcomingAverage(self):
        try:
            return self.df.sum().mean()
        except Exception as e:
            raise CantGetOutcomingAverage(e)

    def getTotalOutcoming(self):
        try:
            return self.df.iloc[:, 1:].where(self.df.iloc[:, 1:] < 0).sum(axis=1).sum()
        except Exception as e:
            raise CantGetTotalOutcoming(e)

    def getTotalIncoming(self):
        try:
            return self.df.iloc[:, 1:].where(self.df.iloc[:, 1:] >= 0).sum(axis=1).sum()
        except Exception as e:
            raise CantGetTotalIncoming(e)

    def printResults(self):
        try:
            print(f"El mes que más se ha gastado ha sido {self.maxOutcomingMonth} ({self.maxOutcomingAmount})")
            print(f"El mes que menos se ha gastado ha sido {self.minOutcomingMonth} ({self.minOutcomingAmount})")
            print(f"La media de gasto mensual ha sido {self.outcomingAverage}")
            print(f"El total de gastos ha sido {self.totalOutcoming}")
            print(f"El total de ingresos ha sido {self.totalIncoming}")
        except Exception as e:
            print('Error:', e)


if __name__ == '__main__':
    financialData = FinancialData()
    financialData.printResults()
