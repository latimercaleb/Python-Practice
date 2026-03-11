from alchemy import db, Raider, Master, Guild, app

with app.app_context():
    # 4 raiders
    # 1 master
    # 1 guild

# 1 Create members & Check
    # sam = Raider('Samurai', 'Sam', 84, 1)
    # bar = Raider('Bard', 'Bart', 19, 1)
    # mag = Raider('Mage', 'Mill', 142, 1)
    # pld = Raider('Paladin', 'Paz', 3, 1)

    # db.session.add_all([sam,bar,mag,pld])
    # db.session.commit()

    print(Raider.query.all())

    sam = Raider.query.filter_by(name = 'Sam').first()
    bar = Raider.query.get(2)
    mag = Raider.query.get(3)
    pld = Raider.query.get(4)
    print(sam)

# 2 Create Guild & Master, check representations
    sees = Guild('Sees', 4)
    sees.guild_member.add(element)
    print(sees)
    sees.show_member_names()


    # db.session.add_all([sam,bar,mag,pld])
    # db.session.commit()

# 3 Add master & members to guild

# 4 Check and retrieve details

# TODO Finish integrating each model and testing it to make sure it's correct
