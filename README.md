# nbd


# Problem Outline

Consider a computational cluster consisting of a job dispatcher device and N servers, each equipped with its own processing and memory resources.

## Assumptions

The following assumptions are made for the problem:

- Each server has the same processing power µ, expressed in GNCU. Hence, the service time of a task is X = C/µ.
- Each server has a memory amount of 1 GNMU.
- Pre-emption is allowed as well as server sharing, if deemed useful.
- It is not allowed to kill a job or a task, i.e., all tasks must be worked out eventually.
- The dispatcher and servers have knowledge of the exact service time of a task upon its arrival.
- Delay and loss are negligible for message exchange among the dispatcher and the servers.
- Each running task is assigned the memory space it requires as long as it is running. Swapping a task from running to standby and back requires negligible time.
- At any given time, the sum of all assigned memory workspaces to running tasks on a given server shall not exceed the overall memory of that server.

Please refer to the original problem outline for further details.

## Metrics

Metrics used to evaluate the performance of the computational cluster:

- `Job Response Time (R):` Job response time is defined as the time elapsed from the arrival of the first task of a job until all tasks belonging to that job have been fully served. The mean job response time (R) is obtained by averaging the response times of all jobs.

- `Job Slowdown (S):` Job slowdown is calculated as the ratio of the response time of a job to the sum of the service times of all tasks belonging to that job. The mean job slowdown (S) is obtained by averaging the slowdown values of all jobs.

- `Utilization Coefficient (ρk):` The utilization coefficient of server k (ρk) represents the fraction of time that server k is busy serving tasks. The overall mean utilization coefficient (ρ) is calculated as the average of ρk values for all servers: ρ = (ρ1 + ρ2 + ... + ρN) / N.

- `Messaging Load (L):` Messaging load refers to the number of messages exchanged between the dispatcher and servers for a given task dispatching. The mean message load (L) is obtained by averaging the message load values of all tasks.



