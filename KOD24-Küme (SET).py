#Kümenin diziden farkı tekrarlayan elemana izin vermez

kume1 = {1,2,5,8,9}
print(kume1)

kume2 = {1,2,3,6,6,2,7,7}
print(kume2)

kume3 = {"ben bir metinim, bir string ifadeyim"}
print(kume3)

kume4 =set("ben bir metinim, bir stein ifadeyim")
print(kume4)

# A-B kümesi
print(kume1.difference(kume2))

kume5 = [1,2,6,7,8,9,0,0,2,6]
print(set(kume5))
