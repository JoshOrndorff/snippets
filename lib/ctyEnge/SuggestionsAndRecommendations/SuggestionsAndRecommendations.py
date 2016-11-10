from random import choice
from snippets import Snippet

class SuggestionsAndRecommendations(Snippet):

  def __init__(self, subject, ancestorTokens = [], children = {}):
    
    # Tokens are replaced in the order specified here.
    #TODO This list feels redundant since I've defined functions / children for all tokens.
    self.ownTokens = ['main', 'final', 'ta', 'cname', 'truly']
    
    #TODO there is nicer syntax for python3
    super(SuggestionsAndRecommendations, self).__init__(subject, ancestorTokens, children)
    
    self.supportedData = ['notebook[@check="1"]',
                          'notebook[@check="2"]',
                          'ta',
                          'cname',
                          'instructor']

  def token_ta(self):
    return self.subject['ta'].split()[0]
    
  def token_cname(self):
    if self.subject['cname'] is None:
      return self.subject['fname']
      
    return self.subject['cname']
  
  def token_truly(self):
    if self.subject['completion'] == "successfully completing":
      return "truly "
    else:
      return ""
      
  def token_main(self):
    options = ["/cname, I recommend that you continue to build on your engineering and problem-solving skills by studying the more advanced topics in our textbook and practicing with your breadboard that you received in the course.",
               "/cname, /ta and I /truly enjoyed working with you this summer. I recommend that you continue to develop your engineering and problem-solving skills by studying the more advanced topics in our textbook.",
               "I suggest that you continue to build on what you've learned by studying more advanced topics in our text book and online, and practicing with the breadboard that you received in class."]
  
    return choice(options)

  def token_final(self):
    options = []
      
    if self.subject['completion'] == "successfully completing":
      options.append("/ta and I truly enjoyed working with you this summer. I hope to hear of the many successes that are surely in your future, and wish you the best of luck in all your endeavors.")
      
    if self.subject['completion'] == "completing" or self.subject['completion'] == "successfully completing":
      options.append("/cname, /ta and I /truly enjoyed working with you this summer. I look forward to hearing about your engineering and academic successes, and wish you the best of luck in the future.")
      options.append("It has /truly been a pleasure to work with you this summer, /cname. Best of luck in your future academic work.")
    else:
      options.append("/ta and I look forward to hearing about your engineering and academic successes in the future. Good luck!")

    return choice(options)
      

  def is_compatible(cls, subject):
    #TODO Implement This
    pass

  def generate_text(self):

    # The main part of the paragraph
    self.text = "/main"

    # Specific comment if they had a messy notebook
    if int(self.subject['notebook[@check="1"]']) < 70 and int(self.subject['notebook[@check="2"]']) < 70:
      self.text += " I also encourage you to continue working on your organizational skills and practice writing your work formally."

    # Final bit
    self.text += '\n\n'
    self.text += "/final"
      

