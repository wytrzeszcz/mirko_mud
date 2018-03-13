import time
import wykop
import auth 
import sys
from random import randint
init_done = False 
while not init_done:
    try:
        api=wykop.WykopAPI(auth.appkey,auth.secretkey)
        api.authenticate(auth.login, auth.connection_key)
        init_done=True
    except:
        print "no auth???"
        print sys.exc_info()[0]
        time.sleep(120)
    
anserws={}
id_of_last_post=None;
while True:
    try:
        if id_of_last_post is not None:
            print id_of_last_post
            voters= api.get_entry(id_of_last_post)["voters"]
            respond="rozliczenie tury:"
            x=len(voters)-1;
            x=randint(0,x)
            i=0
            for vote in voters:
                print "@"+vote["author"]
                respond+="\n"
                respond+="@"+vote["author"]
                if(i!=x):
                    respond+=" :UMAR! bo nie umie grac i ma myszke na kulke"
                else:
                    respond+=" :WYGRAL BO MA NAJWIEKSZY PIWNY BRZUCH"
                i+=1
            api.add_entry_comment(id_of_last_post,respond)

        tekst="Na swojej drodze spoktales LAN-Party, aby zagrac z innymi we \"wstrzas\" daj plusa!\n zwyciezca tej smiertelnej bitwy moze byc tylko jeden!\n\nJest to wpis testowy dla zaprezentowania ideii #mudnamirko, opisy i ogolna logika bedzie oczywiscie lepsza\nmam nadzieje jednak ze wam sie podoba pomysl\n ! @wytrzzeszcz pilnuj "    
        id_of_last_post=api.add_entry(body=tekst,embed="https://i.ytimg.com/vi/AuAHg5ZPadA/maxresdefault.jpg")["id"] # emged=
    except:
            print "Sky is a limit, but API has limit too2"
            print sys.exc_info()[0]
            time.sleep(210) 		
    time.sleep(5*60);

