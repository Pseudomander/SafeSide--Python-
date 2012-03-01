from SS import SafeSide2

mykey= raw_input('Please Insert Your Key:   \n  --> ')    
exiting= False
while exiting == False:
    A=''
    while (((A =='E') or (A =='e') or (A =='D') or (A =='d') or (A =='Q') or (A =='q')) != True):
        A= raw_input('Encrypt Decrypt or Quit? (E/D/Q)  :\n --> ')
    if ((A == 'E') or (A == 'e')):
        PT= raw_input('Please insert PlainText: \n  --> ')
        out= SafeSide2().encryptstr(mykey,PT)
        print out
    if ((A == 'D') or (A=='d')):
        CT= raw_input('Please insert CypherText: \n  --> ')
        out = SafeSide2().decryptstr(mykey,CT)
        print out
    if ((A == 'Q') or (A=='q')):
        exiting =True
