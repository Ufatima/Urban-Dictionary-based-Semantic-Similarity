import urbandictionary as ud
import numpy as np
import csv

sentence1 = []
sentence2 = []
with open ("mc_wordpair.csv", "r") as mfile:
    for line in mfile:
        linesp = line.split(",")
        term1 = linesp[0]
        term2 = linesp[1]
        print(term1,term2)
        def1 = ud.define(linesp[0])
        def2 = ud.define(linesp[1])
        l1 = []
        l2 = []
        for d in def1:
            like1 = d.upvotes
            l1.append(like1)
        for d in def2:
            like2 = d.upvotes
            l2.append(like2)
        if len(l1) != 0:
            if len(l2) != 0:
                maxl1 = max(l1)
                maxl2 = max(l2)
                print(maxl1,maxl2)
                s1 = []
                s2 = []
                for p in def1:
                    s = p.definition
                    s1.append(s)
                for q in def2:
                    ss = q.definition
                    s2.append(ss)
                for j in range(len(s1)):
                    sen1 = s1[j]
                    if l1[j] == maxl1:
                        print(s1[j])
                        n = [s1[j]]
                        sentence1.append(n)
                    #a = np.array(sentence1)
                    # with open('s1.csv', 'w', newline="") as f:
                    #     writer = csv.writer(f)
                    #     writer.writerows(a)

                for k in range(len(s2)):
                    sen2 = s2[k]
                    if l2[k] == maxl2:
                        print(s2[k])
                        m = [s2[k]]
                        sentence2.append(m)
                    #b = np.array(sentence2)
                    #with open('s2.csv', 'w', newline="") as f:
                        #writer = csv.writer(f)
                        #writer.writerows(b)