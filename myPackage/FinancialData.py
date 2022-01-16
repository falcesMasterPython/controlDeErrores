## Datos Financieros
"""
En este módulo tenemos la clase para tratar la información financiera de ingresos y gastos de un año.
"""
import pandas as pd
from myPackage.Error import *
import os


## Clase FinancialData
"""
Herramientas para la gestión de datos financieros:

- **Carga de datos**: Valida el data de entrada o toma uno por defecto (ir al método en [[FinancialData.py#setdataframe]]).
- **Validación y corrección de datos**: revisa los datos y modifica los incorrectos.
- **Impresión de resultados**: Muestra los resultados del análisis por pantalla (ir al método en [[FinancialData.py#printresults]]).

Utilizamos la clase [[Error.py]] y sus herederas para gestionar las Excepciones.
"""
class FinancialData:
    ## Constructor
    """
    Se setean las propiedades del objeto y la ruta donde se localiza este archivo.
    """
    def __init__(self):
        self.file = None
        self.totalIncoming = None
        self.totalOutcoming = None
        self.outcomingAverage = None
        self.minOutcomingMonth = None
        self.minOutcomingAmount = None
        self.maxOutcomingMonth = None
        self.maxOutcomingAmount = None
        self.df = None

        """
        Con la librería OS definimos la ruta desde donde se ubica este archivo para poder acceder al archivo 
        por defecto, si se requiere.
        """
        self.dirname = os.path.dirname(__file__)

    # === setDataFrame ===
    def setDataFrame(self, data='../data/finanzas2020.csv'):
        """
        Parámetros:

        - data (str, dict)
        """
        try:
            """
            Carga y valida el origen de datos. Si no se especifica el parámetro, se carga el archivo de datos ./data/finanzas2020.csv
            """
            if type(data) == str:
                data = os.path.join(self.dirname, data)
                self.file = data
                self.df = self.getDataFrameFromCSV(self.file)
            elif type(data) == dict:
                self.df = data
            else:
                raise DataTypeNotAllowed(type(data))

            """
            Genera el DataFrame con Pandas. Analiza su contenido. Los datos erróneos o inexistentes se tratarán como cero.
            """
            self.prepareDataFrame()

            """
            Validamos que el dataFrame tenga doce columnas (una para cada mes).
            """
            if self.checkTwelveColumnsInDataFrame() is False:
                self.file = None
                raise CSVHasNotTwelveColumns(self.file)

            """
            Comprobamos los datos de cada columna:
            
            1. Todas las columnas tienen que tener datos
            2. Los datos deben ser numéricos. Los datos no numéricos se setean a cero.
            """
            self.checkAllMonthsHaveData()
            self.checkValues()
        except Error as e:
            print(e)

    def getDataFrameFromCSV(self, file):
        try:
            return pd.read_csv(file, sep='\t')
        except Exception as e:
            self.file = None
            raise FinnancialFileNotFound(e)

    def prepareDataFrame(self):
        try:
            self.df = pd.DataFrame(self.df)
        except Exception as e:
            raise CantCreateDataFrame(e)

    def checkTwelveColumnsInDataFrame(self):
        if len(self.df.columns) == 12:
            return True
        return False

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
                    except:
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

    # === printResults ===
    def printResults(self):
        """
        Muestra los datos por pantalla:

        - Mes con mayor gasto
        - Mes con menos gasto
        - Media de gasto anual
        - Total de gastos
        - Total de ingresos
        """
        try:
            if self.file is None:
                raise Exception('No hay datos')
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
        except Exception as e:
            print(e)

### Ejecución del script
if __name__ == '__main__':
    financialData = FinancialData()
    financialData.setDataFrame()
    financialData.printResults()
