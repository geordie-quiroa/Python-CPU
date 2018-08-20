#parseo el archivo
class data:
    _readMe = open("data.code", 'r').read()
    _predata = _readMe.split('\n')  # crea un array
    _data = []  # cambie _parseData por _data
    for byte in _predata:
        byte = int(byte)
        _data.append(byte)
    n = len(_data)

    def __init__(self):
        self._datosAMemoria = data._data