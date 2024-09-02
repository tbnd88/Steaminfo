from steam_web_api import Steam
import pprint

KEY = "1BB1E6D8F185ACA51D02BC262DF13C67"
steam = Steam(KEY)
x = 0
y = 0
z = 0
player_id = input("Please input Steamid or Steam Name\n")

if player_id.isdigit():
    player_id = player_id
else:
    player_info = steam.users.search_user(player_id)
    player_steam_id = player_info["player"]["steamid"]
    player_id = player_steam_id
print(player_id)
info_choice = input("What info whould you like about this person? \n 1. Vac Ban info \n 2. Friends List \n 3. List of games \n 4. List of recently played games \n 5. General info\n")


if info_choice == "1":
    print_bans = (steam.users.get_player_bans(player_id))
    while x < len(print_bans["players"]):
        if print_bans["players"][x]["VACBanned"] != None:
            print("VAC Banned")
            print(print_bans["players"][x]["VACBanned"])
        if print_bans["players"][x]["CommunityBanned"] != None:
            print("Community Banned")
            print(print_bans["players"][x]["CommunityBanned"])
        if print_bans["players"][x]["DaysSinceLastBan"] != None and print_bans["players"][x]["DaysSinceLastBan"] != 0:
            print("Days Since Last Ban")
            print(print_bans["players"][x]["DaysSinceLastBan"])
        x = x + 1
elif info_choice == "2":
    print_friends = steam.users.get_user_friends_list(player_id)
    while z < len(print_friends["friends"]):
        if print_friends["friends"][z].get("personaname") != None:
            print("Persona")
            print(print_friends["friends"][z]["personaname"])
        if print_friends["friends"][z].get("realname") != None:
            print("Name")
            print(print_friends["friends"][z]["realname"])
        if print_friends["friends"][z].get("friend_since") != None:
            print("Friends Since")
            print(print_friends["friends"][z]["friend_since"])
        if print_friends["friends"][z].get("loccountrycode") != None:
            print("Country")
            print(print_friends["friends"][z]["loccountrycode"])
        if print_friends["friends"][z].get("locstatecode") != None:
            print("State")
            print(print_friends["friends"][z]["locstatecode"])
        if print_friends["friends"][z].get("profileurl") != None:
            print("Profile")
            print(print_friends["friends"][z]["profileurl"])
        if print_friends["friends"][z].get("steamid") != None:
            print("Steam ID")
            print(print_friends["friends"][z]["steamid"])
        print("\n")
        z = z + 1
elif info_choice == "3":
    sorted_names = []
    print_games = steam.users.get_owned_games(player_id)
    while x < len(print_games["games"]):
        print_names = print_games["games"][x]["name"]
        sorted_names.append(print_games["games"][x]["name"])
        x = x+1
    sorted_names.sort()
    for b in sorted_names:
        print(b)

elif info_choice == "4":
    print_recent = steam.users.get_user_recently_played_games(player_id)
    while y < len(print_recent['games']):
        print(print_recent['games'][y]['name'])
        print("Last 2 weeks")
        print(print_recent['games'][y]['playtime_2weeks'])
        print("All Time")
        print(print_recent['games'][y]['playtime_forever'])
        print("\n")

        y = y + 1
elif info_choice == "5":
    print_info = steam.users.get_user_details(player_id)
    pprint.pprint(print_info["player"])

