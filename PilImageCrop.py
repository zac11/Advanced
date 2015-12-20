__author__ = 'rahul'
 
import unittest
from selenium import webdriver
from PIL import Image
 
 
class ImageCrop(unittest.TestCase):
 
    def setUp(self):
        self.driver = webdriver.Firefox()
 
    def test_ImageCrop(self):
 
        driver = self.driver
        driver.maximize_window()
        driver.get('http://stackoverflow.com/')
        ele = driver.find_element_by_id('hlogo')
 
        #getting element's location
        loc1= ele.location
 
        #getting element's size
        size1= ele.size
 
        #save page's screenshot
        driver.save_screenshot('/home/rahul/Downloads/image1.png')
 
        #open the image using Pillow
        image2 = Image.open('image1.png')
 
        #setting the crop attributes using image's location and size.
        left = loc1['x']
        top = loc1['y']
        right = loc1['x'] + size1['width']
        bottom1 = loc1['y'] + size1['height']
   
        #crop the image using the attributes defined
        image2 = image2.crop((left,top,right,bottom1))
 
        #use the attribute to save image
        image2.save('/home/rahul/Downloads/image2.png')
 
    def tearDown(self):
        self.driver.quit()
 
 
 
if __name__ == '__main__':
    unittest.main()
