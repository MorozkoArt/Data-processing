def allChildren(parent):
    counter = 0
    children = []
    if type(parent).__name__ == "list":
        return parent
    if type(parent).__name__ != "dict":
        return []
    for child in parent.values():
        children += allChildren(child)
    return children