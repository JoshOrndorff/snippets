from csv import reader
import xml.etree.ElementTree as ET #TODO should I use lxml? What's the difference?

class ElementWrapper(object):

  '''
    Wrapping Element class to allow accessing data by string key like in dict."
  '''

  def __init__(self, element):
    self.element = element
    
    # Composition finished. Bind all future set calls to instance element.
    self.__setattr__ = self.setattr
  
  def setattr(self, name, value):
    self.ET.Element.__setattr__(self.element, name, value)
  
  def __getattr__(self, name):
    return ET.Element.__getattribute__(self.element, name)
  
  def __getitem__(self, index):
    if type(index) == str:
      element = self.find(index)
      if element is None:
        raise ValueError("data, '{}', not in element".format(index))
      return element.text
    else:
      return ET.Element.__getitem__(self.element, index)
      
  def __contains__(self, datum):
    try:
      self[datum]
    except ValueError:
      return False
    else:
      return True


def get_students_csv(filename):

  '''
    Returns student data from a csv file specified in filename. This method is
    useful for medium sized data that requires a flat data structure. For the
    more rubust data structure that supports nesting, use get_students_xml().
  '''

  students = []

  with open(filename, 'rU') as f:
    categories = next(reader(f), None) # Get the header row
    for studentData in reader(f):
      student = ET.Element('student')
      blankSoFar = True
      for i in range(len(studentData)):
        if studentData[i] != '':
          blankSoFar = False
        currentElement = ET.SubElement(student, categories[i])
        currentElement.text = studentData[i]
      if not blankSoFar:
        students.append(ElementWrapper(student))
      
  return students
      
def get_students_xml(filename):

  '''
    Returns student data specified in from xml file specified in filename. This
    is the recommended way of storing student data because it is most robust
    (and it is the data format used internally. It supports metadata, a nested
    data structure.
  '''

  def attach_common_elements_to_children(currentElement):
      
    commonElements = []
    
    # First, loop to find the common info
    for child in currentElement:
      if len(child) == 0:
        commonElements.append(child)
    
    # Second, loop to add common elements to each sibling
    for child in currentElement:
      if len(child) > 0:
        for commonElement in commonElements:
          child.append(commonElement)
        if child.tag == 'student':
          students.append(ElementWrapper(child))
        else: # If it is a more deeply nested container, make the recursive call
          attach_common_elements_to_children(child)

  root = ET.parse(filename).getroot()      
  students = []
  # Make the initial call to the recursive function
  attach_common_elements_to_children(root)
    
  return students

def get_students_interactive(categories):

  '''
    Returns student data after accepting it as interactive from the user at the
    terminal. This method is mostly useful for small data sets and quickly
    generating a report. As such it only supports a flat data structure. For the
    more rubust data structure that supports nesting, use get_students_xml().
  '''

  students = []
  anotherStudent = True
  
  while anotherStudent:
    student = ET.Element('student')
    
    for category in categories:
      currentElement = ET.SubElement(student, category)
      currentElement.text = input(category + ': ')
      
    prompt = "Press enter to enter another student, or type 'done' to end. "
    anotherStudent = not (input(prompt) == 'done')
    students.append(ElementWrapper(student))    
    
  return students




