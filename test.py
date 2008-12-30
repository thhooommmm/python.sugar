import sys,io

class TestPy(object):
  def __init__(self):
    test_regex = r'[0-9]{2,4}.\{'
    test_single_quote = 'single quote string'
    test_single_quote = u'single quote string'
    test_single_quote = '''single
                           quote
                           string'''
    test_single_quote = u'''single
                           quote
                           string'''
    test_double_quote = "double quote string"
    test_double_quote = u"double quote string"
    test_double_quote = """double
                           quote
                           string"""
    test_double_quote = u"""double 
                            quote 
                            string"""