class Sell:
    adult_workday_price = 100
    adult_weekend_price = adult_workday_price*1.2
    child_workday_price = adult_workday_price/2
    child_weekend_price = adult_weekend_price/2
    def workdayprice(self,adult,child):
        print('一共是%.2f元'%(self.adult_workday_price * adult + self.child_workday_price * child))
    def weekendprice(self,adult,child):
        print('一共是%.2f元'%(self.adult_weekend_price * adult + self.child_weekend_price * child))
    
