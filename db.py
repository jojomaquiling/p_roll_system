import sqlsoup
import clr

import System

Database = sqlsoup.SQLSoup("sqlite:///system.db")


class userinfo(System.Object):
    def __init__(self, username, firstname,lastname):
        self.Username = username
        self.Firsname = firstname
        self.Lastname = lastname

