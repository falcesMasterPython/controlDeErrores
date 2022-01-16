## Clase Error
"""
Esta es la clase padre para imprimir por pantalla las excepciones lanzadas en [[FinancialData.py]]
"""


class Error(Exception):
    ## Constructor
    """
    - Recibe el comentario a mostrar por pantalla
    - Recibe el nombre de la excepción hija (opcional) (ver método en [[Error.py#getname]]).
    - Crea un cuadro en formato ASCII para imprimir en pantalla
    """
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

    # === getName ===
    def getName(self):
        """
        Devuelve un string con el nombre de la clase que ejecuta el método.
        """
        return self.__class__.__name__


### FinnancialFileNotFound
class FinnancialFileNotFound(Error):
    """
    Hereda de Error, se lanza cuando no se puede leer el archivo CSV especificado.
    """
    def __init__(self, error):
        errorMessage = f'No se puede leer el archivo CSV: {error}'
        super().__init__(errorMessage, self.getName())

### CantCreateDataFrame
class CantCreateDataFrame(Error):
    """
    Hereda de Error, se lanza cuando no se puede crear el data frame a partir de los datos dados.
    """
    def __init__(self, error):
        errorMessage = f'No puedo crear el DataFrame: {error}'
        super().__init__(errorMessage, self.getName())

### CantGetMaxOutcomingAmount
class CantGetMaxOutcomingAmount(Error):
    """
    Hereda de Error, se lanza cuando no se puede calcular la mayor cantidad de gasto.
    """
    def __init__(self, error):
        super().__init__(error, self.getName())

### CantGetMaxOutcomingMonth
class CantGetMaxOutcomingMonth(Error):
    """
    Hereda de Error, se lanza cuando no se puede especificar el mes de mayor gasto.
    """
    def __init__(self, error):
        super().__init__(error, self.getName())

### CantGetMinOutcomingAmount
class CantGetMinOutcomingAmount(Error):
    """
    Hereda de Error, se lanza cuando no se puede calcular la menor cantidad de gasto.
    """
    def __init__(self, error):
        super().__init__(error, self.getName())

### CantGetMinOutcomingMonth
class CantGetMinOutcomingMonth(Error):
    """
    Hereda de Error, se lanza cuando no se puede leer el archivo CSV especificado.
    """
    def __init__(self, error):
        super().__init__(error, self.getName())

### CantGetOutcomingAverage
class CantGetOutcomingAverage(Error):
    """
    Hereda de Error, se lanza cuando no se puede leer el archivo CSV especificado.
    """
    def __init__(self, error):
        super().__init__(error, self.getName())

### CantGetTotalOutcoming
class CantGetTotalOutcoming(Error):
    """
    Hereda de Error, se lanza cuando no se puede especificar el mes de menor gasto.
    """
    def __init__(self, error):
        super().__init__(error, self.getName())

### CantGetTotalIncoming
class CantGetTotalIncoming(Error):
    """
    Hereda de Error, se lanza cuando no se puede calcular el total de gastos.
    """
    def __init__(self, error):
        super().__init__(error, self.getName())

### CSVHasNotTwelveColumns
class CSVHasNotTwelveColumns(Error):
    """
    Hereda de Error, se lanza cuando el dataframe generado no tiene doce columnas.
    """
    def __init__(self, file):
        errorMessage = f"El documento {file} no tiene 12 columnas"
        super().__init__(errorMessage, self.getName())

### EmptyField
class EmptyField(Error):
    """
    Hereda de Error, se lanza cuando hay algún campo en blanco.
    """
    def __init__(self, field):
        errorMessage = f'El campo {field} no tiene datos'
        super().__init__(errorMessage, self.getName())

### DataTypeNotAllowed
class DataTypeNotAllowed(Error):
    """
    Hereda de Error, se lanza cuando no el tipo de datos de entrada no está especificado.
    """
    def __init__(self, dataType):
        errorMessage = f'El tipo de datos {dataType} no está soportado'
        super().__init__(errorMessage, self.getName())
