balance = 500
requested=277
current = 0
counter = 0



while requested >=0:
	if (counter == 0):
		print "give 100";
		requested = requested - 100;
		counter=counter + 1;
	if (counter == 1):
		print "give 100";
		requested = requested - 100;
		counter=counter + 1;
	if (counter == 2):
		print "give 50";
		requested = requested - 50;
		counter=counter + 1;
	if (counter == 3):
		print "give 10";
		requested = requested - 10;
		counter=counter + 1;
	if (counter == 4):
		print "give 10";
		requested = requested - 10;
		counter=counter + 1;
	if (counter == 5):
		print "give 5";
		requested = requested - 5;
		counter=counter + 1;
	if (counter == 6):
		print "give 2";
		requested = requested - 2;
		counter=counter + 1;
