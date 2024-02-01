travel_log = [
    {   
        "country": "france",
        "cities_visited" : ["berlin", "kakka", "denemark"],
        "the number of visits" : 5
    },
    {
        "country": "egypt",
        "cities_visited" : ["cairo", "geza", "alexandria"],
        "the number of visits" : 4 
    }

]

def add_new_country(count, nums, cites):
    empty_list = {}
    travel_log.append(empty_list)
    empty_list["country"] = count
    empty_list["cities_visited"] = cites
    empty_list["the number of visits"] = cites






add_new_country("russia" , 4, ["moscow", "alaska", "sandiego"])
print(travel_log)