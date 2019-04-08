myList = ['advertisement', 'start', 'clever', 'billowy', 'melted', 'charge', 'longing', 'disgusting', 'phobic', 'carry', 'chew', 'big', 'mist', 'warn', 'faint']


def new_list(myList):
    newlist = []
    for word in myList:
        if 'a' in word:
            newlist.append(word)
    return newlist


print(new_list(myList))

