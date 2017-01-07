import hero


class Monster():
    def __index__(self):
        pass
    description = ""
    polish_name = ""


# noinspection PyPep8Naming
class Skeleton(Monster):
    description = "Spotykasz na swojej drodze szkieleta, jego oczy szkrzą na zielono. " \
                  "Trzyma on w ręce długą kość udową"
    polish_name = "Szkielet"


class HerdOfRats(Monster):
    description = "Wyszły zewsząd, są głodne, zapach ich mokrej sierści uderza twe nozdża. " \
                  "Pędzi na Ciebie lawina małych ciałek. Zostałeś zaatakowany przez szczury"
    polish_name = "stado szczurów"


class Werewolf(Monster):
    # this monster has special rule, attacks as the first only males NIJ
    polish_name = "wilkołak"  # here is another place where i need to ask for sex of monster...


class Basilisk(Monster):
    # instant kill if you have no mirror in hand
    polish_name = "bazyliszek"


class Snakes(Monster):
    polish_name = "węże"


class Vampire(Monster):
    # can attack mentally females
    polish_name = "wąpież"


class Demon(Monster):
    polish_name = "demon"


class JellyCube(Monster):
    polish_name = "Galaretowaty sześcian"


class Witch(Monster):
    polish_name = "czarownica"


class Nixie(Monster):
    # when fight agnist male can seduce and kill during sex,
    # so weak in normal fight
    polish_name = "rusałka"


class Nymphs(Monster):
    # work as nixie but strong in normal fight
    polish_name = "Wiła"


class Gargoyle(Monster):
    # slow, weak but have great armor
    polish_name = "gargulec"


class Dragon(Monster):
    # can attack with fire
    polish_name = "smok"


class Spider(Monster):
    polish_name = "Pająk"  # big one


class Centaur(Monster):
    # Centaur never attacks first, females can run command "Baw sie" to this monster and in 10% chance they were killed in 10% will be ill but in 80% they lost only 2HP and get sperm centarua item.
    polish_name = "Centaur"
