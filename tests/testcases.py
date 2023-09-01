import unittest
import requests
import json

class testapi(unittest.TestCase):
    def setUp(self):
        self.url = 'http://192.168.29.26:8008/api/get_float?text='  
        self.token = 'jwt-token'  

    def test_api_response(self):
        data = 'My name is Abhilash Kumar Pulikonda.'
        headers = {'Authorization': f'Bearer {self.token}'}
        print(self.url+f"?text={data}")
        response = requests.post(self.url+f"{data}", json=data)#, headers=headers)

        self.assertEqual(response.status_code, 200) # Check if it is getting response successfully
        result = json.loads(response.text)
        float_array = result.get('result')
        # print(float_array)

        self.assertIsInstance(float_array, list) # check if type of output 
        self.assertEqual(len(float_array), 500)  # check for length of array 
        self.assertTrue(all(isinstance(i, float) for i in float_array))  # check if they are float values

if __name__ == '__main__':
    unittest.main()
