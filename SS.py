class SafeSide2:
    def characterset(self,start):
        cset=[]
        for i in range(126-start):
            place = abs(round(( (i-1) *3.6 +i ))) % (len(cset) +1)
            cset.insert( place , chr( i + start ) )
        return cset
    def strtocsetind(self,string,cset):
        outp=[]
        for i in range( len(string) ):
            outp.insert(i,cset.index(string[i]))
        return outp
    def cropstr(self,string,cset):
        outp=''
        for i in range( len(string )):
            if (string[i] in cset) == True:
                outp= outp+string[i]
        return outp
    def csettostrind(self,string,cset):
        outp=''
        for i in range(len(string)):
            outp= outp+ cset[string[i]] 
        return outp
    def Keyset(self,key,cset):
        Set=[]
        for i1 in range(len(key)):
            for i2 in range(len(key)):
                Set.insert(i1*len(key)+i2,(key[i1]+key[i2]+((i1*7)%45) -((i1*6)%8) +i1+i2)%len(cset))
        return Set
    def encryptstr(self,key,string):
        cset= self.characterset(32)
        Key = self.strtocsetind(self.cropstr(key,cset),cset)
        Extendedkey= self.Keyset(Key,cset)
        plaintext= self.strtocsetind(self.cropstr(string,cset),cset)
        ciphertext=[]
        for i in range(len(plaintext)):
            ciphertext.insert(i,(plaintext[i]+i+Extendedkey[i%len(Extendedkey)])%len(cset))
        return self.csettostrind(ciphertext,cset)
    def decryptstr(self,key,string):
        cset= self.characterset(32)
        Key = self.strtocsetind(self.cropstr(key,cset),cset)
        Extendedkey= self.Keyset(Key,cset)
        plaintext= self.strtocsetind(self.cropstr(string,cset),cset)
        ciphertext=[]
        for i in range(len(plaintext)):
            ciphertext.insert(i,(plaintext[i]-i-Extendedkey[i%len(Extendedkey)])%len(cset))
        return self.csettostrind(ciphertext,cset)

    
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
    if ((A == 'q') or (A=='q')):
        exiting =True
