class Address:

    def __init__(self, housenumber, street, city, postcode):
        self.housenumber = housenumber
        self.street = street
        self.city = city
        self.postcode = postcode

    def __str__(self):
        return f"\nHouse number: {self.housenumber} \nStreet: {self.street} \nCity:{self.city} \nPostcode:{self.postcode}"