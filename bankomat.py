#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.INFO)
# turn off logging
#########################
# This program is ATM.
# I used greedy algorithm.
##########################

# all bank notes
class atm(object):
   cash = {
    500: 20,
    200: 19,
    100: 18,
    50: 17,
    20: 16,
    10: 15
   }
# sum of Bank notes
   def sumCash(self):
       sum = int(0)
       for key, value in self.cash.items():
            sum += (key * value)
       logging.debug(sum)
       return sum

   def Person(self,limit):
    self.limit = limit

# How much money does he wants to take out?
   def HowMuchMoney(self, count):
       self.count = count

       def banknote(denomination: object, count: object, limit: object, cash: object, sumCash: object) -> object:
            print(count)
            # if (count <= sumCash and limit >= count and count % 10 == 0):
            if count >= denomination and cash[denomination] > 0:
                if (count / denomination) > cash[denomination]:
                    print("Bank note %i: %i" % (denomination, cash[denomination]))
                    count = count - denomination * cash[denomination]
                    cash[denomination] = cash[denomination] - cash[denomination]
                    # logging.debug(cash[denomination])  # how many Bank notes left
                    print("The remaining amount: %i" % count)
                else:
                    cash[denomination] -= int(count / denomination)
                    print("Bank note %i: %i" % (denomination,  (count / denomination)))
                    count = count - denomination * int(count / denomination)
                    # logging.debug(self.cash[denomination])
                    print("The remaining amount: %i" % count)
            else:
                pass
            return count

       # TODO I need to create one method for all types of banknotes! - ok.
       banknotes = [500, 200, 100, 50, 20, 10]

       if (self.limit >= self.count <= self.sumCash() and self.count % 10 == 0):
           for bn in banknotes:
               self.count = banknote(bn, self.count, self.limit, self.cash, self.sumCash())
       else:
            if self.limit < self.count:
                print("Limit is too less")
            else:
                print(("ATM empty"))
# old comment
# if (count <= self.sumCash() and self.limit >= count and count % 10 == 0):
# More cash at the ATM #less cash than the limit #take out money  divided  without rest
# take out money:

print(5 * '#####')
# amount to take out
x = 1980
print("amount to take out:", x)
obj1 = atm()
print("sum of bank notes:", obj1.sumCash())
print(5 * '#####')
# limit
obj1.Person(100000)
obj1.HowMuchMoney(x)

