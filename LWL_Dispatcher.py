
import numpy as np
from task_controller import JOB_Control
from FCFS import FirstComeFirstService as FCFS

class Least_Work_Left:
 
    def __init__(self, N, df):
        
        self.N = N
        self.clock = int(df["Arrival_Time"].iloc[0])
        self.job_controller = JOB_Control(df).register
        self.servers = [FCFS(id) for id in range(0,N)]
        
    def dispatch(self, task):
        
        task = JOB_Control.preprocess(task)
        work_load = np.array([server.work_load for server in self.servers])
        pointed = np.argmin(work_load)

        while self.servers[pointed].add_to_queue(task) == False:
            work_load[pointed]= work_load.max()
            pointed = np.argmin(work_load)

        #self.servers[pointed].add_to_queue(task)
        
    def time_manager(self, task):
        
        now = int(task['Arrival_Time'])
        active_queues = [k for k in range(self.N) if len(self.servers[k].queue)>0]
        
        if self.clock != now and len(active_queues):
            self.clock = now
            
            for i in active_queues:
                this_queue = self.servers[i].queue     #Pointed queue
                pre = this_queue[0]['arrival_time']    #Active task activation time
                delta = now - pre                     #Time elapsed between the arrival of the active task and the clock updating
                loop = True
                while loop:
                    job = this_queue[0]['id'].split('_')[0]
                    if this_queue[0]['service_time'] > delta:
                        this_queue[0]['service_time'] -= delta
                        break
                    else:
                        d = this_queue[0]['service_time'] - delta
                        self.job_controller[job]['Active_tasks'] -= 1
                        comp = self.clock + d

                        if (comp > self.job_controller[job]['Completion']):
                            self.job_controller[job]['Completion'] = comp
                        self.servers[i].delete_from_queue()
                        if len(self.servers[i].queue) == 0:
                            break
                        else:
                            if self.servers[i].queue[0]['arrival_time'] <= comp:
                                delta = self.clock - comp
                                self.servers[i].queue[0]['service_time'] -= comp - self.servers[i].queue[0]['arrival_time']    
                            else: 
                                delta = self.clock - self.servers[i].queue[0]['arrival_time']                      
                        this_queue = self.servers[i].queue
