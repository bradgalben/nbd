
from numpy import array
#from pandas import DataFrame, unique

class JOB_Control:
    
    def __init__(self):
        
        self.register = [] # list of dict
    
    def preprocess(self, task : dict, mu=0.1):
    
        assert list(task.keys()) == ['Job_ID', 'Task_ID', 
                                    'Arrival_Time', 'CPU', 'Memory'], 'Incorrect input format'
        
        new_job_id = str(int(task["Job_ID"]))+ "_" + str(int(task["Task_ID"]))
        arrival_time_task = task["Arrival_Time"]
        running_time_task = (task["CPU"]/mu)

        a_dict = {"id": new_job_id, "Memory": task['Memory'], 
                "Arrival_Time": arrival_time_task, "service_time" : running_time_task}
        
        return a_dict
