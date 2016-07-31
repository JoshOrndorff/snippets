from csv import reader

def get_comments(commentFile):
  '''
    Gets comments from a csv file and strips them to usable form.
  '''
  
  CL = []
  with open(commentFile, 'rU') as f:
    for row in reader(f):
      del row[0] # Strip the row headers
      while '' in row: # Remove blank entries from rows
        row.remove('')
      CL.append(row)
  return CL

def replace_gender(text, gender):
  '''
    Replaces tokens in text with gendered pronouns and returns gendered text.
    Gender must be in ['m', 'M', 'f', 'F'].
  '''
  sanitizedGender = gender.lower().strip()
  if sanitizedGender == 'm':
    text = text.replace('/heshe', 'he')
    text = text.replace('/HeShe', 'He')
    text = text.replace('/himher','him')
    text = text.replace('/hishers','his')
    text = text.replace('/hisher','his')
    text = text.replace('/HisHer', 'His')
  elif sanitizedGender == 'f':
    text = text.replace('/heshe', 'she')
    text = text.replace('/HeShe', 'She')
    text = text.replace('/himher','her')
    text = text.replace('/hishers','hers')
    text = text.replace('/hisher','her')
    text = text.replace('/HisHer', 'Her')
  else:
    raise ValueError('Invalid gender: ' + gender)
    
  return text
