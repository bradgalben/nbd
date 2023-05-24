
import numpy as np
import pandas as pd

class JOB_Control:
    
    def __init__(self, df):
        
        assert list(df.columns) == ['Job_ID', 'Task_ID', 
                                    'Arrival_Time', 'CPU', 'Memory'], 'Incorrect input format'
        
        arrival_times = np.array(pd.unique(df['Arrival_Time']))
        id_s = np.array(pd.unique(df['Job_ID']))
        count = np.array(df.groupby('Job_ID')["Task_ID"].count())
        tot_cpu = np.array(df.groupby('Job_ID')["CPU"].sum())*10000
        
        self.register = {str(a_id):{'Active_tasks':k, 'Arrival': t, 'Completion': 0} 
                                       for (a_id, k, t, num) in zip(id_s, count, arrival_times,tot_cpu)}
    
    def preprocess(task, mu=0.1):
    
        assert list(task.keys()) == ['Job_ID', 'Task_ID', 
                                    'Arrival_Time', 'CPU', 'Memory'], 'Incorrect input format'
        
        new_job_id = str(int(task["Job_ID"]))+ "_" + str(int(task["Task_ID"]))
        arrival_time_task = int(task["Arrival_Time"])
        running_time_task = (task["CPU"]/mu)*1000

        a_dict = {"id": new_job_id, "Memory": task['Memory'], 
                "arrival_time": arrival_time_task, "service_time" : running_time_task}
        
        return a_dict