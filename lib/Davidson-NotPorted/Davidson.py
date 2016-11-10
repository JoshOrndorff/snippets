from os.path import dirname
from os import sep
from random import choice
from snippets.shared import *

commentFile = dirname(__file__) + sep + "comments.csv"
CL = get_comments(commentFile)

def generate_text(student):

  # Opening Comment
  comment = choice(CL[0])

  # Second comment if student struggled in a particular area
  if student['explanation'] != '':
    comment += choice(CL[1])
    comment += choice(CL[2])

  # Participation
  comment += choice(CL[6 - int(student['participation'])])
  
  # and but
  if student['participation'] == student['prep']:
    comment += ' and '
  else:
    comment += ' but '
  
  # Preparation
  comment += choice(CL[9 - int(student['prep'])])

  # See me frequently
  comment += choice(CL[12 - int(student['seemefreq'])])
  
  # Conclusion
  comment += CL[12][0]
  
  # Replace tokens
  comment = comment.replace('/fname',  student['fname'])
  comment = comment.replace('/grade',  student['overallgrade'])
  comment = comment.replace('/course', student['course'])
  comment = comment.replace('/exp',    student['explanation'])
  comment = replace_gender(comment,    student['gender'])

  return comment
