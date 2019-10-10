#!/usr/bin/env python
# coding: utf-8

# In[184]:


import csv
import apyori as ap
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd


# In[205]:


def display_rules(association_results):
    d = []
    for item in association_results:
        # first index of the inner list
        # Contains base item and add item
        pair = item[0]
#         print("pair", len(pair))
        if len(pair) == 1:
            continue
        items = [x for x in pair]
#         print(items)
        if 'nan' in items:
            continue

        # print("item",item)
#         print('item[2][0][1]',str(item[2][0][1]))
#         print('item[2][0][0]',str(item[2][0][0]))
        LL = len(item[2])
#         print("lenght",LL)
        for tt in range(0, LL):
            A_items = [x for x in item[2][tt][0]]
            B_items = [x for x in item[2][tt][1]]
#             print("A_items",A_items)
#             print("B_items",B_items)
            d.append(str(A_items) + " -> " + str(B_items))
            #         print("Rule: " + item[2][0][0] + " -> " + item[2][0][1])

            # second index of the inner list
            #print("Support: " + str(item[1]))

            # third index of the list located at 0th
            # of the third index of the inner list

            #print("Confidence: " + str(item[2][tt][2]))
            #print("Lift: " + str(item[2][tt][3]))
            # print("=====================================")
    return d


# In[197]:


# #Toy example 2
# transactions_2 = [
#     ['Bread', 'Milk', 'Chips', 'Mustard'],
#     ['Beer', 'Diaper', 'Bread', 'Eggs'],
#     ['Beer', 'Coke', 'Diaper', 'Milk'],
#     ['Beer', 'Bread', 'Diaper', 'Milk','Chips'],
#     ['Coke', 'Bread', 'Diaper', 'Milk'],
#     ['Beer', 'Bread', 'Diaper', 'Milk','Mustard'],
#     ['Coke', 'Bread', 'Diaper', 'Milk'],

# ]
# #print("transactions_2",transactions_2)


# In[198]:


def association(datafile, min_sup, min_conf):
    datafile = open(datafile, 'r')
    datareader = csv.reader(datafile)
    transactions_2 = []
    for row in datareader:
        transactions_2.append(row)

    association_rules = ap.apriori(transactions_2, min_support=min_sup, min_confidence=min_conf)
    association_results = list(association_rules)
    # print(association_results)
    # print(association_results)
    #print("------------list of rules------------")
    # display_rules(association_results)
    a = []
    for i in range(len(association_results)):
        a.append(association_results[i][0])
    b = []
    for i in range(len(association_results)-1):
        for j in range(i, len(association_results)):
            if set(association_results[i][0]) < set(association_results[j][0]):
                b.append(association_results[i][0])
                break
    c = [i for i in a if i not in b]
    d = display_rules(association_results)
    return a, c, d
