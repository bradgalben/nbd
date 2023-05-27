

class  First_Come_First_Service:
    
    def __init__(self, id : int):

        self.server_id = id 
        self.status = 0
        self.memory = 1
        self.work_load = 0
        self.queue = []
        self.details = []
    
    def add_to_queue(self, task : dict):
        
        task['waiting_time'] = 0

        #if self.memory > task["Memory"]: 
            
        self.queue.append(task)   
        self.status = 1
        self.memory -= task["Memory"]
        self.work_load = sum([task['service_time'] if self.status == 1 else 0 for task in self.queue])
        self.details.append(task['service_time'])
                
        #else: return False
            #raise Exception('Memory error!')
            
    def delete_from_queue(self):
  
        self.memory += self.queue[0]['Memory']
        self.queue.pop(0)
        if len(self.queue) == 0: self.status = 0
        self.work_load = sum([task['service_time'] if self.status == 1 else 0 for task in self.queue])
