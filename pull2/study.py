# al_resource  = [[2,0,1,1],[0,1,2,1],[4,0,0,3],[0,2,1,0],[1,0,3,0]]
# max_resource = [[3,2,1,4],[0,2,5,2],[5,1,0,5],[1,5,3,0],[3,0,3,3]]
# maximum resources: 8 5 9 7
# need = [ 0 for i in range(n)]]

# for i in range(len(al_resource)):
#     for j in range(len(al_resource)):
#         need = max_resource[i][j] - al_resource[i][j]
# print(need)



# direct mapping 구현 
# def virtural_address(p,d):
#     page_map_table_size = 40
#     memory_size = 1024
#     page_size = 4
#     page_frame_size = memory_size/page_size
#     import random
#     pmt = {}
#     for idx in range(len(page_map_table_size)):
#         pmt[idx] =[1,random.randint(0,page_frame_size)]

#     main_memory = []
#     for idx in range(memory_size):
#         main_memory.append(random.randInt(0,10000))

#     return main_memory[pmt["p"]*page_size+ d]

