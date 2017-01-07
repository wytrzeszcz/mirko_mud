import hero
import 

class monster
	description="";
	polish_name="";	
#class monster end;

class skeleton monster

	description="Spotykasz na swojej drodze szkieleta,jego oczy szkrzą na zielono. Trzyma on w ręce długą kość udową"
	polish_name="Szkielet"
#class skeleton end;

class herd_of_rats monster 
	description="Wyszły zewsząd, są głodne, zapach ich mokrej sierści uderza twe nozdża. Pędzi na Ciebie lawina małych ciałek. Zostałeś zaatakowany przez szczury"
	polish_name="stado szczurów"

#class herd_of_rats end;

class werewolf monster
	#this monster has special rule, attacks as the first only males NIJ
	polish_name="wilkołak" # here is another place where i need to ask for sex of monster... 
#class werewolf end;

class basilisk monster 
	#instant kill if you have no mirror in hand
	polish_name="bazyliszek"
#class basilisk end;

class snakes monster 
	polish_name="węże"
#class snakes end;

class vampire monster
	#can attack mentally females
	polish_name="wąpież"
#class vampire end;

class demon monster
	polish_name="demon" 
#class demon end;

class jelly_cube monster 
	polish_name="Galaretowaty sześcian"
#class jelly_cube end;

class witch monster
	polish_name="czarownica"
#class witch end;

class nixie monster
	#when fight agnist male can seduce and kill during sex, 
	#so weak in normal fight
	polish_name="rusałka"
#class nixie end;

class nymphs monster 
	#work as nixie but strong in normal fight
	polish_name="Wiła"
#class nymphs end

class gargoyle monster
	# slow, weak but have great armor
	polish_name="gargulec"
#class gargoyle end;

class dragon monster
	# can attack with fire
	polish_name="smok"
#end class dragon

class spider monster
	polish_name="Pająk" # big one
#end class spider

class centaur monster
	#never atack first, females can run command "Baw sie" to this monster and in 10% chance they were killed in 10% will be ill but in 80% they lost only 2HP and get sperm centarua item. 
	polish_name="Centaur"
#end class monster
