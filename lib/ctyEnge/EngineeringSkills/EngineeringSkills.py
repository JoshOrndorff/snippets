from snippets import Snippet
from os.path import dirname
from os import sep
from random import choice
from snippets.core.shared import get_comments

class EngineeringSkills(Snippet):

  def __init__(self,subject, ancestorTokens = [], children = {}):
    
    self.ownTokens = ['examples', 'cname', 'challenges']
    
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
  
  def token_challenges(self):
    
    # Get all the challenges they solved
    challenges = self.subject.find('challenges')
    
    # First make sure there are any challenges to speak of
    if len(challenges) == 0:
      return ""
    
    # Sort them into lists based on whether they closed the challenges or not.
    closed = []
    unclosed = []
    for challenge in challenges:
      if challenge.get("closed") in ["True", "true"]:
        closed.append(challenge.text)
      else:
        unclosed.append(challenge.text)
    
    # If they only closed.
    if len(unclosed) == 0:
      comment = "You not only solved, but also publicly presented your solution to many design challenges including "
      for challenge in closed:
        comment += challenge + ', '
    
    # If they didn't close any.
    elif len(closed) == 0:
      comment = "You solved many design challenges including "
      for challenge in unclosed:
        comment += challenge + ', '
    
    # If they closed some but not many, talk about both
    else:
      comment = "You solved many design challenges including "
      for challenge in unclosed:
        comment += challenge + ', '
      
      comment += "and even publicly presented your solution to "
      for challenge in closed:
        comment += challenge + ', '
    
    # We're done here.
    return comment
      
    #######
    for note in notes:
      if xmlStructure:
        note = note.text
      self.document.add_paragraph(note, style='List Bullet')
      
      
  def is_compatible(cls, subject):
    #TODO Implement This
    pass
    
  def generate_text(self):
    self.text = self.CL[0][0] + ' '
    
    self.text += '/examples'
    
    self.text += '/challenges '
    
    self.text += "[Soldering Skills] "
    
    self.text += "[Breadboarding / Debugging] "
    
