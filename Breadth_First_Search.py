from collections import deque
graph={}
graph["you"]=["alice","bob","claire"]
graph["bob"]=["anuj","peggy"]
graph["alice"]=["peggy"]
graph["claire"]=["thom","jonny"]
graph["anuj"]=[]
graph["peggy"]=[]
graph["thom"]=[]
graph["jonny"]=[] #空的部分一定要加上，不然计算过程会断了000·                                     
def search(name):
    search_queue=deque()
    search_queue+=graph[name]
    searched=[]
    while search_queue:
        person=search_queue.popleft()
        if not person is searched:
            if person_is_seller(person):
                print person+" is a mango seller!"
            else:
                search_queue+=graph[person]
                searched.append(person)
    return False
def person_is_seller(name):
    return name[-1]=='m'
search("you")
