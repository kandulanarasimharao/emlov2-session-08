import unittest

import requests
import json
import base64
from requests import Response
import pytest

@pytest.mark.usefixtures("pass_parameters")
class TestCIFAR(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("executed")
        cls.image_paths = ["./cifar10_test_data/airplane.png","./cifar10_test_data/automobile.png","./cifar10_test_data/bird.png","./cifar10_test_data/cat.png","./cifar10_test_data/deer.png","./cifar10_test_data/dog.png","./cifar10_test_data/frog.png","./cifar10_test_data/horse.png","./cifar10_test_data/ship.png","./cifar10_test_data/truck.png"]
    
    
    def test_predict(self):
        #ServerPublicAddress="svecw.ai"
        #print(self.ServerPublicAddress)
        for image_path in self.image_paths:
            with open(image_path, 'rb') as file:
                image=image_path.split("/")[2]
                print(f"using the URL : http://"+self.ServerPublicAddress+":8080/predictions/"+self.ModelName+"/1.0")
                print(f"testing: {image}")
                
                response: Response = requests.request("POST", "http://localhost:8080/predictions/cifar/1.0", files={'data': file})
                print(f"response: {response.text}")

                data = response.json()
                predicted_label=list(data.keys())[0]
                print(f"predicted label: {predicted_label}")

                self.assertEqual((image_path.split("/")[2]).split(".")[0], predicted_label)

                print(f"done testing: {image}")
                print()
            
if __name__ == '__main__':
    unittest.main()