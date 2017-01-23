import numpy as np
import pylab
import copy
from random import randint
from mpmath.tests.test_levin import xrange
from random import shuffle


def genlist():
    sortlist = [np.random.randint(10, 40)]
    for i in range(20):
        sortlist.append(np.random.randint(10, 40))
    return sortlist


def plot(id, alist, count):
    col = '#42d7f4'
    if id == 'IS':
        t = 0.05
        col = '#42f44b'
        text = 'Insertion Sort: Iteration '
    elif id == 'SS':
        t = 0.05
        col = '#f4fc16'
        text = 'Selection Sort: Iteration '
    elif id == 'BB':
        t = 0.01
        col = '#ef2913'
        text = 'Bubble Sort: Iteration '
    elif id == 'MS':
        t = 0.5
        col = '#e514db'
        text = 'Merge Sort: Iteration '
    else:
        t = 0.05
        col = '#0de4e8'
        text = 'Quick Sort: Iteration '

    width = 0.75
    pylab.clf()
    pylab.bar(range(0, len(alist)), alist, width, color=col)
    pylab.axis((0, 20, 0, 40))
    pylab.title(text + str(count))
    pylab.xlabel('List Index')
    pylab.ylabel('Size')
    pylab.suptitle("SORTING VISUALIZATION - Data Set - 2")
    pylab.pause(t)


#Bubble Sort
# FIX count
def bubble_sort(nlist):
    alist = np.copy(nlist)
    count = 0
    plot('BB', alist, count)
    pylab.pause(5)
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
                count += 1
                plot('BB', alist, count)
    print("BUBBLE SORT, for 20 elements, took " + str(count) + " Iterations")


# Selection Sort
def selection_sort(nlist):
    alist = np.copy(nlist)
    count = 0
    plot('SS', alist, count)
    pylab.pause(5)
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax=0
        for location in range(1, fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
        count += 1
        plot('SS', alist, count)
    print("SELECTION SORT, for 20 elements, took " + str(count) + " Iterations")

# Insertion Sort
def insertion_sort(nlist):
    # Generating an iterable on the length of the input array
    count = 0
    alist = np.copy(nlist)
    plot('IS', alist, count)
    pylab.pause(5)
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        print(currentvalue, '&&', end='')
        while position > 0 and alist[position-1] > currentvalue:
            print(alist[position])
            alist[position] = alist[position-1]
            plot('IS', alist, count)
            position -= 1
            count += 1
            print(alist)
        if position != index:
            alist[position] = currentvalue
            plot('IS', alist, count)
            print(alist)
    #alist[position] = currentvalue
    print("INSERTION SORT, for 20 elements, took " + str(count) + " Iterations")

#Merge sort
def merge_sort(nlist):
    global mcount
    global plist
    global sumcount

    plist = copy.copy(nlist)
    print('plist here is: ', plist)
    mcount = 0
    sumcount = 0
    alist = nlist
    plot('MS', alist, sumcount)
    pylab.pause(5)
    p = len(alist)
    sortedlist = merge_sort_perform(alist)
    if len(sortedlist) == p:
        # Overwrite the dummy statement Here for analysis
        print("MERGE SORT, for 20 elements, took " + str(sumcount) + " Iterations")
        return sortedlist


def minIndex(alist):
    st = plist.index(alist[0])
    for item in alist:
        if plist.index(item) < st:
            st = plist.index(item)
    return st

def maxIndex(alist):
    end = plist.index(alist[len(alist) - 1])
    for item in alist:
        if plist.index(item) > end:
            end = plist.index(item)
    return end


# For slicing the list
def processlist(alist, mcount):
    # required for editing a global variable
    global plist
    s = minIndex(alist)
    e = maxIndex(alist)
    if s == 0 and e != 0:
        print('s and e are: ', s, '&', e)
        p1 = alist[:]
        print('p1 here', p1)
        p2 = plist[e+1 : len(plist)]
        print('p2 here', p2)
        plist = p1 + p2
    elif s != 0 and e != 0:
        p1 = plist[:s]
        p2 = alist[:]
        p3 = plist[e+1:len(plist)]
        plist = p1 + p2 + p3
    else:
        p1 = plist[:s-1]
        p2 = alist[:]
        plist = p1 + p2
    plot('MS', plist, mcount)


def merge_sort_perform(alist):
    global mcount
    # Splitting the list

    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort_perform(lefthalf)
        merge_sort_perform(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1

            else:
                # collect essential info an d send to a recurrent function
                alist[k] = righthalf[j]
                j += 1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            print("Left ", lefthalf[i])
            i += 1
            k=k+1

        while j < len(righthalf):
            print("Right ", righthalf[j])
            alist[k] = righthalf[j]
            j=j+1
            k=k+1
        mcount += 1
        print("merged ", alist)
        print(plist)
        processlist(alist, mcount)

    return alist


# Quick Sort
def quick_sort(alist):
    global count

    count = 0
    plot('QS', alist, count)
    pylab.pause(7)
    quicksorthelper(alist, 0, len(alist)-1)

def quicksorthelper(alist, start, end):
    if start < end:
        pivot = randint(start, end)
        temp = alist[end]
        alist[end] = alist[pivot]
        alist[pivot] = temp

        p = partition(alist, start, end)
        quicksorthelper(alist, start, p - 1)
        quicksorthelper(alist, p + 1, end)


def partition(alist, start, end):
    global count
    pivot = randint(start, end)
    temp = alist[end]
    alist[end] = alist[pivot]
    alist[pivot] = temp
    newPivotIndex = start - 1
    for index in xrange(start, end):
        if alist[index] < alist[end]:  # check if current val is less than pivot value
            newPivotIndex = newPivotIndex + 1
            temp = alist[newPivotIndex]
            alist[newPivotIndex] = alist[index]
            alist[index] = temp
            count += 1
            plot('QS', alist, count)
    temp = alist[newPivotIndex + 1]
    alist[newPivotIndex + 1] = alist[end]
    alist[end] = temp
    count += 1
    plot('QS', alist, count)
    return newPivotIndex + 1



l1 = [19,31,18,20,17,23,16,30,22,39,24,15,26,14,25,13,37,12,27,11]

l2 = [35, 35, 31, 18, 28, 39, 20, 33, 14, 33, 19, 21, 39, 21, 38, 34, 37, 13, 25, 21, 11]

shuffle(l2)

bubble_sort(genlist())
#selection_sort(genlist())
#insertion_sort(l2)
#merge_sort(l1)
#quick_sort(genlist())
pylab.pause(3)
