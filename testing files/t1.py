def Withdraw(balance,request):
    if request > balance:
        print "can't give all this money"
    if request <= 0 :
        print "no transaction to continue"
    

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

request = Withdraw(1000,277)

print request