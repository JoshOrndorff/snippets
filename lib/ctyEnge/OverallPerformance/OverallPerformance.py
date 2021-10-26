from snippets import Snippet
from os.path import dirname
from os import sep
from random import choice
from snippets.core.shared import get_comments

class OverallPerformance(Snippet):

  def __init__(self, subject, ancestorTokens = [], children = {}):
    
    self.ownTokens = ['adj', 'cname', 'notebook', 'body']
    
    super().__init__(subject, ancestorTokens, children)
    
    commentFile = dirname(__file__) + sep + "comments.csv"
    self.CL = get_comments(commentFile)
    
    # set an overall int to represent completion
    if self.subject['completion'] == "successfully completing":
      self.comp = 3
    elif self.subject['completion'] == "completing":
      self.comp = 2
    else:
      self.comp = 1
    
    self.supportedData = ['completion',
                          'notebook[@check="1"]',
                          'notebook[@check="2"]',
                          'cname',
                          'fname']
    
    
  def token_adj(self):
    options = self.CL[3 - self.comp] 
    return choice(options)
    
  def token_cname(self):
    if self.subject['cname'] is None:
      return self.subject['fname']
      
    return self.subject['cname']
    
  def token_notebook_numeric(self):
    ''' This technique was used with percentage based grades, it is now replaced
    with metric prefix based grades. '''
    nb1 = int(self.subject['notebook[@check="1"]'])
    nb2 = int(self.subject['notebook[@check="2"]'])

    if nb1 >= 90 and nb2 >= 90:
      options = self.CL[4]
    elif nb1 < 80 and nb2 >= 90:
      options = self.CL[5]
    elif nb1 < 70 and nb2 < 70:
      options = self.CL[6]
    else:
      return ""

    return choice(options)
  
  def token_notebook(self):
    
    nb1 = self.subject['notebook[@check="1"]']
    nb2 = self.subject['notebook[@check="2"]']
    
    good = ['base', 'k', 'M', 'G']
    bad  = ['n', 'u', 'm']

    if nb1 in good and nb2 in good:
      options = self.CL[4]
    elif nb1 not in good and nb2 in good:
      options = self.CL[5]
    elif nb1 in bad and nb2 in bad:
      options = self.CL[6]
    else:
      return ""

    return choice(options)
    
  def token_body(self):
    return choice(self.CL[8])
    
  def is_compatible(cls, subject):
    #TODO Implement This
    pass
    
  def generate_text(self):
    self.text = "Your " if choice([True, False]) else "/cname, your "
    self.text += "performance in class was /adj. "
    
    self.text += "/body "
    
    self.text += "/notebook"
    
    
