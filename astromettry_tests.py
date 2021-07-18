import unittest

import photometry
import numpy as np
from PIL import Image
import logging
class Tests_findsources(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger(__name__)
        logger.debug(("mlikdifmlkqsdjlmkfqdmlkfqsmlkfqsmfqsdljfqsdkl"))


    def test_something(self):
        img1 = "sample_images/DSC01651.JPG"
        with Image.open(img1) as image:
            imonoc = image.convert('1')
            pix = np.array(imonoc)

        photometry.find_sources(pix, 1.5)



if __name__ == '__main__':

    unittest.main()
