import os
import pyautogui

src: str = "{}/src/idle_auto/data".format(os.getcwd())


char_btn_1 = "{}/lv_btn_1.png".format(src)
char_btn_2 = "{}/lv_btn_2.png".format(src)
char_btn_3 = "{}/lv_btn_3.png".format(src)
char_btn_4 = "{}/lv_btn_4.png".format(src)
bag: str = "{}/bag.png".format(src)
buy_10x: str = "{}/buy_10x.png".format(src)
city: str = "{}/city_btn.png".format(src)
city_selected: str = "{}/city_selected_btn.png".format(src)
city_maid: str = "{}/city_maid.png".format(src)
claim_all: str = "{}/claim_all.png".format(src)
initial_confirm: str = "{}/initial_confirm.png".format(src)
equip_popup: str = "{}/equip_popup.png".format(src)
fast_explore: str = "{}/fast_explore.png".format(src)
login_select: str = "{}/login_select.png".format(src)
login: str = "{}/start_char_selected.png".format(src)
logout: str = "{}/btn_logout.png".format(src)
confirm_logout: str = "{}/btn_logout_yes.png".format(src)
menu: str = "{}/menu_btn.png".format(src)
menu_element: str = "{}/menu_element.png".format(src)
pet_arena: str = "{}/pet_arena.png".format(src)
pvp_challenge: str = "{}/battle_btn_challenge.png".format(src)
pvp_enter: str = "{}/enter_pvp.png".format(src)
pvp: str = "{}/pvp_enter.png".format(src)
no_pvp: str = "{}/no_pvp.png".format(src)
start: str = "{}/start_btn.png".format(src)
empty_smelt: str = "{}/empty_gear.png".format(src)
smith: str = "{}/smith_btn.png".format(src)
smelt_start: str = "{}/smelt_start.png".format(src)
store: str = "{}/store_btn.png".format(src)
store_pet: str = "{}/store_pet_section.png".format(src)
store_pet_selected: str = "{}/store_pet_section_selected.png".format(src)
store_pet_daily_10: str = "{}/store_pet_section_daily_10.png".format(src)
store_pet_daily_free: str = "{}/store_pet_section_daily_free.png".format(src)
store_pet_confirm: str = "{}/store_pet_section_confirm.png".format(src)
pet: str = "{}/pet_btn.png".format(src)
pet_selected: str = "{}/pet_btn_selected.png".format(src)
pet_explore: str = "{}/pet_explore_btn.png".format(src)
pet_grimoire: str = "{}/pet_grimoire_btn.png".format(src)
pet_mvp_bigger_plus: str = "{}/bigger_plus_btn.png".format(src)
pet_mvp_plus: str = "{}/plus_btn.png".format(src)
pet_mvp_raid: str = "{}/pet_mvp_raid_btn.png".format(src)
pet_mvp_confirm: str = "{}/pet_mvp_confirm_btn.png".format(src)
friend: str = "{}/friend_btn.png".format(src)
friend_pat: str = "{}/friend_pat_btn.png".format(src)
friend_refuse_location: str = "{}/friend_refuse_location.png".format(src)
friend_send: str = "{}/friend_send_btn.png".format(src)
icy_rose: str = "{}/icy_rose_btn.png".format(src)
daily_sign_in: str = "{}/daily_sign_in.png".format(src)
daily_sign_in_btn: str = "{}/daily_sign_in_btn.png".format(src)
leave_daily_sign_in: str = "{}/leave_daily_sign_in.png".format(src)
daily_sign_in_confirm: str = "{}/confirm_daily_sign_in.png".format(src)
market: str = "{}/market.png".format(src)
market_buy_coin: str = "{}/market_money_buyable_btn.png".format(src)
market_refresh: str = "{}/market_refresh_btn.png".format(src)
market_sold_item: str = "{}/market_sold_item.png".format(src)

# Possible states

# Initial screen
s_login: int = 0x00

# Character selection screen
s_character_selection: int = 0x01

# Bag section
s_bag: int = 0x02

# Battle section
s_battle: int = 0x03

# City section (main menu)
s_city: int = 0x04

# Inside menu
s_in_menu: int = 0x05

# When a pop up to equip an item appears
s_in_popup_equip: int = 0x06

# Popup after a battle win
s_in_popup_battle: int = 0x07

# In main pet menu
s_pet: int = 0x08

# In pet explore menu
s_pet_explore: int = 0x09

# In pet claim all popup
s_pet_popup_claim_all = 0x0A

# Supposed initial state
state: int = s_login

pyautogui.PAUSE = 4.0
