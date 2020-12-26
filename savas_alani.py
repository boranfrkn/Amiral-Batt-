class SavasAlani:
    def __init__(self, n_satir, n_sutun):
        self.n_satir = n_satir
        self.n_sutun = n_sutun
        self.savas_alani = self.init_savas_alani()
        self.diger_savas_alani = self.init_savas_alani()

    def init_savas_alani(self):
        matris = []
        for satir in range(self.n_satir):
            matris.append(["-"] * self.n_sutun)
        return matris

    def __str__(self):
        kendi_savas_alanim = self.savas_alani_olustur(self.savas_alani)
        diger_savas_alani = self.savas_alani_olustur(self.diger_savas_alani)
        return kendi_savas_alanim
    def savas_alani_olustur(self, savas_alani):
        satir_numaralari = list(range(1, self.n_satir + 1))
        satir_numaralari = list(map(str, satir_numaralari))
        sutun_numaralari = list(range(1, self.n_sutun + 1))
        sutun_numaralari = list(map(str, sutun_numaralari))
        max_sutun_numarasi = len(sutun_numaralari[-1])
        bosluk_str = " " * max_sutun_numarasi
        savas_alani_str = bosluk_str
        for sutun_numarasi in sutun_numaralari:
            bosluk_sayisi = max_sutun_numarasi - len(sutun_numarasi) + 1
            bosluk_str = " " * bosluk_sayisi
            savas_alani_str += sutun_numarasi + bosluk_str
        savas_alani_str += "\n"
        for satir_numarasi in satir_numaralari:
            satir = savas_alani[int(satir_numarasi) - 1]
            satir_str = (max_sutun_numarasi * " ").join(satir)
            if int(satir_numarasi) >= 10:
                savas_alani_str += satir_numarasi + f" {satir_str}\n"
            else:
                savas_alani_str += satir_numarasi + f"  {satir_str}\n"
        return savas_alani_str







savas_alani = SavasAlani(20, 20)
print(savas_alani)
