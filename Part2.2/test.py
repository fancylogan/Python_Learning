# import pickle

# def savedic(dic):
#     with open ("db.pkl","wb") as f :
#         pickle.dump(dic,f)

# def readdic():
#     with open ("db.pkl","rb") as f :
#         c = pickle.load(f)
#         return c 

# dic = {}
# dic[1] = "a"
# dic[2] = "b"
# savedic (dic)
# print(readdic())


a = []
a.append([1,2,3])
a.append([11,33,22])
a[1]=[44,444,44]
print (a)
