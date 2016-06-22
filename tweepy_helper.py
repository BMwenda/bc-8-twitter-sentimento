import tweepy as twp
from time import sleep, strftime, time
import config

TIME = time()

class TwAPI:
    def __init__(self, mode):
        """
        :mode: either "user" or "app"
        :return: nothing
        """

        cons_key = "gPD2ZjrRaXY6OKSWiza5YQJOg"
        cons_sec = 'KaPXywbktbNeOzpegQzDHAQp2qnpicgcCLqnzw451BsxdmQGYx' # own key

        if mode == "user":
            accs_tok = '272311979-SWU6JF7TM62mGFn2ZC3xN8Fh6nQHB22cngAuMc1I' # own key
            accs_sec = 'A6gqoojWr8TYuJMXVDKxb892uM7HJeCoP8b4rkmTi3PZ0' # own key

            self.auth = twp.OAuthHandler(cons_key, cons_sec)
            self.auth.set_access_token(accs_tok, accs_sec)

        if mode == "app":
            self.auth = twp.AppAuthHandler(cons_key, cons_sec)

        self.mode = mode
        self.api = twp.API(self.auth)

    def get_friends(self, name):
        cursor = twp.Cursor(self.api.friends, id=name, count=200)
        l = list()
        for i in cursor.pages():
            for user in i:
                l.append(user.screen_name)
            return l

    def get_timeline(self, name):
        cursor = twp.Cursor(self.api.user_timeline, id=name, count=200)
        for i in cursor.pages():
            sleep(self.sleepy_time('timeline'))
            for tweet in i:
                yield tweet


    def sleepy_time(self, sw):
        """
        TODO: make the limit fetch itself given a target so we can get
            rid of the ugly if/elif statements that do the same. Can
            be fetched from self.api.rate_limit_status()['resources'].

        :sw: friends or messages
        :return: float cooldown seconds
        """
        global TIME
        t = strftime('%H:%M:%S')
        if sw == 'friends':
            lim = 0  # correct
        elif sw == 'messages':
            lim = 180 if self.mode == "user" else 60
        elif sw == 'timeline':
            lim = 180 if self.mode == "user" else 300
        else:
            lim = 15 if self.mode == "user" else 30

        process_time = time() - TIME
        TIME = time()
        cooldown = float(15 * 60) / float(lim) - process_time

        return cooldown if cooldown > 0 else 0

api = TwAPI("user")
print(api.get_friends("desterio"))
#api.get_timeline("_cmry")
