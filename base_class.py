from .shared import replace_gender

#TODO At some point, I want to be able to pass only part of the subject tree
# to child snippets.

class Snippet(object):
  ''' The base snippet class that all snippets will extend.
  
  Responsible for listing required and optional subject data, validating a
  passed subject, generating a bit of text which can have zero or more tokens,
  filled in dynamically. '''
  
  # Data names, in xpath format, that are recognized by this snippet
  supportedData = []
  
  # Tokens that this snippet will replace
  ownTokens = []
  
  def __init__(self, subject, ancestorTokens = [], children = {}):
    ''' Sets up a new snippet instance. '''
    
    # Each snippet has a list of tokens that it will replace. This base class
    # simply adds the parent's supported tokens to that list. Any tokens that
    # will be replaced at this level should be appended to the tokens list in
    # the child class's constructor.
    self.ancestorTokens = ancestorTokens
    self.children = children
    
    # Each instance has a subject
    self.subject = subject
    
    # Each instance has a dict of tokens that are overridden by child snippets.
    for token, child in children.items():
    
      # If the token is actually supported, copy it to the instance
      if token in self.ownTokens:
        self.children[token] = child
      else:
        raise ValueError("Token, {}, not supported.".format(token))

  
  #TODO this should be a class method or static method or something because it
  # will be called before construction presumably.
  def is_compatible(cls, subject):
    ''' Returns boolean whether the subject is compatible with this snippet. '''
    
    raise NotImplementedError("Abstract method, 'is_compatible' not implemented in child class.")
    
  def generate_text(self):
    
    raise NotImplementedError("Abstract method, 'generate_text' not implemented in child class.")
    
  def render(self):
    ''' Primary method for actually constructing the final text.
    
    Replaces tokens with text from child snippets if they are provided, or
    the default snippet handler if not. Replacement happens in the order
    specified in snippet's the ownTokens list'''
    
    # Generate text
    self.generate_text()
    
    # Replace tokens
    for token in self.ownTokens:
      if '/' + token in self.text: # Only replace the token if it actually needs replacing.
        if token in self.children:
          # This is for nesting snippets. I don't think this line has ever actually been tested.
          self.text = self.text.replace('/' + token, self.children[token].render())
        else:
          self.text = self.text.replace('/' + token, getattr(self, 'token_' + token)())
      
      
    #TODO Figure out the best way to handle the gender pronouns. For now they
    # are handled here in the base class.   Idea: gender could be a seperate
    # snippet, and depending which token is being replaced, it will return a
    # different pronoun. Or it could be a bunch of different snippets
    self.text = replace_gender(self.text, self.subject['gender'])

    
    # Return fully rendered text
    return self.text
      
  def get_all_tokens(self):
    ''' Returns a list of all tokens safe to return to this snippet. A safe token
    is any token that is replaced directly by this snippet or guarenteed to be
    replaced by one of its ancestors.'''
    return self.ownTokens + self.ancestorTokens
      
      
