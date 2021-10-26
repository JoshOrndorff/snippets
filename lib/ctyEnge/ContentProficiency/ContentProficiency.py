from snippets import Snippet
from os.path import dirname
from os import sep
from random import choice
from snippets.core.shared import get_comments

class ContentProficiency(Snippet):

  def __init__(self,subject, ancestorTokens = [], children = {}):
    
    self.ownTokens = ['opening', 'progression', 'filler', 'cname']
    
    #TODO there is nicer syntax for python3
    super(ContentProficiency, self).__init__(subject, ancestorTokens, children)
    
    commentFile = dirname(__file__) + sep + "comments.csv"
    self.CL = get_comments(commentFile)
    
    
    self.supportedData = ['cname', 'notes[@"content proficiency"]']
    
    
  def token_opening(self):
    return choice(self.CL[0])
    
  def token_progression(self):
    # Assumes number of problems presented is correlated with problem success
    problemsPresented = len(self.subject.find('homework'))
    if problemsPresented < 2:
      return choice(self.CL[3])
    else:
      return choice(self.CL[2])
  
  def token_filler(self):
    # Only insert filler material if there aren't many student-specific notes.
    notes = self.subject.find('notes[@category="content proficiency"]')
    if len(notes) < 3:
      return choice(self.CL[5])
    return ""
  
  def token_cname(self):
    if self.subject['cname'] is None:
      return self.subject['fname']
      
    return self.subject['cname']
    
    
  def is_compatible(cls, subject):
    #TODO Implement This
    pass
    
  def generate_text(self):
    self.text = "/opening "
    
    self.text += "/progression "
    
    self.text += "For example ... [Homework or Design Challenges] [Anything else from notes?]"
    
    self.text += "/filler" # In case there isn't much specific info about the kid.
