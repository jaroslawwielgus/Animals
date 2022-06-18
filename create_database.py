from schema import engine, Base

'''
Creating database
'''
Base.metadata.create_all(engine)