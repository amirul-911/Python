#copy string1 to string2 and delete duplicate content

def removeduplicate(list, n):
    idx = 0
    for i in range(0, n):
        for j in range(0, i+1):
            if (latestnames[i] == latestnames [j]):
                break
        if (j == i):
            latestnames[idx] = latestnames[i] #print into latest string 
            idx += 1

    return " , ".join(latestnames[:idx]) #return new 'joined' string separated by ',' from 0 until latest idx

fewnames = ['John','barry','mary','jane','philip']
manynames = ['rahim','karim','sabri','John','leo',
             'safik','barry','mary','saif','adrian',
             'jane','sahil','chong','philip','adnan']

latestnames = fewnames + manynames #combine 2 strings into new string
n = len(latestnames)

print(removeduplicate(list(latestnames), n)) #call function remove duplicate sending new string list and length of new string
