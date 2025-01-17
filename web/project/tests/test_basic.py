# project/test_basic.py


import os
import unittest

from project import app, db


TEST_DB = 'test.db'


class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(app.config['BASEDIR'], TEST_DB)
        self.app = app.test_client()

    # executed after each test
    def tearDown(self):
        pass


    def test_fill_database(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        
    def test_eight_queen_puzzle(self)  
        result = self.app.get('/get/4')
        #print result.data     
        self.assertIn('[[1, 3, 0, 2], [2, 0, 3, 1]]',result.data)

  
if __name__ == "__main__":
    unittest.main()
