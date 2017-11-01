def powerSet(lst):
    """take a list of items, return the powerset of the lst;
       author: Leo Yuanjie Li
       date: 10/11/2017
    """
    resultList = [[]]
    for item in lst:
        resultList.extend([[item] + res for res in resultList])
    return resultList
