class ATM:
 bankName=""
 balance=0

 def __init__(self,bankName , balance):
    self.bankName = bankName
    self.balance = balance
    print "="*50
    print "Welcome to %r Bank" % self.bankName
    print "Your current balance is: %r" % self.balance
    print "="*50

 def WithDraw(self, request):
    if request > self.balance:
        print "can't give all this money"
    elif request <= 0 :
        print "no transaction to continue"    
    else:
        while request > 0:
            if request >= 100:
                print "give 100"
                request = request - 100
            elif request >= 50:
                print "give 50"
                request = request - 50
            elif request >= 20:
                print "give 20"
                request = request - 20
            elif request >= 10:
                print "give 10"
                request = request - 10
            elif request >= 5:
                print "give 5"
                request = request -5
            else:
                print ("give " + str(request))
                request = 0        
            
    return request
    
atm1 = ATM("NBE",5000)
request = atm1.WithDraw(10000)
print request

atm2 = ATM("HSBC",100000)
request = atm2.WithDraw(550)
print request
