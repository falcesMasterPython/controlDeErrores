import pandas as pd
from FinancialErrors.FinancialErrors import *

class FinancialData:

    def __init__(self, data=None):

        if data == None:
            self.data = 'data/finanzas2020.csv'
        else:
            self.data = data

        self.df = None

        self.totalIncoming = None
        self.totalOutcoming = None
        self.outcomingAverage = None
        self.minOutcomingMonth = None
        self.minOutcomingAmount = None
        self.maxOutcomingMonth = None
        self.maxOutcomingAmount = None

        self.setDataFrame()

    def setDataFrame(self):
        try:
            if type(self.data) is None:
                raise DataTypeNotAllowed(type(self.data))
            elif type(self.data) == str:
                self.df = self.getDataFrameFromCSV(self.data)
            elif type(self.data) == dict:
                self.df = self.data
            else:
                self.data = None
                raise DataTypeNotAllowed(type(self.data))
            self.df = pd.DataFrame(self.df)
        except FinancialErrors as e:
            print(e)

    def getDataFrameFromCSV(self, file):
        try:
            return pd.read_csv(file, sep='\t')
        except Exception as e:
            self.data = None
            raise FinnancialFileNotFound(e)

    def checkDataFrame(self):
        try:
            if(self.data != None):
                if self.checkTwelveColumnsInDataFrame() is False:
                    self.data = None
                    raise CSVHasNotTwelveColumns(self.file)

                if self.checkAllMonthsHaveData() is False:
                    self.addZeroToEmptyData()

                self.checkValues()
            else:
                raise FinnancialFileNotFound('No hay datos')
        except FinancialErrors as e:
            print(e)

    def checkTwelveColumnsInDataFrame(self):
        if len(self.df.columns) == 12:
            return True
        return False

    def checkAllMonthsHaveData(self):
        for i in self.df.index:
            for c in self.df.columns:
                # print('Valor:', self.df.loc[i, c], type(self.df.loc[i, c]))
                # if pd.isna(self.df.loc[i, c]):
                if self.df.loc[i, c] == '':
                    print('Valor:', self.df.loc[i, c], type(self.df.loc[i, c]))
                    return False
        return True

    def addZeroToEmptyData(self):
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
            if self.data is None:
                raise NoFinancialData()
            else:
                self.maxOutcomingAmount = self.getMaxOutcomingAmount()
                self.maxOutcomingMonth = self.getMaxOutcomingMonth()
                self.minOutcomingAmount = self.getMinOutcomingAmount()
                self.minOutcomingMonth = self.getMinOutcomingMonth()
                self.outcomingAverage = self.getOutcomingAverage()
                self.totalOutcoming = self.getTotalOutcoming()
                self.totalIncoming = self.getTotalIncoming()

                print(f"El mes que más se ha gastado ha sido {self.maxOutcomingMonth} ({self.maxOutcomingAmount})")
                print(f"El mes que menos se ha gastado ha sido {self.minOutcomingMonth} ({self.minOutcomingAmount})")
                print(f"La media de gasto mensual ha sido {self.outcomingAverage}")
                print(f"El total de gastos ha sido {self.totalOutcoming}")
                print(f"El total de ingresos ha sido {self.totalIncoming}")
        except FinancialErrors as e:
            print(e)


if __name__ == '__main__':
    from FinancialErrors.FinancialErrors import *
    financialData = FinancialData('../data/finanzas2020a.csv')
    financialData.setDataFrame()
    financialData.checkDataFrame()
    financialData.printResults()
