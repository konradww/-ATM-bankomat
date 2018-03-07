#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.INFO) #turn off logging
##########################
# This program is ATM.
# 
# I used greedy algorithm.
##########################

# all bank notes
class atm(object):
   cash ={
    500:20,
    200:19,
    100:18,
    50:17,
    20:16,
    10:15
   }
# sum of Bank notes
   def sumCash(self):
       sum = int(0)
       for key, value in self.cash.items():
            sum = sum + (key * value)

       logging.debug(sum)
       return sum

   def Person(self,limit):
    self.limit = limit

# How much money does he wants to take out?
   def HowMuchMoney(self,count):
       self.count = count
       logging.debug(count)
       if (count <= self.sumCash() and self.limit >= count and count % 10 == 0):
# More cash at the ATM #less cash than the limit #take out money  divided  without rest
# take out money:
# bank note 500
            if count >= 500 and self.cash[500]>0:
                if (count / 500) >  self.cash[500]:
                    print( "Bank note 500: %i" % self.cash[500])
                    count = count - 500 * self.cash[500]
                    self.cash[500]= self.cash[500] - self.cash[500]
                    logging.debug( self.cash[500])  #how many Bank notes left
                    print( "The remaining amount: %i" % count)
                else:
                    self.cash[500]= self.cash[500] - int(count / 500)
                    print( "Bank note 500: %i"% (count / 500))
                    count = count - 500 * int(count / 500)
                    logging.debug( self.cash[500])
                    print( "The remaining amount: %i" % count)
            else:
                pass
# 200
            if count >= 200 and self.cash[200]>0 and count>0:
                if (count / 200) >  self.cash[200]:
                    print( "Bank note 200: %i" % self.cash[200])
                    count = count - 200 * self.cash[200]
                    self.cash[200]= self.cash[200] - self.cash[200]
                    logging.debug( self.cash[500])
                    print( "The remaining amount: %i" % count)
                else:
                    self.cash[200]= self.cash[200] - int(count / 200)
                    print( "Bank note 200: %i"% (count / 200))
                    count = count - 200 *  int(count / 200)
                    logging.debug( self.cash[200])
                    print( "The remaining amount: %i" % count)
            else:
                pass
# 100
            if count >= 100 and self.cash[100]>0:
                if (count / 100) >  self.cash[100]:
                    print( "Banknot 100: %i" % self.cash[100])
                    count = count - 100 * self.cash[100]
                    self.cash[100]= self.cash[100] - self.cash[100]
                    logging.debug( self.cash[100])
                    print( "The remaining amount: %i" % count)
                else:
                    self.cash[100]= self.cash[100] - int(count / 100)
                    print( "Banknot 100: %i"% (count / 100))
                    count = count - 100 *  int(count / 100)
                    logging.debug( self.cash[100])
                    print( "The remaining amount: %i" % count)
            else:
                pass
# 50
            if count >= 50 and self.cash[50] > 0:
                if (count / 50) > self.cash[50]:
                    print("Bank note 50: %i" % self.cash[50])
                    count = count - 50 * self.cash[50]
                    self.cash[50] = self.cash[50] - self.cash[50]
                    logging.debug(self.cash[50])
                    print("The remaining amount: %i" % count)
                else:
                    self.cash[50] = self.cash[50] - int(count / 50)
                    print("Bank note 50: %i" % (count / 50))
                    count = count - 50 * int(count / 50)
                    logging.debug(self.cash[50])
                    print("The remaining amount: %i" % count)
            else:
                pass
#             if count >= 50 and self.cash[50]>0 and count>0:
#                 if (count / 50) >  self.cash[50]:
#                         if True:
#                             print( "Bank note 50: %i" % self.cash[50])
#                             count = count - 50 * self.cash[50]
#                             self.cash[50]= self.cash[50] - self.cash[50]
#                             logging.debug(self.cash[50])
#                             print( "The remaining amount: %i" % count)
#                         else:
#
#                             print( "go to bank note 20")
#                 else:
#                         #if (count - (50 * (self.cash[50]- int(count / 50)))) % 20 == 0: #zeby nie zostalo 30 np.
#                         if True:
#                             self.cash[50]= self.cash[50] - int(count / 50) # subtract with bank
#                             print( "Banknot 50: %i"% (count / 50))
#                             logging.debug(self.cash[50])
#                             count = count - 50 *  int(count / 50)
#
#                             print( "The remaining amount: %i" % count)
#                         else:
#                             self.cash[50]= self.cash[50] - ((count / 50)-1) # subtract with bank
#                             print( "Bank note 50: %i"% ((count / 50)-1))
#                             count = count - 50 * ((count / 50)-1)
#                             logging.debug( self.cash[50])
#                             print( "The remaining amount: %i" % count)
#
#
#                             print( "go to bank note20")
#
#             else:
#                 pass
# 20
            if count >= 20 and self.cash[20]>0 and count>0:
                if (count / 20) >  self.cash[20]:
                    print( "Banknot 20: %i" % self.cash[20])
                    count = count - 20 * self.cash[20]
                    self.cash[20]= self.cash[20] - self.cash[20]
                    logging.debug(self.cash[20])
                    print( "The remaining amount: %i" % count)
                else:
                    self.cash[20]= self.cash[20] - int(count / 20)
                    print( "Bank note 20: %i"% (count / 20))
                    count = count - 20 *  int(count / 20)
                    logging.debug(self.cash[20])
                    print( "The remaining amount: %i" % count)
            else:
                pass
# 10
            if count >= 10 and self.cash[10]>0 and count>0:
                if (count / 10) >  self.cash[10]:
                    print( "Banknot 10: %i" % self.cash[10])
                    count = count - 10 * self.cash[10]
                    self.cash[10]= self.cash[10] - self.cash[10]
                    logging.debug( self.cash[20])
                    print( "left to take out: %i" % count)
                else:
                    self.cash[10]= self.cash[10] - int(count / 10)
                    print( "Banknot 10: %i"% (count / 10))
                    count = count - 10 *  int(count / 10)
                    logging.debug( self.cash[10])
                    print( "The remaining amount: %i" % count)
            else:
                pass
            if count >0:
                print( "ATM doesnt have more bank note.")

       else:
           if self.limit < count:
               print( "Limit is too less")
           else:
                print( ("ATM empty"))


print(5 * '#####')

# amount to take out
x=980
print("amount to take out:",x)
obj1 = atm()
print("sum of bank notes:",obj1.sumCash())
print(5 * '#####')
# limit
obj1.Person(100000)
obj1.HowMuchMoney(x)

