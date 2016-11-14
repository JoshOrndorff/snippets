#! /usr/bin/env python3

# Helper function to parse student data
from snippets.core.input import get_students_csv

# Snippet from the library.
from snippets.lib import GeneralSchoolCourse

# Setup input and output
students = get_students_csv("students.csv")
outputFile = "output.txt"

# Make the interims and save the file
with open(outputFile, "w") as f:
  for student in students:
    f.write(GeneralSchoolCourse(student).render())
    f.write("\n\n")

