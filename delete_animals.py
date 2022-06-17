from schema import Cat, Dog, Cow, Horse, Lion, Session, engine

local_session = Session(bind=engine)

cat_to_delete = local_session.query(Cat).filter(Cat.race=='kot sfinks').first()
local_session.delete(cat_to_delete)
local_session.commit()