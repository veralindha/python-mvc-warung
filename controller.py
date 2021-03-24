from model import WarungModel
from view import MenuView


class WarungController(object):
    def createPesanan(self):
        view = MenuView()
        data = view.formMenu()

        return data

    def tampil(self, data):
        view = MenuView()
        option = view.pilihPengaturan()

        if option == '1':
            self.viewMenu(data)
        elif option == '2':
            print('stop')
        else:
            print('404 error')
            self.tampil(data)

    def viewMenu(self, data):
        view = MenuView()
        view.tampilMenu(data)

        self.tampil(data)

    def run(self):
        register = self.createPesanan()
        minuman = register['minuman']
        makanan = register['makanan']
        meja = register['meja']

        data = WarungModel(minuman, makanan, meja)

        datamenu = data.getAll()
        self.tampil(datamenu)