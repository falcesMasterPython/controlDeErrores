import pytest
from myPackage import *
from test.datasets import *

fd = FinancialData()


def test_checkTwelveColumnsInDataFrame_True():
    fd.setDataFrame()
    assert fd.checkTwelveColumnsInDataFrame() is True


def test_checkTwelveColumnsInDataFrame_False():
    fd.setDataFrame(dataFrame_11meses)
    assert fd.checkTwelveColumnsInDataFrame() is False


def test_checkValues_space_is_converted():
    fd.setDataFrame(dataFrame3_datoVacio)
    assert fd.df.iloc[2, 6] is 0
