"""
Polymorphism in Python

Polymorphism means the same method name can behave differently for different classes.
"""

class PDFReport:
    def generate(self):
        print("Generating PDF report")


class ExcelReport:
    def generate(self):
        print("Generating Excel report")


reports = [PDFReport(), ExcelReport()]

for report in reports:
    report.generate()
