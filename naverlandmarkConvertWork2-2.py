def createDir(path):
    if os.path.exists(path):
        return -1
    os.mkdir(path)
    
def pprint(iterable):
    for iter in iterable:
        print(iter)
def customOsWalk(path):
    res = []
    for root, dirs, files in os.walk(path, topdown=WALK_OPT_TOPDOWN):
        if not dirs: # 트리 마지막 노드만 필터링
           res.append(root)
    return sorted(res)

pprint(customOsWalk('134-pt'))


def cutLevel1Dirname(relpath):
    regexPattern = re.compile('pt(.*)')
    res = regexPattern.search(relpath)
    res = res[1] if res else -1
    print('-' * 50)
    print(relpath)
    print(res)
    return res
    # re.search('pt(.*)', relpath)
cutLevel1Dirname('106-pt/1-10/0--Parade - 최석원')


PATH_38PT = './38-pt'
PATH_106PT = './106-pt'
PATH_134PT = './134-pt'

print(os.getcwd())

subdir38pt = customOsWalk(PATH_38PT)
subdir106pt = customOsWalk(PATH_106PT)
subdir134pt = customOsWalk(PATH_134PT)

pprint(subdir38pt)
pprint(subdir106pt)
pprint(subdir134pt)



for subdir in subdir38pt:
    print(subdir)
    # t1, t2, t3 = re.split(os.sep, subdir)
    # print(t1, t2, t3)
    res = re.split(os.sep, subdir)
    print(res)
    break
