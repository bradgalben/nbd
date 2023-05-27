
from numpy import array, argmin

from task_controller import JOB_Control
from Scheduling import First_Come_First_Service

class Dispatcher:
 
    def __init__(self, N : int, starting : float, df):
        
        self.N = N
        self.clock = starting
        self.job_controller = JOB_Control()
        self.servers = [First_Come_First_Service(id) for id in range(N)]

        print("\n Dispatcher →", self.Least_Work_Left.__name__)

    def clock_update(self, new_time_from_task):
        self.clock = new_time_from_task
        
    def Least_Work_Left(self, task):
        
        task = self.job_controller.preprocess(task, mu=0.1)
        work_load = array([server.work_load for server in self.servers])
        pointed = argmin(work_load)
        self.servers[pointed].add_to_queue(task)
        

    def queue_manager(self, task):

        active_queues = [server for server in self.servers if len(server.queue)>0]
        if len(active_queues) != 0:
            for server in active_queues:
                queue = server.queue
                now = task['Arrival_Time']
                delta = now-self.clock
                while delta > 0 and len(queue) > 0:
                    active = queue[0]
                    if active['service_time'] - delta <= 0:
                        self.job_controller.register.append({  'Job_ID:':active['id'].split('_')[0],
                                                               'Task_ID:':active['id'].split('_')[1],
                                                               'Arrived_at': active['Arrival_Time'],
                                                               'Completed_at:': now+active['service_time']-delta   })
                        server.delete_from_queue()
                        delta -= active['service_time']
                        queue = server.queue
                    else:
                        active['service_time'] -= delta
                        break
            
