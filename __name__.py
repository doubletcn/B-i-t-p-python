# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 22:55:50 2023

@author: ADMIN
"""



# list1=[1,2,'3',True]
# list2=list1+['5', 'sáu']
# print(list1)
# print(list2)


# from audioop import reverse


# emails=["ttceen@gmail.com","thanhtrungcn@gmail.com","thanhtrungbbox@gmail.com"]
# emails.extend([10,'122'])
# # result=[]
# # for email in emails:
# #     user_name=email[0:email.index("@")]
# #     domain_name=email[email.index("@")+1:]
# #     result.append([user_name])
# print(emails[::-1])

# print(list(reversed(emails)))
# if result.reverse()==result:

# # def in2(result):
# #     print(result)

                                        #lambda
                            #map: chuyển đổi các thành phần trong list
                            #filter: lọc các thành phần trong list
                            #reduce: thực hiện func cho ra 1 giá trị đơn lặp
# from functools import reduce
# sequence=["chu", "nguyen", "thanh", "trung"]
# seq=[1,4,6,9,3]
# print(reduce(lambda a,b: a if a>b else b,seq))

# print(list(filter(lambda i: i%2!=0,seq)))

# print(list(map(lambda word: word.title(),sequence)))
# people=[
#     {'ten':'trung', 'tuoi':'26'},
#     {'ten':'huyen', 'tuoi':'21'},
#     {'ten':'anh', 'tuoi':'30'},
# ]
# def f(people):
#     return people['ten']
# people.sort(key=f, reverse=True )
# print(people)

def foo(*args):
    for arg in args:
        print(1)

foo(1, 2, 3, 4, 5) # In ra các số từ 1 đến 5


