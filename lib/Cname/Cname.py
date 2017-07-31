from snippets import Snippet

class Cname(Snippet):
  '''
  Renders a person's 'common name' or cname. If a common name is specified, it
  is used, and if not the first name is used.
  '''

  def __init__(self, subject, ancestorTokens = [], children = {}):
    
    # Call parent class constructor
    super().__init__(subject, ancestorTokens, children)
    
    # Data names, in xpath format, that are recognized by this snippet
    self.supportedData = ['fname', 'cname']
    
    # Tokens that this snippet will replace directly
    self.tokens = []
    
    
  #TODO this should be a class method or static method or something because it
  # will be called before construction presumably.
  def is_compatible(cls, subject):
    ''' Returns boolean whether the subject is compatible with this snippet. '''
    
    #TODO implement this
    return True
    
    

  def generate_text(self):
    
    if self.subject['cname'] is None:
      self.text = self.subject['fname']
    else:
      self.text = self.subject['cname']


