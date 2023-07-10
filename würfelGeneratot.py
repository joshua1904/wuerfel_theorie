import json
from statistics import median, mean
from _thread import start_new_thread
results = list()
end = False
import random
def main():
    arr = [0, 0, 0, 0]
    counter = 0
    info_counter = 0
    while True:
        arr[0] += random.randint(1, 6)
        arr[1] += random.randint(1, 6) 
        arr[2] += random.randint(1, 6) 
        arr[3] += random.randint(1, 6) 
        counter += 1
        if equal(arr)[0] == True:
            results.append({counter: equal(arr)[1]})
            break
        if info_counter == 1000000:
            print(arr)
            print(f"versuche: {counter}")
            info_counter = 0
        #elif counter > 1000000:
         #    results.append({1000000: 3500000})
          #   break
        info_counter += 1

def loop(howManyLoops: int):
    for i in range(howManyLoops):
        main()
        print(i)
    print(results)

def threading(howmanyLoops):
    loops = int(howmanyLoops / 2)
    start_new_thread(loop, (loops,))

    loop(loops)
    print(results)
    solution(getValueList(results), getKeyList(results))
    safe()

def equal(arr: list()) -> bool:
    counter = 0
    thisNumber = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                counter += 1
                thisNumber = arr[i]
        if counter >= 2:
            return (True, thisNumber)
        counter  = 0
    return (False, 0)



def safe():
    out_file = open("mimi.json", "w")
  
    json.dump(results, out_file, indent = 6)
    
    out_file.close()

def getKeyList(resultsList: list()):
    returnValue = list()
    for i in resultsList: 
        returnValue.append(list(i.keys())[0])
    return returnValue

def getValueList(resultsList: list()):
    returnValue = list()
    for i in resultsList: 
        returnValue.append(list(i.values())[0])
    return returnValue

def solution(valueList: list(), keyList: list()):
    valueMean = mean(valueList)
    keyMean = mean(keyList)
    keyMedian = median(keyList)
    valueMedian = median(valueList)
    print(f"counterMedian = {keyMedian} counterMean = {keyMean} valueMedian = {valueMedian}, valueMean = {valueMean}")


loop(1)


x = {
        "answer": "counterMedian = 636.5 counterMean = 274439.624 valueMedian = 2230.5, valueMean = 960537.76"
      }