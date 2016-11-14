from os.path import dirname
from os import sep
from random import choice
from snippets.core.shared import get_comments
from snippets import Snippet
from ..LetterGrade import LetterGrade

class Survey2017(Snippet):

  def __init__(self, subject, ancestorTokens = [], children = {}):
    
    # Setup grade as a child
    grade = LetterGrade(subject) #TODO figure out what part of the subject actually needs to be passed here.
    children['grade'] = grade
                     
    # Tokens are replaced in the order specified here.
    self.ownTokens = ['fname', 'cname', 'lname', 'grade', 'course', 'exp']
    
    super().__init__(subject, ancestorTokens, children)
    
    commentFile = dirname(__file__) + sep + "comments.csv"
    self.CL = get_comments(commentFile)
    
    #TODO Why is course even a token. The whole snippet is specifically for this course.
    self.supportedData = ['course',
                          'explanation',
                          'participation',
                          'seemefreq',
                          'fname',
                          'lname',
                          'cname',
                          'grade']
    
    
  def token_fname(self):
    return self.subject['fname']
    
  def token_cname(self):
    if self.subject['cname'] != '':
      return self.subject['cname']
    else:
      return self.subject['fname']
      
  def token_lname(self):
    return self.subject['lname']
  
  def token_course(self):
    return self.subject['course']
  
  def token_exp(self):
    return self.subject['explanation']
    
  
  def is_compatible(cls, subject):
    #TODO Implement This
    pass


  def generate_text(self):
    
    # Student identifying information
    self.text = '/fname /lname\n'
    
    # Opening comment
    self.text += choice(self.CL[0])

    # Second comment if student struggled in a particular area
    if self.subject['explanation'] != '':
      self.text += choice(self.CL[1])
      self.text += choice(self.CL[2])

    # Participation
    self.text += choice(self.CL[6 - int(self.subject['participation'])])
    
    # Homework
    # self.text += choice(self.CL[9 - int(self.subject['homework'])])

    # See me frequently
    self.text += choice(self.CL[12 - int(self.subject['seemefreq'])])
    
    # Conclusion
    self.text += choice(self.CL[12])



