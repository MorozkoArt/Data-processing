def listsCompare(first, second):
    for i in range(len(first)):
        if first[i] != second[i]:
            return False
    return True