from snippets import Snippet
from os.path import dirname
from os import sep
from random import choice
from snippets.shared import get_comments

class CollaborationAndParticipation(Snippet):

  def __init__(self,subject, ancestorTokens = [], children = {}):
    
    self.ownTokens = ['opening', 'listening', 'cname']
    
    #TODO there is nicer syntax for python3
    super(CollaborationAndParticipation, self).__init__(subject, ancestorTokens, children)
    
    commentFile = dirname(__file__) + sep + "comments.csv"
    self.CL = get_comments(commentFile)
    
    
    self.supportedData = []
    
    
  def token_opening(self):
    notes = self.subject.find('notes[@category="collaboration and participation"]')
    
    # Choose the right comment row based on how much the student participated
    row = 0 if len(notes) > 4 else 1
    
    return choice(self.CL[row])
    
  def token_listening(self):
    return choice(self.CL[3])
    
  def token_cname(self):
    if self.subject['cname'] is None:
      return self.subject['fname']
      
    return self.subject['cname']
    
  def is_compatible(cls, subject):
    #TODO Implement This
    pass
    
  def generate_text(self):
    self.text = '/opening '
    
    self.text += '/listening '
