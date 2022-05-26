'''
Given an array of non-negative integers representing the elevations,
     many units of snow could be captured between the hills. 
     from the vertical cross section of a range of hills, determine how much snow can be collected.

     See the example array and elevation map below.
  
  int [] arr=new int[]{0,1,3,0,1,2,0,4,2,0,3,0};
                                 ___
             ___                |   |        ___
            |   |        ___    |   |___    |   |
         ___|   |    ___|   |   |   |   |   |   |
     ___|___|___|___|___|___|___|___|___|___|___|___
     {0,  1,  3,  0,  1,  2,  0,  4,  2,  0,  3,  0}
                                 ___
             ___                |   |        ___
            |   | *   *  _*_  * |   |_*_  * |   |
         ___|   | *  _*_|   | * |   |   | * |   |
     ___|___|___|_*_|___|___|_*_|___|___|_*_|___|___
     {0,  1,  3,  0,  1,  2,  0,  4,  2,  0,  3,  0}

     Solution: In this example 13 units of snow (*) could be captured.
     '''



import sys


def getResults(input):
    op = 0
    left_track, right_track = [], []
    l_max, r_max = sys.maxsize * -1, sys.maxsize * -1
    for i in range(len(input)):
        if input[len(input) - i - 1] > r_max:
            r_max = input[len(input) - i - 1]
        if input[i] > l_max:
            l_max = input[i]
        left_track.append(l_max)
        right_track.append(r_max)
    right_track.reverse()
    
    for i in range(len(right_track)-1):
        op = op + min(right_track[i], left_track[i]) - input[i]


 
    return op



input = [0,1,3,0,1,2,0,4,2,0,3,0]
print(getResults(input))