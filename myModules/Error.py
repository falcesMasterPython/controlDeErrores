class Error(Exception):
    def __init__(self, error, origin = 'Exception'):

        errorMessage = str(error)

        top = '┌'
        messageText = '| Error (' + origin + '): ' + errorMessage + ' |\n'
        bottom = '└'

        messageLength = len(messageText)

        for i in range(3,messageLength):
            top    += '-'
            bottom += '-'

        top    += '┐\n'
        bottom += '┘\n'

        super().__init__(top + messageText + bottom)

    def getName(self):
        return self.__class__.__name__

class FinnancialFileNotFound(Error):
    def __init__(self, error):
        errorMessage = f'No se puede leer el archivo CSV: {error}'
        super().__init__(errorMessage, self.getName())

class CantCreateDataFrame(Error):
    def __init__(self, error):
        errorMessage = f'No puedo crear el DataFrame: {error}'
        super().__init__(errorMessage, self.getName())

class CantGetMaxOutcomingAmount(Error):
    def __init__(self, error):
        super().__init__(error, self.getName())

class CantGetMaxOutcomingMonth(Error):
    def __init__(self, error):
        super().__init__(error, self.getName())

class CantGetMinOutcomingAmount(Error):
    def __init__(self, error):
        super().__init__(error, self.getName())

class CantGetMinOutcomingMonth(Error):
    def __init__(self, error):
        super().__init__(error, self.getName())

class CantGetOutcomingAverage(Error):
    def __init__(self, error):
        super().__init__(error, self.getName())

class CantGetTotalOutcoming(Error):
    def __init__(self, error):
        super().__init__(error, self.getName())

class CantGetTotalIncoming(Error):
    def __init__(self, error):
        super().__init__(error, self.getName())

class CSVHasNotTwelveColumns(Error):
    def __init__(self, file):
        errorMessage = f"El documento {file} no tiene 12 columnas"
        super().__init__(errorMessage, self.getName())

class EmptyField(Error):
    def __init__(self, campo):
        errorMessage = f'El campo {campo} no tiene datos'
        super().__init__(errorMessage, self.getName())