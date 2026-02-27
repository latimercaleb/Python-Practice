from alchemy import db, Raider, app

with app.app_context(): 
    # Makes all tables from model classes
    db.create_all() 

    # CRUD

    # C
    # gwil = Raider('Tank', 99)
    # lola = Raider('Bard', 82)

    # db.session.add(gwil)
    # db.session.add(lola)
    # db.session.add_all([gwil,lola]) # Example of adding all at once

    # db.session.commit() # Saves changes
    # print(gwil.id)
    # print(lola.job)

     # R
    all_raiders = Raider.query.all()
    print (all_raiders)

    first_raider = Raider.query.get(1) # Get by id
    print(first_raider)

    get_bard = Raider.query.filter_by(level=82) 
    print(get_bard) # Returns query, run query to get result
    print(get_bard.all()) # Returns query, run query to get result it will be a list without other filters added

    # U
    first_raider.job = "Samurai"
    first_raider.level = 22
    db.session.add(first_raider)

    second_raider = Raider.query.get(2)
    second_raider.job = "Red Mage"
    second_raider.level = 73
    db.session.add(second_raider)
    
    db.session.commit()

    # D
    db.session.delete(second_raider)
    db.session.commit()
