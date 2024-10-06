import random
import string

def generate_alien_name():
    vowels = 'aeiou'
    consonants = ''.join(set(string.ascii_lowercase) - set(vowels))
    
    name_length = random.randint(3, 8)
    name = ''
    
    for i in range(name_length):
        if i % 2 == 0:
            name += random.choice(consonants)
        else:
            name += random.choice(vowels)
    
    return name.capitalize()

def generate_alien_trait():
    traits = [
        "telepathic", "shape-shifting", "time-traveling", "energy-absorbing",
        "gravity-manipulating", "dimension-hopping", "mind-controlling",
        "light-bending", "sound-mimicking", "emotion-sensing"
    ]
    return random.choice(traits)

def generate_alien_planet():
    prefixes = ["Zor", "Xen", "Qua", "Neb", "Vort", "Kry", "Plu", "Gly", "Tril", "Ome"]
    suffixes = ["on", "ax", "oid", "ius", "ara", "ex", "ini", "ova", "ux", "eon"]
    return random.choice(prefixes) + random.choice(suffixes)

def alien_encyclopedia_entry():
    name = generate_alien_name()
    trait = generate_alien_trait()
    planet = generate_alien_planet()
    
    entry = f"""
    Species Name: {name}
    Notable Trait: {trait}
    Home Planet: {planet}
    
    The {name} species, hailing from the distant world of {planet}, 
    is renowned across the galaxy for their {trait} abilities. 
    These fascinating beings have developed a unique culture and advanced 
    technology based on their extraordinary capabilities.
    """
    
    return entry

if __name__ == "__main__":
    print("Welcome to the Galactic Alien Encyclopedia Generator!")
    print("Generating a random alien species entry...\n")
    print(alien_encyclopedia_entry())
    
    while True:
        generate_more = input("\nWould you like to generate another entry? (y/n): ").lower()
        if generate_more != 'y':
            print("Thank you for using the Galactic Alien Encyclopedia Generator. Goodbye!")
            break
        print("\n" + alien_encyclopedia_entry())
