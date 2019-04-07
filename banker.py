import random
import sys
import time


def error():
    print("something went wrong")
    sys.exit(1)


def mainloop():
    thecounter = 0
    processesmax = {}
    processesalloc = {}
    resourses = []
    releasetime = {}

    try:
        if len(sys.argv) < 3 + int(sys.argv[2]):
            s = " ".join(sys.argv[1:])
            print(s)
            return error()

        processes_num = int(sys.argv[1])
        resources_num = int(sys.argv[2])
        # fill out the list of resources
        for i in range(1, resources_num + 1):
            resourses.append(int(sys.argv[i + 2]))
    except Exception as e:
        s = " ".join(sys.argv[1:])
        print(s)
        error()

    # fill out the allocation array
    for j in range(processes_num):
        arr = []
        for i in range(resources_num):
            arr.append(0)
        processesalloc.update({j + 1: arr})

    # fill out the max array
    for k in range(1, processes_num + 1):
        maxes = []
        for u in range(1, resources_num + 1):
            maxes.append(random.randint(0, int(sys.argv[2 + u])))
        processesmax.update({k: maxes})

    releasetime = dict.fromkeys(processesalloc.keys(), 0)
    print("the allocation table:")
    print(processesalloc)
    print("the max table:")
    print(processesmax)
    print("the resourses:")
    print(resourses)
    time.sleep(2)

    condition = False
    d = str(raw_input("Please select the number of requests (write 'd' for default mode (16 reqs) or 'i' for infinite mode):\n"))
    if d == 'd':
        default = 15
    elif d == 'i':
        default = 15
        condition = True
    else:
        try:
            default = int(d) - 1
        except Exception as e:
            error()

    # the loop
    while(thecounter <= default or condition):

        flag = True

        for index in range(1, processes_num + 1):
            if releasetime[index] == thecounter and thecounter != 0:
                releasetime[index] = 0
                for index2 in range(resources_num):
                    resourses[index2] += processesalloc[index][index2]
                    processesalloc[index][index2] = 0
                print("Process Number[{}] released its resourses".format(index))
                print("the allocation table:")
                print(processesalloc)
                print("the max table:")
                print(processesmax)
                print("the remaining resourses:")
                print(resourses)
                time.sleep(2)

        randomresourses = []
        randomprocess = random.choice(processesalloc.keys())

        for o in range(resources_num):
            randomresourses.append(random.randint(0, processesmax[randomprocess][o] - processesalloc[randomprocess][o]))

        # check for unsafe request
        for f in range(resources_num):
            if randomresourses[f] > resourses[f]:
                flag = False
                break

        if sum(randomresourses) == 0:
            continue

        print("the request[{}]: ".format(thecounter + 1) + str(randomresourses) + " for process no " + str(randomprocess))

        # allocation decision
        if flag:
            for count in range(len(randomresourses)):
                processesalloc[randomprocess][count] = processesalloc[randomprocess][count] + randomresourses[count]
                resourses[count] = resourses[count] - randomresourses[count]
            releasetime[randomprocess] = random.randint(thecounter, thecounter + 15)
            print("request accepted")
        else:
            print("request denied")
        thecounter += 1
        print("the allocation table:")
        print(processesalloc)
        print("the max table:")
        print(processesmax)
        print("the remaining resourses:")
        print(resourses)
        time.sleep(2)


mainloop()
