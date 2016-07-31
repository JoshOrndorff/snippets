from snippets import Snippet
from os.path import dirname
from os import sep
from random import choice
from snippets.shared import get_comments

class EngineeringSkills(Snippet):

  def __init__(self,subject, ancestorTokens = [], children = {}):
    
    self.ownTokens = ['examples', 'cname']
    
    #TODO there is nicer syntax for python3
    super(EngineeringSkills, self).__init__(subject, ancestorTokens, children)
    
    commentFile = dirname(__file__) + sep + "comments.csv"
    self.CL = get_comments(commentFile)
    
    
    self.supportedData = ['cname', 'notes[@"engineering skills"]']
    
    
  def token_examples(self):
    return choice(self.CL[2]) + '[Replace with individual examples] '
    
  def token_cname(self):
    if self.subject['cname'] is None:
      return self.subject['fname']
      
    return self.subject['cname']
    
  def is_compatible(cls, subject):
    #TODO Implement This
    pass
    
  def generate_text(self):
    self.text = self.CL[0][0] + ' '
    
    self.text += '/examples'
    
    self.text += "[Design Challenges] "
    
    self.text += "[Soldering Skills] "
    
    self.text += "[Breadboarding / Debugging] "
    
