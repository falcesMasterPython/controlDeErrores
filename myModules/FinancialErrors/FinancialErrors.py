class FinancialErrors(Exception):
    def __init__(self, error, origin='Exception'):
        errorMessage = str(error)

        top = '┌'
        messageText = '| Error (' + origin + '): ' + errorMessage + ' |\n'
        bottom = '└'

        messageLength = len(messageText)

        for i in range(3, messageLength):
            top += '-'
            bottom += '-'

        top += '┐\n'
        bottom += '┘\n'

        super().__init__(top + messageText + bottom)

    def getName(self):
        return self.__class__.__name__


class FinnancialFileNotFound(FinancialErrors):
    def __init__(self, error):
        errorMessage = f'No se puede leer el archivo CSV: {error}'
        super().__init__(errorMessage, self.getName())

class NoFinancialData(FinancialErrors):
    def __init__(self):
        errorMessage = 'No hay datos'
        super().__init__(errorMessage, self.getName())


class CantCreateDataFrame(FinancialErrors):
    def __init__(self, error):
        errorMessage = f'No puedo crear el DataFrame: {error}'
        super().__init__(errorMessage, self.getName())


class CantGetMaxOutcomingAmount(FinancialErrors):
    def __init__(self, error):
        super().__init__(error, self.getName())


class CantGetMaxOutcomingMonth(FinancialErrors):
    def __init__(self, error):
        super().__init__(error, self.getName())


class CantGetMinOutcomingAmount(FinancialErrors):
    def __init__(self, error):
        super().__init__(error, self.getName())


class CantGetMinOutcomingMonth(FinancialErrors):
    def __init__(self, error):
        super().__init__(error, self.getName())


class CantGetOutcomingAverage(FinancialErrors):
    def __init__(self, error):
        super().__init__(error, self.getName())


class CantGetTotalOutcoming(FinancialErrors):
    def __init__(self, error):
        super().__init__(error, self.getName())


class CantGetTotalIncoming(FinancialErrors):
    def __init__(self, error):
        super().__init__(error, self.getName())


class CSVHasNotTwelveColumns(FinancialErrors):
    def __init__(self, file):
        errorMessage = f"El documento {file} no tiene 12 columnas"
        super().__init__(errorMessage, self.getName())


class EmptyField(FinancialErrors):
    def __init__(self, field):
        errorMessage = f'El campo {field} no tiene datos'
        super().__init__(errorMessage, self.getName())


class DataTypeNotAllowed(FinancialErrors):
    def __init__(self, type):
        errorMessage = f'El tipo de datos {type} no está soportado'
        super().__init__(errorMessage, self.getName())
