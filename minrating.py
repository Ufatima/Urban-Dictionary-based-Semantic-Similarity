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
        ul1 = []
        ul2 = []
        for d in def1:
            unlike1 = d.downvotes
            ul1.append(unlike1)
        for d in def2:
            unlike2 = d.upvotes
            ul2.append(unlike2)
        if len(ul1) != 0:
            if len(ul2) != 0:
                maxul1 = max(ul1)
                maxul2 = max(ul2)
                print(maxul1,maxul2)
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
                    if ul1[j] == maxul1:
                        print(s1[j])
                        n = [s1[j]]
                        sentence1.append(n)
                    # a = np.array(sentence1)
                    # with open('uls1.csv', 'w', newline="") as f:
                    #      writer = csv.writer(f)
                    #      writer.writerows(a)
                for k in range(len(s2)):
                    sen2 = s2[k]
                    if ul2[k] == maxul2:
                        print(s2[k])
                        m = [s2[k]]
                        sentence2.append(m)
                    # b = np.array(sentence2)
                    # with open('uls2.csv', 'w', newline="") as f:
                    #     writer = csv.writer(f)
                    #     writer.writerows(b)