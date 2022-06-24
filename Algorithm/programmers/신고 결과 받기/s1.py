from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    reported_id = defaultdict(list)
    check = defaultdict(int)

    for i in report:
        ID1, ID2 = i.split()
        reported_id[ID1] = ID2
        check[ID2] += 1

    for i in id_list:
        cnt = 0
        for j in reported_id[i]:
            if check[j] >= k:
                cnt += 1
        answer.append(cnt)

    return answer