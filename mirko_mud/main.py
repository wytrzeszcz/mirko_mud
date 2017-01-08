import wykop
import auth 
api=wykop.WykopAPI(auth.appkey,auth.secretkey)
api.authenticate(auth.login, auth.connection_key)
notyfication=api.get_notifications();
anserws={}
for call in notyfication:
	print "author"
	print call['author']
	print "URL"
	print call['url']
	print "id"
	print call['entry']['id']
	anserws[call['entry']['id']]+="Zawolales mnie @"
	anserws[call['entry']['id']]+=call['author']
	anserws[call['entry']['id']]+=" turaj to Ci odpowiadam, przeprasza jednoczesnie za spam\n"

for entry,anserw in anserws:
	print anserw
	print entry 
	


