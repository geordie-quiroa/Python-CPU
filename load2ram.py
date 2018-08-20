#parseo el archivo
class data:
    _readMe = open("RAM.code", 'r').read()
    _predata = _readMe.split('\n')  # asigna a cada linea del archivo, una posicion en el arreglo privado _predata
    _data = []  #en este arrreglo voy a tener lo de _predata ya como integers
    for byte in _predata:
        byte = int(byte)
        _data.append(byte)
    n = len(_data)

    def __init__(self):
        self._datosAMemoria = data._data