# class Logger:
#     def __init__(self):
#         #key - log message, value - list of timestamps
#         self.log = {}

#     def shouldPrintMessage(self, message:list):
#         if not message[0]:
#             return None
#         if message[1] in self.log:
#             self.log[message[1]].append(message[0])
#             timestamps = self.log[message[1]][-11:]
#             if max(timestamps)-min(timestamps)>10:
#                 return True
#             else:
#                 return False
#         else:
#             self.log[message[1]] = [message[0]]
#             return True
        
class Logger:
    def __init__(self):
        self.log = {}

    def shouldPrintMessage(self, timestamp, message):
        if message in self.log:
            if timestamp - self.log[message]>=10:
                self.log[message]=timestamp      
                return True
            else:
                return False
        else: 
            self.log[message]=timestamp      
            return True
            
        
    
