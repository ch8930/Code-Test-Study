from collections import deque


def solution(bridge_length, weight, truck_weights):
    wait_trucks = deque(truck_weights)
    cross_trucks = deque()

    cur_time = 1

    f_truck = wait_trucks.popleft()
    cross_trucks.append((f_truck, cur_time + bridge_length))
    now_weight = weight - f_truck
    cur_time += 1

    while wait_trucks:

        # 해당 시점에서 다리를 지난 트럭이 있는지 체크
        while cross_trucks and cross_trucks[0][1] <= cur_time:
            w, _ = cross_trucks.popleft()
            now_weight += w

        if wait_trucks[0] <= now_weight:
            truck = wait_trucks.popleft()
            cross_trucks.append((truck, cur_time + bridge_length))
            now_weight -= truck
            # 트럭을 올리고 한 칸 전진한 상태
            cur_time += 1
        else:
            if cross_trucks:
                # 해당 트럭이 내려간 시점으로 jump
                cur_time = cross_trucks[0][1]

    #         # 트럭이 다리를 지나갈 수 없는 상태
    #         while now_length < 1 or now_weight < now_truck:
    #             out_truck, s, e= cross_trucks.popleft()
    #             cur_time = e
    #             now_length += 1
    #             now_weight += out_truck

    #         s = cur_time
    #         e = cur_time + bridge_length
    #         cross_trucks.append((now_truck, s, e))
    #         now_length -= 1
    #         now_weight -= now_truck
    #         cur_time += 1

    return cross_trucks[-1][1]