from __init__ import *
import time
from battle import Battle
from market_buy import MarketBuy
from log_out import LogOut
from open_menu import OpenMenu
from daily_mvp_frags import DailyMvpFrags
from send_gift import SendGift
from daily_sign_in import DailySignIn
from login import Login
from store_sections import StoreSections
from pet_daily import PetDaily
from friend_pat import FriendPat
from smelt_items import SmeltItems
from send_present_menu import SendPresentMenu
from smelt_items import SmeltItems
from in_city_enter import InCityEnter
from enter_in import EnterIn
from initial_confirm import InitialConfirm

def battleRoutine(char):
    while True:
        city_enter = EnterIn(EnterIn.CITY)
        city_enter.execute()

        pvp_enter = InCityEnter(InCityEnter.BATTLE)
        pvp_enter.execute()

        battle = Battle()
        try:
            result = battle.execute()
            if (result == 1):
                break
        except Exception:
            open_menu = OpenMenu()
            open_menu.execute()

            logout = LogOut()
            logout.execute()
            login = Login(char)
            login.execute()

            initial_conf = InitialConfirm()
            initial_conf.execute()
        time.sleep(35)
        
def smeltRoutine():
    city_enter = EnterIn(EnterIn.CITY)
    city_enter.execute()

    smelt_enter = InCityEnter(InCityEnter.SMELT)
    smelt_enter.execute()

    smelt = SmeltItems()
    smelt.execute()

def patFriends():
    city_enter = EnterIn(EnterIn.CITY)
    city_enter.execute()

    friend_enter = InCityEnter(InCityEnter.FRIEND)
    friend_enter.execute()

    friend_pat = FriendPat()
    friend_pat.execute()

def giftPresent():
    city_enter = EnterIn(EnterIn.CITY)
    city_enter.execute()

    friend_enter = InCityEnter(InCityEnter.FRIEND)
    friend_enter.execute()

    send_present_menu = SendPresentMenu()
    send_present_menu.execute()

    send_present = SendGift(SendGift.ICY_ROSE)
    send_present.execute()

def login(char):
    login = Login(char)
    login.execute()

    initial_conf = InitialConfirm()
    initial_conf.execute()

def logout():
    open_menu = OpenMenu()
    open_menu.execute()

    logout = LogOut()
    logout.execute()

def dailySignIn():
    city_enter = EnterIn(EnterIn.CITY)
    city_enter.execute()

    daily_sign_in = DailySignIn()
    daily_sign_in.execute()

def storeDailyPet():
    city_enter = EnterIn(EnterIn.CITY)
    city_enter.execute()

    store = InCityEnter(InCityEnter.STORE)
    store.execute()

    store_section = StoreSections(StoreSections.SECTION_PET)
    store_section.execute()

    daily_pet = PetDaily()
    daily_pet.execute()

def dailyMvpPet():
    pet_enter = EnterIn(EnterIn.PET)
    pet_enter.execute()

    daily_mvp = DailyMvpFrags()
    daily_mvp.execute()

def marketBuy(until = 17):
    city_enter = EnterIn(EnterIn.CITY)
    city_enter.execute()

    market_enter = InCityEnter(InCityEnter.MARKET)
    market_enter.execute()

    market_buy = MarketBuy(until)
    market_buy.execute()



for i in range(1, 5):
    login(i)
    dailyMvpPet()
    battleRoutine(i)
    patFriends()
    giftPresent()
    dailySignIn()
    smeltRoutine()
    storeDailyPet()
    marketBuy()
    smeltRoutine()
    logout()
