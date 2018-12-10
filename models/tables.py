import datetime

# each match has a base term, and the two terms paired with it.
def get_user_email():
    return None if auth.user is None else auth.user.email

db.define_table('game', 
		Field('user_email', default=get_user_email()), 
                Field('base_term', 'text'),
                Field('term1', 'text'),
                Field('term2', 'text'),
                Field('url', 'text'),
                )

db.game.url.writable = False
