# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose, Item


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_qualite_positive(self):
        item = Item("foo", 5, 10)
        items = [item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertTrue(item.quality >= 0, "La qualité de l'item doit être positive")

    def test_qualite_limite_max (self):
        item = Item("foo", 5, 10)
        items = [item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertTrue(item.quality <= 50, "La qualité de l'item ne doit pas dépasser 50")

    def test_qualite_sulfuras(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 80)
        items = [item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertTrue(item.quality == 80, "La qualité du Sulfuras doit toujours être de 80")

    def test_peremption_passee(self):
        item = Item("foo", 0, 10)
        items = [item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertTrue(item.quality == 8, "La qualité doit se dégrader deux fois plus vite car la date de péremption est passée")

    def test_aged_brie_updated_quality(self):
        item = Item("Aged Brie", 5, 10)
        items = [item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertTrue(item.quality == 11, "La qualité du Aged Brie augmente plus le temps passe")

    

if __name__ == "__main__":
    unittest.main()

