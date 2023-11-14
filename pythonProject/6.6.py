class Link:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkList:
    def __init__(self):
        self.first=None
    def push(self, el):
        new_link=Link(el)
        if self.first is None:
            self.first=new_link
        else:
            cur=self.first
            while cur.next:
                cur=cur.next
            cur.next=new_link
    def get(self, index_of_el):
        leng=0
        cur=self.first
        while cur:
            leng+=1
            cur=cur.next
        try:
            if leng<=0 or index_of_el>leng or index_of_el<=0:
                raise IndexError("Ошибка! Неправильный индекс! ")
                # return
        except IndexError as err:
            # print(err)
            return err
        el = self.first

        for i in range(index_of_el-1):
            el=el.next

        d=el.data
        # self.first=None
        return d

linklist=LinkList()
print(linklist.get(3))
linklist.push(11)
linklist.push(21)
linklist.push(31)

# linklist.get(1)
print(linklist.get(1))
print(linklist.get(2))
print(linklist.get(3))
print(linklist.get(7))

from Dist import Dist
d1=Dist(10,15.4)
d2=Dist(4,12.3)
d3=Dist(34,18)
dist_link_list=LinkList()
dist_link_list.push(d1)
dist_link_list.push(d2)
dist_link_list.push(d3)

# linklist.get(1)
print(dist_link_list.get(1))
print(dist_link_list.get(2))
print(dist_link_list.get(3))
print(dist_link_list.get(3))
