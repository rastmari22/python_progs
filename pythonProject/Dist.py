class Dist:
    # def __init__(self):
    # meters, centimeters=0,0.0


    def __init__(self,mt,cm):
        self.meters=mt
        self.centimeters=cm
    def get_diist(self):
        self.meters=int(input())
        self.centimeters=float(input())

    def show_dist(self):
        print(f"{self.meters} м {self.centimeters} см")

    def __add__(self, d2):
        met=self.meters+d2.meters
        cem=self.centimeters+d2.centimeters

        if cem>=100:
            cem-=100
            met+=1
        return Dist(met,cem)

    def __lt__(self, d2):
        bd1=float(self.meters+self.centimeters/100.)
        bd2=float(d2.meters+d2.centimeters/100.)
        return bd1<bd2
    def __le__(self, d2):
        return self<d2 or self==d2
    def __gt__(self, d2):
        bd1 = float(self.meters + self.centimeters / 100.)
        bd2 = float(d2.meters + d2.centimeters / 100.)
        return bd1 > bd2
    def __ge__(self, d2):
        return self>d2 or self==d2
    def __sub__(self, d2):
        if not self<d2:
            # alc2=d2.meters*100+d2.centimeters
            # alc1=self.meters*100+self.centimeters
            c=self.meters*100+self.centimeters-d2.meters*100+d2.centimeters
            m=0
            while c>=100:
                m+=1
                c-=100
            return Dist(m,c)
    def __mul__(self, d2):
        c =( d2.meters * 100 + d2.centimeters) * (self.meters * 100 + self.centimeters)
        m=0
        while c>=100:
            m+=1
            c-=100
        return Dist(m,c)
    def __truediv__(self, d2):
        c = (d2.meters * 100 + d2.centimeters) / (self.meters * 100 + self.centimeters)
        m = 0
        while c >= 100:
            m += 1
            c -= 100
        return Dist(m, c)
    def __str__(self):
        return f"{self.meters} м {self.centimeters} см"
    def __eq__(self,d2):
        return self.meters*100+self.centimeters==d2.meters*100+d2.centimeters
    def __ne__(self, d2):
        return not self==d2

