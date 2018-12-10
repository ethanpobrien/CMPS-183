import datetime

# each match has a base term, and the two terms paired with it.
db.define_table('game', 
                Field('base_term', 'text'),
                Field('term1', 'text'),
                Field('term2', 'text'),
                Field('url', 'text'),
                )

db.game.url.writable = False
