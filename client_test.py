import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))


  """ ------------ Add more unit tests ------------ """

  def test_getRatio_priceBZero(self):
    # Test when price B is zero
    price_a = 10
    price_b = 0
    ratio = getRatio(price_a, price_b)
    self.assertEqual(ratio, 0)

  def test_getRatio_priceAZero(self):
    # Test when price A is zero
    price_a = 0
    price_b = 10
    ratio = getRatio(price_a, price_b)
    self.assertEqual(ratio, 0)

  def test_getRatio_bothPricesZero(self):
    # Test when both prices are zero
    price_a = 0
    price_b = 0
    ratio = getRatio(price_a, price_b)
    self.assertEqual(ratio, 0)

  def test_getRatio_priceAGreaterThanB(self):
    # Test when price A is greater than price B
    price_a = 20
    price_b = 10
    ratio = getRatio(price_a, price_b)
    self.assertEqual(ratio, price_a / price_b)

  def test_getRatio_priceBGreaterThanA(self):
    # Test when price B is greater than price A
    price_a = 10
    price_b = 20
    ratio = getRatio(price_a, price_b)
    self.assertEqual(ratio, price_a/price_b)


if __name__ == '__main__':
    unittest.main()
