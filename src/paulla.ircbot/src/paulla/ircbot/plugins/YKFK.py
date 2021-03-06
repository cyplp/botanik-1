from configparser import ConfigParser, ExtendedInterpolation
import irc3


parser = ConfigParser(interpolation=ExtendedInterpolation())
parser.read('ykfk.cfg')
masters = parser['config']['immunized'].splitlines()

@irc3.plugin
class Yakafokon:
    """ YKFK plugin """
    def __init__(self, bot):
        self.bot = bot
        self.log = self.bot.log

    @irc3.event(irc3.rfc.PRIVMSG)
    def ykfk(self, mask, event, target, data):
        if not mask.nick.startswith(masters):
            yakafokon = ['falloir', 'faudrait', 'faudra', 'faut', 
                         'faille', 'fallait', 'il fallût', 'fallu' ,
                         'faire']
            if [terme for terme in yakafokon if terme in data]:
                self.bot.privmsg(target, "¡¡¡ YAKAFOKON detected !!!")
