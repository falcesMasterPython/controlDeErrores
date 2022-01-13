import unittest
import pandas as pd
from myModules.FinancialData import FinancialData


class FinancialDataTest(unittest.TestCase):
    def __init__(self):
        data = {
            'Enero': [10.1, 20.1, 30.1, 40.1, 50.1],
            'Febrero': [10.2, 20.2, 30.2, 40.2, 50.2],
            'Marzo': [10.3, 20.3, 30.3, 40.3, 50.3],
            'Abril': [10.1, 20.1, 30.1, 40.1, 50.1],
            'Mayo': [10.2, 20.2, 30.2, 40.2, 50.2],
            'Junio': [10.3, 20.3, 30.3, 40.3, 50.3],
            'Julio': [10.1, 20.1, 30.1, 40.1, 50.1],
            'Agosto': [10.2, 20.2, 30.2, 40.2, 50.2],
            'Septiembre': [10.3, 20.3, 30.3, 40.3, 50.3],
            'Octubre': [10.1, 20.1, 30.1, 40.1, 50.1],
            'Noviembre': [10.2, 20.2, 30.2, 40.2, 50.2],
            'Marzo': [10.3, 20.3, 30.3, 40.3, 50.3],
        }
        self.df = pd.DataFrame(data)

        self.financialData = None

    def test_checkTwelveColumnsInDataFrame(self):
        self.financialData = FinancialData()



        self.assertEqual(
            self.financialData.checkTwelveColumnsInDataFrame(),

        )