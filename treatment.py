import pandas as pd

class Treatment:
    def __init__(self, name, numberoftreats, avgcovered, avgtotalpay, avgmedicalpay):
        self.name = name
        self.numberoftreats = numberoftreats
        self.avgcovered = avgcovered
        self.avgtotalpay = avgtotalpay
        self.avgmedicalpay = avgmedicalpay
        
    def __str__(self):
        return f"Address: {self.name} {self.numberoftreats}, {self.avgcovered}, {self.avgtotalpay}, {self.avgmedicalpay}"

df2 = pd.read_csv('inpatientCharges.csv', sep=';', low_memory=False)

treatments = []

