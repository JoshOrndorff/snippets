from os.path import dirname
from os import sep
from random import choice
from snippets.core.shared import get_comments
from snippets import Snippet

class Cocurricular(Snippet):

  def __init__(self, subject, ancestorTokens = [], children = {}):
    
    # Tokens are replaced in the order specified here.
    #TODO This list feels redundant since I've defined functions / children for all tokens.
    self.ownTokens = ['fname', 'lname', 'grade', 'course', 'effort', 'strength', 'weakness', 'prestopic', 'nextbot']
    
    super().__init__(subject, ancestorTokens, children)
    
    commentFile = dirname(__file__) + sep + "CocurricularComments.csv"
    self.CL = get_comments(commentFile)
    
    self.supportedData = ['course',
                          'strength',
                          'weakness',
                          'grade',
                          'effort',
                          'fname',
                          'lname',
                          'grade']

  def token_fname(self):
    return self.subject['fname']
    
  def token_lname(self):
    return self.subject['lname']
  
  def token_course(self):
    return self.subject['course']
    
  def token_grade(self):
    return self.subject['overall']
    
  def token_effort(self):
    return self.subject['effort']
    
  def token_strength(self):
    return self.subject['strength']
    
  def token_weakness(self):
    return self.subject['weakness']
    
  def token_prestopic(self):
  
    presOffsets = {'motor': 14, 'dispbutt': 18, 'touch': 22, 'speakerstatus': 26, 'gyro': 30, 'color': 34, 'wires': 38}
    
    if self.subject['prestopic'] in presOffsets:
      presOffset = presOffsets[self.subject['prestopic']]
      return choice(self.CL[presOffset - int(self.subject['presentation'])])
      
    elif self.subject['prestopic'] == "":
      return "" # Optional argument intentionally left blank
      
    else:
      return "!!!!!Unsupported prestopic; correct or manually write!!!!!"
    
  def token_nextbot(self):
        
    botOffsets = {'gyro': 39, 'puppy': 40, 'arm': 41, 'color': 42, 'custom': 43}
    
    if self.subject['nextbot'] in botOffsets:
      botOffset = botOffsets[self.subject['nextbot']]
      return choice(self.CL[botOffset])
      
    elif self.subject['nextbot'] == "":
      return "" # Optional argument intentionally left blank
      
    else:
      return "!!!!!Unsupported nextbot; correct or manually write!!!!!"
    

  def is_compatible(cls, subject):
    #TODO Implement This
    pass

  def generate_text(self):

    # Open with basic information
    self.text = "/fname /lname: /grade /effort\n"

    # Opening comment based on overall grade
    if self.subject['overall'] == 'EP':
      self.text += choice(self.CL[0])
    elif self.subject['overall'] == 'HP':
      self.text += choice(self.CL[1])
    elif self.subject['overall'] == 'P':
      self.text += choice(self.CL[2])
    elif self.subject['overall'] == 'LP':
      self.text += choice(self.CL[3])
    else:
      self.text += choice(self.CL[3])
      self.text += "!!!STUDENT DID NOT PASS. MANUALLY EDIT COMMENT!!!"
      
    # Second comment if student struggled in a particular area
    if self.subject['weakness'] != '':
      self.text += choice(self.CL[4])

    # Third comment if student excelled in a particular area
    if self.subject['strength'] != '':
      self.text += choice(self.CL[5])

    # Participation
    self.text += choice(self.CL[9 - int(self.subject['participation'])])
    
    # Presentation. Comments are specific to topic and student's success.
    if 'prestopic' in self.subject:
      self.text += "/prestopic"
    
    #TODO Obstacle course
    # In the student spreadsheet I could enter a space separated list of what
    # each students got points for in the obstacle course. Then jsut mention them
    # in the narrative.
    # for item in self.subject['obstaclecourse'].split():
    
    # Other Robot. Comments are specific to robot
    if 'nextbot' in self.subject:
      self.text += "/nextbot"
    
    # Conclusion
    self.text += choice(self.CL[9])
