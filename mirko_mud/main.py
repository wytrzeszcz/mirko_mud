import time
import wykop
import auth 
api=wykop.WykopAPI(auth.appkey,auth.secretkey)
api.authenticate(auth.login, auth.connection_key)

anserws={}
while True:
	notyfication=api.get_notifications();

	for call in notyfication:
		if call['new'] :
			if call['type'] in ["entry_comment_directed","entry_directed","entry_tag"]:
				print "author"
				print call['author']
				print "URL"
				print call['url']
				print "id"
				print call['entry']['id']
				print 
				if call['entry']['id'] not  in anserws.keys():
					anserws[call['entry']['id']]=""
				anserws[call['entry']['id']]+="Zawolales mnie @"
				anserws[call['entry']['id']]+=call['author']
				anserws[call['entry']['id']]+=" tutaj to Ci odpowiadam, przeprasza jednoczesnie za spam\n powinno to byc ostatnie\n"
			api.mark_as_read_notification(call['id'])


	for key in anserws.keys():
		try:
			print key
			print anserws[key]	
			api.add_entry_comment(key,anserws[key],"http://cdn.skim.gs/images/v1/msi/dc1h0q9jtxrqdqpwt6ai/tips-for-raising-a-healthy-and-happy-cat")
			anserws.pop(key,nil) # after ok anserw delete
		except:
			print "Sky is a limit, but API has limit too"
			time.sleep(120) 		


