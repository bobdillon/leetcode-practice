from datetime import datetime, timedelta

class Vehicle:
    def __init__(self, type):
        self.type = type
        self.spot_size_map = {
        'motorcycle':'small',
        'car':'medium',
        'truck':'large'}
        self.size = self.spot_size_map.get(self.type)

class Ticket:
    def __init__(self, spot_number, size):
        self.entry_time = datetime.now()
        self.spot_number =  spot_number
        self.size=size

class Parking:
    def __init__(self):#, vehicle):
        self.lot = {'large' :[1,2],
                    'medium':[3,4,5,6],
                    'small' :[7,8,9] }
        #self.vehicle = vehicle

    # find and assign an available spot. 
    # Return a ticket or raise an error if full.
    def allocate_spot(self, vehicle):
        size = vehicle.size
        if not self.lot[size]:
            return "error: lot is full for this vehicle type"
        spot = self.lot[size].pop()
        return Ticket(spot, size)

        # if self.vehicle in self.lot:
        #     # if number spots not at max
        #     if self.lot[self.vehicle][1]< self.lot[self.vehicle][0]:
        #         # then increment for new vehicle
        #         self.lot[self.vehicle][1] +=1
        #         #assign spot number
        #         #assign initial timestamp
        #     else:
        #         return "error: lot is full for this vehicle type"
        # else:
        #     return "error: lot does not support thie vehicle type"                                           
        # return None
    
    def exit(self, ticket):
        #make spot available again 
        self.lot[ticket.size].append(ticket.spot_number)
        #payment = (datetime.timedelta(datetime.now()) - datetime.timedelta(ticket.entry_time))//60*5
        duration_minutes = (datetime.now() - ticket.entry_time).seconds // 60
        payment = duration_minutes * 5
        return payment


    # def payment(self, timestamp):
    #     current = datetime.now()
    #     payment = (datetime.timedelta(current) - datetime.timedelta(timestamp))//60*5
    #     return payment


 #truck = Vehicle('truck')       