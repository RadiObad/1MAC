class ATM:
 #bankName=""
 #balance=0

 def __init__(self,bankName , balance):
    self.bankName = bankName
    self.balance = balance
    self.withDrawalList=[]
    print "="*50
    print "Welcome to %r Bank" % self.bankName
    print "Your current balance is: %r" % self.balance
    print "="*50

 def Calculate(self,request):
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
        if request > 0:
            self.withDrawalList.append(request)
    return request

 def WithDraw(self, request):
    if request > self.balance:
        print "can't give all this money"
    elif request <= 0 :
        print "no transaction to continue"    
    else:
        request = self.Calculate(request)                     
    return request

 def PrintWithDrawHistory(self):
     for withdrawProcess in self.withDrawalList:
         print ("you withdraw: {0}".format(withdrawProcess))

atm2 = ATM("HSBC",100000)
request = atm2.WithDraw(550)
atm2.PrintWithDrawHistory()