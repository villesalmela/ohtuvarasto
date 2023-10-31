import unittest
from varasto import Varasto


class TestInvalidVarasto(unittest.TestCase):
    def setUp(self) -> None:
        self.varasto = Varasto(tilavuus=-10, alku_saldo=-11)

    def test_tilavuus_nollattu(self):
        self.assertEqual(self.varasto.tilavuus, 0.0)

    def test_saldo_nollattu(self):
        self.assertEqual(self.varasto.saldo, 0.0)

class TestInvalidVarasto2(unittest.TestCase):
    def setUp(self) -> None:
        self.varasto = Varasto(tilavuus=10, alku_saldo=11)

    def test_saldo_oikein(self):
        self.assertEqual(self.varasto.saldo, 10.0)

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_tyhja_lisays(self):
        self.varasto.lisaa_varastoon(maara=-10)
        self.assertEqual(self.varasto.saldo, 0)

    def test_liian_paljon_lisays(self):
        self.varasto.lisaa_varastoon(maara=100)
        self.assertEqual(self.varasto.saldo, 10)

    def test_ota_liikaa(self):
        self.varasto.lisaa_varastoon(maara=10)
        self.assertEqual(self.varasto.ota_varastosta(100), 10)

    def test_ota_neg(self):
        self.varasto.lisaa_varastoon(maara=10)
        self.assertEqual(self.varasto.ota_varastosta(-10), 0.0)

    def test_print(self):
        self.varasto.lisaa_varastoon(7)
        self.assertEqual(str(self.varasto), "saldo = 7, vielä tilaa 3")