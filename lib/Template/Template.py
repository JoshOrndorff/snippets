from snippets import Snippet

class Tempalte(Snippet):

  def __init__(self, subject, ancestorTokens = [], children = {}):
    
    # Here you should setup the ownTokens list and the children.
    
    # Call parent class constructor
    super().__init__(, subject, ancestorTokens, children)
    
    # Data names, in xpath format, that are recognized by this snippet
    self.supportedData = []
    
    # Tokens that this snippet will replace directly
    self.tokens = []
    
    
  #TODO this should be a class method or static method or something because it
  # will be called before construction presumably.
  def is_compatible(cls, subject):
    ''' Returns boolean whether the subject is compatible with this snippet. '''
    
    return True
    
    

  def generate_text(self):
    
    selt.text = "You've used the tempalte snippet. You should copy and modify it."


