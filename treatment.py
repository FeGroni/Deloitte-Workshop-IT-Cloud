import pandas as pd

class Address:
    def __init__(self, state, city, street, housenumber, zipcode, referralregion):
        self.state = state
        self.city = city
        self.street = street
        self.housenumber = housenumber
        self.zipcode = zipcode
        self.referralregion = referralregion

    def __str__(self):
        return f"Address: {self.housenumber} {self.street}, {self.city}, {self.state}, {self.zipcode}, {self.referralregion}"

df = pd.read_csv('inpatientCharges.csv', sep=';', low_memory=False)

addresses = []
for index, row in df.iterrows():
    state = row['Provider State']
    city = row['Provider City']
    street = row['Provider Street Address']
    housenumber = row['Provider Id']
    zipcode = row['Provider Zip Code']
    referralregion = row['Hospital Referral Region Description']

    address = Address(state, city, street, housenumber, zipcode, referralregion)
    addresses.append(address)

for address in addresses:
    print(address)
