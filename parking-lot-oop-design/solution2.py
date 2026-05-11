from datetime import datetime

class Ticket:
    def __init__(self):#, spot_number):
        self.timestamp = datetime.now()
        #self.spot_number = None


class Vehicle:
    def __init__(self, vehicle_name):
        size_map = {'truck':'large',
                    'car':'regular',
                    'motorcycle':'compact'}
        # assumes only these vehicle types
        self.size = size_map.get(vehicle_name) 
        self.spot_number = None


class ParkingLot:
    def __init__(self):
        self.lot = {'large':[1,2],
                    'regular':[3,4,5,6],
                    'compact':[7,8]}
        
    def allocate_spot(self, vehicle):
        if vehicle.size in self.lot:
            #vehicle.spot_number = self.lot[vehicle.size][:-1]
            spot_number = self.lot[vehicle.size][-1]
            vehicle.spot_number = spot_number
            # ticket = Ticket()
            # ticket.spot_number = spot_number
            self.lot[vehicle.size].pop()      
            #return ticket
        else:
            return "Vehicle type not supported, you can't park here."

    def calculate_payment(self, ticket, vehicle):
        self.lot[vehicle.size].append(vehicle.spot_number)
        current = datetime.now()
        #price = ((current - ticket.timestamp)//60) * 5
        elapsed = current - ticket.timestamp
        hours = elapsed.seconds / 3600
        price = hours * 5
        return price
    
    def report_capacity(self):
        # for i in self.lot:
        #     print(f'There are {len(self.lot[i[1]])} {self.lot[i[0]]} spots left')
        for i in self.lot:
            print(f'There are {len(self.lot[i])} {i} spots left')


    