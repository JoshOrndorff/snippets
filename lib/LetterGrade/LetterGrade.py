from snippets import Snippet

class LetterGrade(Snippet):

  def __init__(self, *args, **kwargs):
      
    super().__init__(*args, **kwargs)
    
    self.supportedData = ['grade']
                          
    self.tokens = []
    
    
  #TODO this should be a class method or static method or something because it
  # will be called before construction presumably.
  def is_compatible(cls, subject):
    ''' Returns boolean whether the subject is compatible with this snippet. '''
    
    try:
      self.subject['grade']
    except KeyErrror:
      return False
    else:
      return True
      
    #TODO support an optional way to override the default cutoffs via a subject datum.


  def generate_text(self):
    
    grade = float(self.subject['grade'])
    
    if grade > 100 or grade < 0:
      raise ValueError("Grade must be between 0 and 100")
    
    cutoffs = [ 97,   93,   90,   87,  83,   80,   77,  73,   70,   67,  63,   60,   0]
    letters = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']
    
    for i in range(len(cutoffs)):
      if grade > cutoffs[i]:
        self.text = letters[i]
        break


