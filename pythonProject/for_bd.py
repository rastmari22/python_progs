p=[0,0,0,0,0,0,0,0]
n=[0,0,0,0,0,0,0,0]
import re
# for i in range(6):
#     p[i]=(input().split('.',1))
#     n[i]=p[i][1].split("-")
#     print(f'INSERT INTO STORE VALUES')
#     print(f'nextval("seq_store"),{n[i][0]},"{n[i][1]}");')
# p=[0,0,0,0,0,0,0,0]
# n=[0,0,0,0,0,0,0,0]
import random
q_dict=dict()
for i in range(401,410):
    q_dict[i]=random.randint(1,20)
print(q_dict)

postup=[]
prod=[]
qpost=dict()
nach=[]
for i in range(401,410):
    for j in range(301,305):
        [tov,mag,k]=i,j,random.randint(1,20)
        nach.append([tov,mag,k])
print(nach)
newnach=[]
for i in range(20):
    s=random.choice(nach)
    newnach.append(s)
    nach.remove(s)
    # print(newnach[i])

print(newnach)
for i in range(20):
    t,m,p=newnach[i]

    mes=(random.randint(3,6))
    den1=(random.randint(1,9))
    den2 = (random.randint(10, 30))

    dd_post=f'2023-0{mes}-0{den1}'
    mes2=random.randint(12-mes,12)
    dd_prod=f'2023-0{12-mes}-{den2}'
    dd_prod2 = f'2023-0{mes2 - mes}-{den2}'
    dpr=[dd_prod2,dd_prod]
    # p=q_dict[t]
    # print(f'nextval("seq_sale"),{dd},);')
    ps=(f"({t},{m},{p},'{dd_post}'),")
    postup.append(ps)
    q_prod=random.randint(1,p)
    pr=(f"(nextval('seq_sale'),{t},'{random.choice(dpr)}',{q_prod}),")
    prod.append(pr)

for i in range(20):
    print(postup[i])
#
for i in range(20):
     print(prod[i])