# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def print_names():
	for key in targets.items():
		print(f"{key}")# 1) Write a function that uses a loop to print the name of each star.
def print_names(targets):
    for name in targets:
        print(name)
print(print_names(targets))
   
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def name_and_spectral(targets):
    for name, value in targets.items():
        print(f"{name}:{value['Spectral Type']}")
print(name_and_spectral(targets))


# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def star_magnitudes_greater_than_value(targets):
    result=[]
    for name, value in targets.items():
        magnitude=value.get("Magnitude")
        if magnitude > 0.1:
            result.append((name, magnitude))
    return result
print(star_magnitudes_greater_than_value(targets))

# 4) Look up another target, add all the necessary information to the targets list.
targets["Capella"]= {
    "RA": "05h 16m 41.4s",
    "Dec": "+45° 59′ 53″",
    "Magnitude":"0.08",
    "Spectral Type":"K0III"
}
print(targets)
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def brightest_near_20(targets):
    closest_star = None
    smallest_mag = float('inf')
    closest_diff = float('inf')

    for name, data in targets.items():
        dec_str = data["Dec"].replace("°", " ").replace("′", " ").replace("″", " ").replace("+", "").replace("−", "-")
        parts = dec_str.split()
        deg = float(parts[0])
        minutes = float(parts[1]) if len(parts) > 1 else 0
        seconds = float(parts[2]) if len(parts) > 2 else 0
        dec = deg + (minutes / 60) + (seconds / 3600)

        diff = abs(dec - 20)  
        if diff < closest_diff or (diff == closest_diff and data["Magnitude"] < smallest_mag):
            closest_diff = diff
            smallest_mag = data["Magnitude"]
            closest_star = name

    return closest_star

print(brightest_near_20(targets))
#I apologize, this is chatgpt code because I just had no idea how to do this one and it just left me stuck and unable to keep going forward

# 6) What is your favorite constellation?
# cygnus
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# 6) What is your favorite constellation?
