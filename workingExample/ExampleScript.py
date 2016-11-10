#! /usr/bin/env python3

# Helper function to parse student data
from snippets.input import get_students_csv

# Original snippet (with some slight changes to use other nice features).
from snippets import Davidson

# Setup input and output
students = get_students_csv("students.csv")
outputFile = "output.txt"

# Make the interims and save the file
with open(outputFile, "w") as f:
  for student in students:
    f.write(Davidson.generate_text(student))
    f.write("\n\n")

