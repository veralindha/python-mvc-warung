class MenuView(object):
    def formMenu(self):
        minuman = input('input minuman :')
        makanan = input('input makanan :')
        meja = int(input('input alamat :'))

        data = {
            'minuman' : minuman,
            'makanan' : makanan,
            'meja' : meja
        }
        return data
    def pilihPengaturan(self):
        print("[1]. view : \n [2]. exit")
        option = (input('Pilih :'))
        return option
    def tampilMenu(self, data):
        print('minuman' + ":" + str(data['minuman']))
        print('makanan' + ":" + data['makanan'])
        print('meja' + ":" + data['meja'])