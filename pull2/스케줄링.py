# from concurrent.futures import process


# def fcfs(processes, bursts, arrivals = None) :
#     # 실행시간 
#     burst_time = bursts
#     # 대기시간
#     wait_time = []
#     # 반환시간
#     turn_time = []
#     temp = 0
#     for i in range(len(processes)):
       
#         wait_time.append(temp - arrivals[i])
#         temp += bursts[i]
#         turn_time.append(temp - arrivals[i])




#     return burst_time, wait_time, turn_time
# # process id
# processes = [1, 2, 3, 4, 5, 6]
# # Burst time of all processes  
# burst_time = [5, 9, 6, 15, 6, 3]
# # Arrival time of all processes
# arrival_time = [0, 3, 6, 7, 8, 10]

# p = processes.copy()
# n = len(processes)

# b,w,t = fcfs(processes, burst_time, arrival_time)
# print("process ID              :", p)
# print("Burst_시간               :", b)
# print("Waiting_시간             :", w)
# print("Turn_Around_시간         :", t)
# print("평균 wating 시간          :", sum(w)/n)
# print("평균 turn around 시간     :", sum(t)/n)



num_page_frame = 4
allocated_pages = [2, 6, 1, 4]           
reference_string = [5, 1, 2, 1, 4, 5, 6, 4, 5]

def LRU_replace(num_page_frame, allocated_pages, reference_string):
    time = 5
    idx = 0

    for data in reference_string:
        print("현재시점", time)
        print("allocated_pages", allocated_pages)
        print("reference_string", reference_string[idx:])
        time = time +1
        idx = idx +1
        if data not in allocated_pages:
            if len(allocated_pages) < num_page_frame:
                allocated_pages.append(data)
            else:
                allocated_pages.pop(0)
                allocated_pages.append(data)
        else:
            allocated_pages.pop(allocated_pages.index(data))
            allocated_pages.append(data)

    return allocated_pages

result_pages = LRU_replace(num_page_frame, allocated_pages, reference_string)
print(result_pages)
