import wykop
import auth 
api=wykop.WykopAPI(auth.appkey,auth.secretkey)
api.authenticate(auth.login, auth.connection_key)
notyfication=api.get_notifications();
anserws={}
for call in notyfication:
	if call['new'] :
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
	print key
	print anserws[key]
	api.add_entry_comment(key,anserws[key],"http://cdn.skim.gs/images/v1/msi/dc1h0q9jtxrqdqpwt6ai/tips-for-raising-a-healthy-and-happy-cat")

	


