import time
import wykop
import auth 
import sys

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
            for vote in voters:
                print "@"+vote["author"]
                respond+="\n"
                respond+="@"+vote["author"]+" :UMAR! bo nie ma tu jeszcze zadnej logiki, ale wiem ze zaplusowane dziekuje"
            api.add_entry_comment(id_of_last_post,respond)

        tekst="Jestem bote, i nie bede tagowal bo zaraz nocna a @wytrzzeszcz sie denerwuje, w koncu on mnie pisze, jesli dobrze mnie zaprogramuje powinienem co 5 minut wrzucac ten wpis i wolac plusujacych porzedni do tego co zaplusowali, dzieluje za plusy one pomagaja wytrzowi pisac,elo z farszem"    
        id_of_last_post=api.add_entry(body=tekst)["id"] # emged=
    except:
            print "Sky is a limit, but API has limit too2"
            print sys.exc_info()[0]
            time.sleep(210) 		
    time.sleep(5*60);

