def solution(sender):
    answer = []

    while len(sender) > 0:
        person = sender.pop()
        # print(person)

        if len(answer) == 0:
            answer.append(person + " 1")
            # print(1)
        else:
            added = False
            for val in answer:
                listval = val.split()
                # print(listval)
                print(person)
                if listval[0] == person:
                    val = listval[0] + " " + str(int(listval[1]) + 1)
                    print(3)
                    added = True
                    break
            
            if (not added):
                answer.append(person + " 1")
            # print(2)

    return answer

print(solution(["D", "A", "C", "D", "B"]))