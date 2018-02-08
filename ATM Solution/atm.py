balance = 800
current = 0
insuffBal = 0;

moneyCategroies = [100,100,100,100,50,50,50,50,50,50,25,25,25,25,10,10,5,2]

for x in moneyCategroies:
	balance = balance - x;
	current = current+x;
	if balance < 0:
		print "Insufficient balance;";
		insuffBal = 1;
		break;
	print "give %r" % x	

if insuffBal == 0:
	print "withdrawn amount is %r" % current
	print "your current balance is %d" % balance
else:
	print "failed transaction"
