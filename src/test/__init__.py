import unittest

loader = unittest.TestLoader()
test_suites = loader.discover('.')

runner = unittest.TextTestRunner()
runner.run(test_suites)