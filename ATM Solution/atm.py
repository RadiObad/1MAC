balance = 500
current = 0

#to define money categories based on user selection
moneyCategroies = [100,100,50,10,10,5,2]

for x in moneyCategroies:
	balance = balance - x;
	current = current+x;
	print "give %r" % x	

print "withdrawn amount is %r" % current
print "your current balance is %d" % balance
