#mahasiswa
class WarungModel(object):
    def __init__(self, minuman, makanan, meja):
        self.minuman = minuman
        self.makanan = makanan
        self.meja = meja
    def getminuman(self):
        return self.minuman
    def setminuman(self, minuman):
        self.minuman = minuman
    def getmakanan(self):
        return self.makanan
    def setmakanan(self, makanan):
        self.makanan = makanan
    def getmeja(self):
        return self.meja
    def setmeja(self, meja):
        self.meja = meja
    def getAll(self):
        data = {
            'minuman' : 'Es teh',
            'makanan' : 'Nasi goreng',
            'meja' : '4'
        }
        return data