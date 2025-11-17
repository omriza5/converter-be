import unittest
from app import app

class CurrencyConverterTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    
    def test_health(self):
        # Arrange + Act
        response = self.client.get("/health")
        
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertIn('status' , response.get_json())
    
    def test_currency_convert(self):
        # Arrange 
        data = {
            "amount" : 10,
            "from":"USD",
            "to":"ILS"
        }
        
        # Act
        response = self.client.post("/convert",json=data)
        
        # Assert
        amount =response.get_json()['amount']
        self.assertEqual(amount, 37.0)
    
        
if __name__ == '__main__':
    unittest.main()