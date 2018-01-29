'''
Created on 2016-3-30

@author: huikeli
'''
# coding = utf8
import random
import datetime
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import itertools
from numpy.core.numeric import nan
from math import exp

from Decompose import decompose
from CalHeteSim import normMat, calHete

def calImportance(path):
    strenth = 0
        
    for index in range(len(path) - 1):
        strenth = strenth + calAveDegree(path[index:index+2]);
        
    importance = exp(strenth - (len(path)-1))
    
    return importance

def calSim(source):
    calSameSim(source)
    calDifSim(source)
    
def calADGSameSim(source, type):
    # get every path
    num = Len / 2
    
    l = ['MA', 'MD', 'MG']
    print l
    pathList = []
    qqq = []
    for j in range(1, num):
        temp = itertools.combinations_with_replacement(l, j) 
        ppp = list(temp) 
        for i in ppp:
            temp1 = itertools.permutations(i, j)
            qqq = list(set(list(temp1) + qqq))
    for i in qqq:
        a = ''.join(list(i))
        pathList.append(a)
    
    totalImportance = 0
    ch = 'A'
    if type == 1:
        sim = [0]*actorNum
        ch = 'A'
    elif type == 2:
        sim = [0]*directorNum
        ch = 'D'
    elif type == 3:
        sim = [0]*genreNum
        ch = 'G'
    
    l1 = []
    # modify later, only implement source is movie, cannot change langth
    
    for j in pathList:
        a = calImportance(ch+j+'M'+ch)
        totalImportance += a
        l1.append(a)
        
    for j in range(len(pathList)):
        wi = l1[j] / totalImportance
        temp = calHeteSim(source, ch+pathList[j]+'M'+ch)
        for k in range(len(temp)):
            sim[k] += wi * temp[k]
    
    
    n = 1
    if type == 1:
        print 'actor:'
        n = 70000
    elif type == 2:
        print 'director:'
        n = 170000
    elif type == 3:
        print 'genre:'
        n = 180000   
    copy = sim[:]
    correct = 0
    maxv = 1
    i = 1
    mrr = 0.0
    aa = 20 # number of results
    for j in range(aa):
        a = max(sim)
        if a == 0:
            break
        b = sim.index(a)
        if gdSt[b] == 1:
            correct += 1
            if mrr == 0.0 and j != 0:
                mrr = 1.0/(j)
            
        c = idList.index(n+b)
        print '%d' %(j+1) + ' ' + nameList[c]
        sim[b] = 0
#     print mrr
    print copy
#     print correct # of correct
    return correct #return copy
def calSameSim(source):
    # get every path
    num = Len / 2
    
    l = ['MA', 'MD', 'MG']
    pathList = []
    qqq = []
    for j in range(1, num+1):
        temp = itertools.combinations_with_replacement(l, j) 
        ppp = list(temp) 
        for i in ppp:
            temp1 = itertools.permutations(i, j)
            qqq = list(set(list(temp1) + qqq))
            
#     print qqq
    for i in qqq:
        a = ''.join(list(i))
        pathList.append(a)
    
#     print pathList
    totalImportance = 0
#     simRank = [0]*movieNum
    sim = [0]*movieNum
    l1 = []
    # modify later, only implement source is movie, cannot change langth
    
    for j in pathList:
        a = calImportance(j+'M')
        totalImportance += a
        l1.append(a)
        
    for j in range(len(pathList)):
        wi = l1[j] / totalImportance
        temp = calHeteSim(source, pathList[j]+'M')
        for k in range(len(temp)):
            sim[k] += wi * temp[k]
#             if pathList[j][0:len(pathList[j])/2] == pathList[j][len(pathList[j])/2:len(pathList[j])]:
# #                 print pathList[j][0:len(pathList)/2], pathList[j][len(pathList)/2:len(pathList)]
#                 simRank[k] += temp[k] 
    
    print 'movie:'   
    copy = sim[:]
    correct = 0
    mrr = 0.0
    aa = N # number of results
    for j in range(aa):
        n = 1
        a = max(sim)
        if a == 0:
            break
        b = sim.index(a)
        if gdSt[b] == 1:
            correct += 1
            if mrr == 0.0 and j != 0:
                mrr = 1.0/(j)
            
        c = idList.index(n+b)
        print '%d' %(j+1) + ' ' + nameList[c]
        sim[b] = 0
        
#     copy1 = simRank[:]
#     correct1 = 0
#     mrr1 = 0.0
#     for j in range(aa):
#         n = 1
#         a = max(simRank)
#         if a == 0:
#             break
#         b = simRank.index(a)
#         if gdSt[b] == 1:
#             correct1 += 1
#             if mrr1 == 0.0 and j != 0:
#                 mrr1 = 1.0/(j)
#             
#         c = idList.index(n+b)
# #         print '%d' %(j+1) + ' ' + nameList[c]
#         simRank[b] = 0
    
#     print mrr
    print copy
#     print correct # of correct
    return correct #return copy
def calSimRank(source):
     # get every path
    num = Len / 2
    
    l = ['MA', 'MD', 'MG']
    print l
    pathList = []
    qqq = []
    for j in range(1, num+1):
        temp = itertools.combinations_with_replacement(l, j) 
        ppp = list(temp) 
        for i in ppp:
            temp1 = itertools.permutations(i, j)
            qqq = list(set(list(temp1) + qqq))
    for i in qqq:
        a = ''.join(list(i))
        pathList.append(a)
    
    totalImportance = 0
    sim = [0]*movieNum
    l1 = []
    # modify later, only implement source is movie, cannot change langth
    
    for j in pathList:
        a = calImportance(j+'M')
        totalImportance += a
        l1.append(a)
        
    for j in range(len(pathList)):
        wi = l1[j] / totalImportance
        temp = calHeteSim(source, pathList[j]+'M')
        for k in range(len(temp)):
            sim[k] += wi * temp[k]
    
    print 'movie:'   
    copy = sim[:]
    correct = 0
    maxv = 1
    i = 1
    mrr = 0.0
    aa = 20 # number of results
    for j in range(aa):
        n = 1
        a = max(sim)
        if a == 0:
            break
        b = sim.index(a)
        if gdSt[b] == 1:
            correct += 1
            if mrr == 0.0 and j != 0:
                mrr = 1.0/(j)
            
        c = idList.index(n+b)
        print '%d' %(j+1) + ' ' + nameList[c]
        sim[b] = 0
    print mrr
    print copy
    print correct # of correct
    return correct #return copy
def calDifSim(source):
    # get every path
    num = Len / 2
    l = ['AM', 'DM', 'GM']
    pathListA = []
    pathListD = []
    pathListG = []
    qqq = []
    for j in range(1, num + 1):
        temp = itertools.combinations_with_replacement(l, j) 
        ppp = list(temp) 
        for i in ppp:
            temp1 = itertools.permutations(i, j)
            qqq = list(set(list(temp1) + qqq))
    for i in qqq:
        a = ''.join(list(i))
        pathListA.append('M'+a+'A')
        pathListD.append('M'+a+'D')
        pathListG.append('M'+a+'G')
    
    pathListA.append('MA')    
    pathListD.append('MD')    
    pathListG.append('MG')
    
    totalImportance = 0
    simA = [0]*actorNum
    simD = [0]*directorNum
    simG = [0]*genreNum
    l1 = []
    # modify later, only implement source is movie, cannot change langth
    
    for j in pathListA:
        a = calImportance(j)
        totalImportance += a
        l1.append(a)
        
    for j in range(len(pathListA)):
        wi = l1[j] / totalImportance
        temp = calHeteSim(source, pathListA[j])
        for k in range(len(temp)):
            simA[k] += wi * temp[k]
    
    print 'actor:'     
    copy = simA[:]
    for i in range(N):
        n = 70000
        a = max(simA)
        b = simA.index(a)
        c = idList.index(n+b)
        print '%d' %(i+1) + ' ' + nameList[c]
        simA[b] = 0
    print copy
    
    for j in pathListD:
        a = calImportance(j)
        totalImportance += a
        l1.append(a)
        
    for j in range(len(pathListD)):
        wi = l1[j] / totalImportance
        temp = calHeteSim(source, pathListD[j])
        for k in range(len(temp)):
            simD[k] += wi * temp[k]
    
    print 'director:'     
    copy = simD[:]
    for i in range(N):
        n = 170000
        a = max(simD)
        b = simD.index(a)
        c = idList.index(n+b)
        print '%d' %(i+1) + ' ' + nameList[c]
        simD[b] = 0
    print copy
    
    for j in pathListG:
        a = calImportance(j)
        totalImportance += a
        l1.append(a)
        
    for j in range(len(pathListG)):
        wi = l1[j] / totalImportance
        temp = calHeteSim(source, pathListG[j])
        for k in range(len(temp)):
            simG[k] += wi * temp[k]
    
    print 'genre:'     
    copy = simG[:]
    for i in range(N):
        n = 180000
        a = max(simG)
        b = simG.index(a)
        c = idList.index(n+b)
        print '%d' %(i+1) + ' ' + nameList[c]
        simG[b] = 0
    print copy
    
    return copy

# def normMat(mat):  
def calHeteSim(source, path):
    n = 0
    if path[0] == 'A':
        n = 70000
    elif path[0] == 'D':
        n = 170000
    elif path[0] == 'G':
        n = 180000
    elif path[0] == 'M':
        n = 1
        
    id = getId(source)
    pathList = decompose(path)
    first = pathList[0]
    second = pathList[1]
    
    a = np.zeros((1,1));
    b = np.zeros((1,1));
    a = getAdjMat(first[0], second[0])[id-n, :]
    a = np.array([a])
    
    for i in range(1, len(first)):
        m = getAdjMat(first[i], second[len(second)-1])
        a = np.dot(a, m)
        
    b = getAdjMat(second[len(second) - 1], first[len(first) - 1]).T
         
    for i in range(len(second) - 1)[::-1]:   
        m = getAdjMat(second[i], first[len(first) - 1]).T  
        b = np.dot(b, m)
        
    heteList = list(calHete(a,b)[0, :])
    
    return heteList

def getAdjMat(item, item1):
    if item == 'MA':
        a = MAmatrix
    elif item == 'MD':
        a = MDmatrix
    elif item == 'MG':
        a = MGmatrix
    elif item == 'AM':
        a = MAmatrix.T
    elif item == 'DM':
        a = MDmatrix.T
    elif item == 'GM':
        a = MGmatrix.T
    elif item == 'M*':
        if item1 == 'A*':
            a = MAstar
        elif item1 == 'D*':
            a = MDstar
        elif item1 == 'G*':
            a = MGstar
    elif item == 'A*':
        a = starMA.T
    elif item == 'D*':
        a = starMD.T  
    elif item == 'G*':
        a = starMG.T
    return a
   
def calAveDegree(temp): 
    if temp == 'MA' or temp == 'AM':
        s = (onesInMA * onesInMA / movieNum / actorNum) ** (-alpha)
    elif temp == 'MD' or temp == 'DM':
        s = (onesInMD * onesInMD / movieNum / directorNum) ** (-alpha)
    elif temp == 'MG' or temp == 'GM':
        s = (onesInMG *onesInMG / movieNum / genreNum) ** (-alpha)
    
    return s
 
def multiMatrix(m1, m2):
    return np.dot(m1, m2)
 
def getId(name):
    ind = nameList.index(name)
    return idList[ind]

#start program
startTime = datetime.datetime.now()

movieNodes = pd.read_csv('F:/bysj/movielens/v_part1.csv')
movieEdges = pd.read_csv('F:/bysj/movielens/e_part1.csv')
# print movieNodes.ix274]
# print movieName.head[()
# print movieName.columns
# i = 0

# construct graph
alpha = 0.5
Len = 5
N = 10

g = nx.Graph()
colorList = [] # color of nodes
labelList = [] # label of nodes
nameList = [] # name of nodes
idList = [] # id of nodes
typeList = []
startList = [] # start node of edges
movieList = []
actorList = []
directorList = []
genreList = []
endList = []
movieNum = 0 
actorNum = 0 
directorNum = 0 
genreNum = 0 
onesInMA = 0 #numbers of 1 in MAmatrix
onesInMD = 0
onesInMG = 0
for n in movieNodes.values:
    if n[1] is nan:
        break
    g.add_node(n[0], name = n[1], nameType = n[2])
    nameList.append(n[1])
    idList.append(n[0])
    typeList.append(n[2])
    if n[2] == 'movie':
        colorList.append('r')
        labelList.append('movie')
        movieNum+=1
    elif n[2] == 'actor':
        colorList.append('b')
        labelList.append('actor')
        actorNum+=1;
    elif n[2] == 'director':
        colorList.append('g')
        labelList.append('director')
        directorNum+=1;
    elif n[2] == 'genre':
        colorList.append('w')
        labelList.append('genre')
        genreNum+=1;
        
for n in movieEdges.values:
    if n[1] is nan:
        break
    g.add_edge(n[1],n[2])
    startList.append(n[1])
    endList.append(n[2])
    if n[2] >= 70000 and n[2] < 170000:
        onesInMA += 1
    elif n[2] >= 170000 and n[2] < 180000:
        onesInMD += 1
    else:
        onesInMG += 1
        
        
# # figure of the network
# pos = nx.spring_layout(g)
# nx.draw_networkx_nodes(g, pos, node_color = colorList)
# nx.draw_networkx_edges(g, pos)
# # nx.draw_networkx_labels(g, pos, label = labelList)
# nx.draw(g)
# plt.show()

MAstar = np.zeros((movieNum, onesInMA))
starMA = np.zeros((onesInMA, actorNum))
MDstar = np.zeros((movieNum, onesInMD))
starMD = np.zeros((onesInMD, directorNum))
MGstar = np.zeros((movieNum, onesInMG))
starMG = np.zeros((onesInMG, genreNum))
MAmatrix = np.zeros((movieNum, actorNum))
MDmatrix = np.zeros((movieNum, directorNum))
MGmatrix = np.zeros((movieNum, genreNum))

count1 = 0
count2 = 0
count3 = 0
for i in range(len(startList)):
    if endList[i] >= 70000 and endList[i] < 170000:
        MAmatrix[startList[i]-1, endList[i]-70000] = 1
        MAstar[startList[i]-1, count1] = 1
        starMA[count1, endList[i]-70000] = 1
        count1 += 1
    elif endList[i] >= 170000 and endList[i] < 180000:
        MDmatrix[startList[i]-1, endList[i]-170000] = 1
        MDstar[startList[i]-1, count2] = 1
        starMD[count2, endList[i]-170000] = 1
        count2 += 1
    else:
        MGmatrix[startList[i]-1, endList[i]-180000] = 1
        MGstar[startList[i]-1, count3] = 1
        starMG[count3, endList[i]-180000] = 1
        count3 += 1

MAM = np.dot(MAmatrix, MAmatrix.T)
MGM = np.dot(MGmatrix, MGmatrix.T)
MDM = np.dot(MDmatrix, MDmatrix.T)
MM = MAM+MDM
gdSt = [0]*movieNum
length = 0
for i in range(np.shape(MM)[0]):
    for j in range(i+1, np.shape(MM)[1]):
        if MM[i][j] >= 2:
            if gdSt[i] == 0:
                gdSt[i] = 1
                length += 1 
            if gdSt[j] == 0:
                gdSt[j] = 1
                length += 1
            
print length
# normalization
MAstar = normMat(MAstar)
starMA = normMat(starMA)
MDstar = normMat(MDstar)
starMD = normMat(starMD)
MGstar = normMat(MGstar)
starMG = normMat(starMG)
MAmatrix = normMat(MAmatrix)
MDmatrix = normMat(MDmatrix)
MGmatrix = normMat(MGmatrix)
 
print 'semantic:'    
path = 'AMGM'  
heteList = calHeteSim('Harvey Keitel', path)
print heteList
a = 1
for i in range(N):
    if a == 0:
        break
    n = 1
    if path[len(path) - 1] == 'A':
        n = 70000
    elif path[len(path) - 1] == 'D':
        n = 170000
    elif path[len(path) - 1] == 'G':
        n = 180000
    a = max(heteList)
#     print a
    b = heteList.index(a)
    c = idList.index(n+b)
    print '%d' %(i+1) + ' ' + nameList[c]
    heteList[b] = 0
          
print
endTime1 = datetime.datetime.now()

print 'relevance:'     
calDifSim('Toy story')
correct = calSameSim('Toy story')

# correct = calADGSameSim('Tom Hanks', 1)
# print correct

endTime2 = datetime.datetime.now()

semanticTime = endTime1 - startTime
relevanceTime = endTime2 - startTime
print semanticTime, relevanceTime

#Fmeasure
# qqq = 0.0
# qqq1 = 0.0
# rrr = 0.0
# rrr1 = 0.0
# for i in range(10):
#     k = random.randint(0, 400)
#     #randomly pick a movie num in namelist
#     kk = calSameSim(nameList[i])
#     qqq += kk[0]
#     qqq1 += kk[1]
#     rrr += kk[2]
#     rrr += kk[3]
#      
# print qqq / N / 10, qqq1 / N / 10
# print rrr / N, rrr1 / N

# calHeteSim('Toy story', 'MDM')
# calHeteSim('Toy story', 'MGM')
# print getId('Annie Potts')
# print g.nodes(data=True)    
# print g.edges()
# print len(g.edges())
# print g.edges

# i = g.number_of_nodes()
# g.nodes(data=True)
# print g.node[1]
# print g.node[1]['id']
# lista = []
# count = 0
# while (count < len(g.node)): 
#     lista.append(g.node[count]['id'])
# for n in movieDirector.values:
#     g.
#     g.add_edge(n[0], i)

# print g.node
