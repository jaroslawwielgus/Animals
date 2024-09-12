from schema import Cat, Dog, Cow, Horse, Lion, Canary, Session, engine

'''
Creating animals
'''
cats=[
    {
        "race":"kot sfinks",
        "color":"zróżnicowane",
        "height": 0.28,
        "weight": 4.5,
        "length_of_life": 13.5,
        "isWild": False,
        "isCatchingMouses": False
    },
    {
        "race":"kot bengalski",
        "color":"zróżnicowane",
        "height": 0.4,
        "weight": 7,
        "length_of_life": 12,
        "isWild": False,
        "isCatchingMouses": False
    },
    {
        "race":"kot perski",
        "color":"białe, rude, mieszane",
        "height": 0.32,
        "weight": 4.5,
        "length_of_life": 14,
        "isWild": False,
        "isCatchingMouses": True
    },
    {
        "race":"kot brytyjski",
        "color":"szare, cynamonowe, mieszane",
        "height": 0.33,
        "weight": 6,
        "length_of_life": 12,
        "isWild": False,
        "isCatchingMouses": False
    },
    {
        "race":"ryś",
        "color":"szare, rdzawe bądź żółtawe z czarnymi plamami",
        "height": 0.9,
        "weight": 24,
        "length_of_life": 14,
        "isWild": True,
        "isCatchingMouses": True
    }
]

dogs=[
    {
        "race":"beagle",
        "color":"biało-brązowo-czarne",
        "height": 0.37,
        "weight": 13,
        "length_of_life": 14,
        "isWild": False,
        "isRetrieving": True
    },
    {
        "race":"border collie",
        "color":"biało-czarne",
        "height": 0.52,
        "weight": 17,
        "length_of_life": 14,
        "isWild": False,
        "isRetrieving": False
    },
    {
        "race":"golden retriever",
        "color":"biało-beżowe lub ciemno-złote",
        "height": 0.58,
        "weight": 32,
        "length_of_life": 11,
        "isWild": False,
        "isRetrieving": True
    },
    {
        "race":"owczarek niemiecki",
        "color":"rudo-czarne",
        "height": 0.63,
        "weight": 35,
        "length_of_life": 11,
        "isWild": False,
        "isRetrieving": True
    },
    {
        "race":"yorkshire terier",
        "color":"zróżnicowane",
        "height": 0.19,
        "weight": 3,
        "length_of_life": 15,
        "isWild": False,
        "isRetrieving": True
    }
]

cows=[
    {
        "race":"holsztyno-fryzyjska",
        "color":"biało-czarne",
        "height": 1.4,
        "weight": 700,
        "length_of_life": 6,
        "isWild": False,
        "isGivingMilk": True,
        "isForMeat": False
    },
    {
        "race":"jersey",
        "color":"brązowo-białe",
        "height": 1.25,
        "weight": 420,
        "length_of_life": 6,
        "isWild": False,
        "isGivingMilk": True,
        "isForMeat": False
    },
    {
        "race":"duńska-czerwona",
        "color":"czerwone",
        "height": 1.34,
        "weight": 640,
        "length_of_life": 6,
        "isWild": False,
        "isGivingMilk": True,
        "isForMeat": False
    },
    {
        "race":"charolaise",
        "color":"białe",
        "height": 1.4,
        "weight": 800,
        "length_of_life": 6,
        "isWild": False,
        "isGivingMilk": False,
        "isForMeat": True
    },
    {
        "race":"limousine",
        "color":"jasnobrązowe",
        "height": 1.35,
        "weight": 730,
        "length_of_life": 6,
        "isWild": False,
        "isGivingMilk": False,
        "isForMeat": True
    }
]

horses=[
    {
        "race":"koń huculski",
        "color":"gniade",
        "height": 1.4,
        "weight": 400,
        "length_of_life": 35,
        "isWild": False,
        "isDraught": False,
        "isSports": False,
        "mane": "duża"
    },
    {
        "race":"koń małopolski",
        "color":"siwe, gniade",
        "height": 1.65,
        "weight": 540,
        "length_of_life": 30,
        "isWild": False,
        "isDraught": False,
        "isSports": False,
        "mane": "mała"
    },
    {
        "race":"koń oldenburski",
        "color":"skarogniade",
        "height": 1.7,
        "weight": 650,
        "length_of_life": 30,
        "isWild": False,
        "isDraught": False,
        "isSports": True,
        "mane": "mała"
    },
    {
        "race":"Holenderski koń gorącokrwisty",
        "color":"kasztanowate",
        "height": 1.7,
        "weight": 900,
        "length_of_life": 20,
        "isWild": False,
        "isDraught": False,
        "isSports": True,
        "mane": "mała"
    },
    {
        "race":"Shire",
        "color":"skarogniade",
        "height": 2,
        "weight": 1200,
        "length_of_life": 25,
        "isWild": False,
        "isDraught": True,
        "isSports": False,
        "mane": "duża"
    }
]

lions=[
    {
        "race":"lew azjatycki",
        "color":"jasnobrązowo - ciemne",
        "height": 1,
        "weight": 225,
        "length_of_life": 10,
        "isWild": True,
        "mane": "niewielka"
    },
    {
        "race":"lew wschodnioafrykański",
        "color":"jasnobrązowo - ciemne",
        "height": 1,
        "weight": 280,
        "length_of_life": 10,
        "isWild": True,
        "mane": "niewielka"
    }, 
    {
        "race":"lew berberyjski",
        "color":"jasnobrązowo - ciemne",
        "height": 2.8,
        "weight": 270,
        "length_of_life": 10,
        "isWild": True,
        "mane": "duża"
    },
    {
        "race":"lew angolski",
        "color":"jasnobrązowo - ciemne",
        "height": 1.2,
        "weight": 250,
        "length_of_life": 10,
        "isWild": True,
        "mane": "duża"
    }
]

canaries=[
    {
        "race":"lipochromowy czerwony",
        "color":"czerwony",
        "height": 0.13,
        "weight": 0.02,
        "length_of_life": 8,
        "isWild": False,
        "isHavingMane": False
    },
    {
        "race":"lipochromowy pomarańczowy",
        "color":"pomarańczowy",
        "height": 0.13,
        "weight": 0.02,
        "length_of_life": 9,
        "isWild": False,
        "isHavingMane": False
    }, 
    {
        "race":"lipochromowy żółty",
        "color":"żółty",
        "height": 0.13,
        "weight": 0.02,
        "length_of_life": 10,
        "isWild": False,
        "isHavingMane": False
    }
]

local_session = Session(bind=engine)

'''
Adding animals to database
'''
'''for c in cats:
    new_cat = Cat(race=c["race"], color=c["color"], height=c["height"], weight=c["weight"], 
        length_of_life=c["length_of_life"], isWild=c["isWild"], isCatchingMouses=c["isCatchingMouses"])
    local_session.add(new_cat)
    local_session.commit()
    print(f"Added {c}")'''

'''for d in dogs:
    new_dog = Dog(race=d["race"], color=d["color"], height=d["height"], weight=d["weight"], 
        length_of_life=d["length_of_life"], isWild=d["isWild"], isRetrieving=d["isRetrieving"])
    local_session.add(new_dog)
    local_session.commit()
    print(f"Added {d}")'''

'''for c in cows:
    new_cow = Cow(race=c["race"], color=c["color"], height=c["height"], weight=c["weight"], 
        length_of_life=c["length_of_life"], isWild=c["isWild"], isGivingMilk=c["isGivingMilk"], 
        isForMeat=c["isForMeat"])
    local_session.add(new_cow)
    local_session.commit()
    print(f"Added {c}")'''

'''for h in horses:
    new_horse = Horse(race=h["race"], color=h["color"], height=h["height"], weight=h["weight"], 
        length_of_life=h["length_of_life"], isWild=h["isWild"], isDraught=h["isDraught"], 
        isSports=h["isSports"], mane=h["mane"])
    local_session.add(new_horse)
    local_session.commit()
    print(f"Added {h}")'''

'''for l in lions:
    new_lion = Lion(race=l["race"], color=l["color"], height=l["height"], weight=l["weight"], 
        length_of_life=l["length_of_life"], isWild=l["isWild"], mane=l["mane"])
    local_session.add(new_lion)
    local_session.commit()
    print(f"Added {l}")'''

# for c in canaries:
#     new_canary = Canary(race=c["race"], color=c["color"], height=c["height"], weight=c["weight"], 
#         length_of_life=c["length_of_life"], isWild=c["isWild"], isHavingMane=c["isHavingMane"])
#     local_session.add(new_canary)
#     local_session.commit()
#     print(f"Added {c}")