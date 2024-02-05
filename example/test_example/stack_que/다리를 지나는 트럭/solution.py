def solution(bridge_length, weight, truck_weights):
    answer = 0
    list_status = [0]*len(bridge_length)
    list_status_map = []
    list_pass = []

    while len(list_pass) != len(truck_weights):
        if sum(list_status) + weight[0] <= weight:
            list_status.append(weight.pop(0))
            head = list_status.pop(0)
            if head != 0:
                list_pass.append(head)
        else:
            list_status.append(0)
            head = list_status.pop(0)          
            if head != 0:
                list_pass.append(head)

        list_status_map.append(list_status)
                     
    answer = len(list_status_map)
    return answer



bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

bridge_length = 100
weight = 100
truck_weights = [10]

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]

answer = solution(bridge_length, weight, truck_weights)
print(answer)