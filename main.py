import pandas

# dtype loads all values as strings
df = pandas.read_csv("hotels.csv", dtype={"id":str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """books hotel by changing availability status to no"""
        availability = df.loc[df["id"] == self.hotel_id, "available"] = "no"
        # write changes to csv, index =False keeps python from adding another index
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """ checks if hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here is your booking ID:
        Name :{self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content

print(df)
hotel_id = input("Enter the id of the hotel:")
hotel = Hotel(hotel_id)

if hotel.available():
    hotel.book()
    name = input("Please enter your name:")
    reservation_ticket = ReservationTicket(customer_name=name, hotel_object =hotel)
    print(reservation_ticket.generate())

else:
    print("Hotel not available")

