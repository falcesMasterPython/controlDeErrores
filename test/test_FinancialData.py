import unittest
import sys

sys.path.append("..")

from myModules.FinancialData import FinancialData


class FinancialDataTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(FinancialDataTest, self).__init__(*args, **kwargs)

        self.dataFrame1 = {
            'Enero': [10.01, 20.01, 30.01, 40.01, 50.01],
            'Febrero': [10.02, 20.02, 30.02, 40.02, 50.02],
            'Marzo': [10.03, 20.03, 30.03, 40.03, 50.03],
            'Abril': [10.04, 20.04, 30.04, 40.04, 50.04],
            'Mayo': [10.05, 20.05, 30.05, 40.05, 50.05],
            'Junio': [10.06, 20.06, 30.06, 40.06, 50.06],
            'Julio': [10.07, 20.07, 30.07, 40.07, 50.07],
            'Agosto': [10.08, 20.08, 30.08, 40.08, 50.08],
            'Septiembre': [10.09, 20.09, 30.09, 40.09, 50.09],
            'Octubre': [10.10, 20.10, 30.10, 40.10, 50.10],
            'Noviembre': [10.11, 20.11, 30.11, 40.11, 50.11],
            'Diciembre': [10.12, 20.12, 30.12, 40.12, 50.12],
        }

        self.dataFrame2 = {
            'Enero': [10.01, 20.01, 30.01, 40.01, 50.01],
            'Febrero': [10.02, 20.02, 30.02, 40.02, 50.02],
            'Marzo': [10.03, 20.03, 30.03, 40.03, 50.03],
            'Abril': [10.04, 20.04, 30.04, 40.04, 50.04],
            'Mayo': [10.05, 20.05, 30.05, 40.05, 50.05],
            'Junio': [10.06, 20.06, 30.06, 40.06, 50.06],
            'Julio': [10.07, 20.07, 30.07, 40.07, 50.07],
            'Agosto': [10.08, 20.08, 30.08, 40.08, 50.08],
            'Septiembre': [10.09, 20.09, 30.09, 40.09, 50.09],
            'Octubre': [10.10, 20.10, 30.10, 40.10, 50.10],
            'Noviembre': [10.11, 20.11, 30.11, 40.11, 50.11],
        }

    def test_checkTwelveColumnsInDataFrame(self):
        self.financialData = FinancialData()
        self.financialData.setDataFrame(self.dataFrame1)

        self.assertTrue(
            self.financialData.checkTwelveColumnsInDataFrame()
        )

        self.financialData.setDataFrame(self.dataFrame2)

        self.assertRaises(CSVHasNotTwelveColumns)

        self.assertTrue('This is broken' in str(context.exception))




if __name__ == '__main__':
    unittest.main()
