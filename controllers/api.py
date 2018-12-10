
#https://trends.google.com/trends/explore?geo=US&q=best%20sock,worst%20sock
def get_match_results():
    return_url = 'https://trends.google.com/trends/explore?geo=US&q={t1}%20{bt},{t2}%20{bt}'.format(t1=request.vars.term1,t2=request.vars.term2,bt=request.vars.base_term)
    print('return_url: ', return_url)

    match_id = db.match.insert(
            base_term=request.vars.base_term,
            term1=request.vars.term1,
            term2=request.vars.term2,
            url=return_url,
            )
    return response.json(dict(match_id=match_id))

def get_match():
    match = db(db.match.match_id == request.vars.id).select()
    return response.json(dict(match=match))

def insert_game():
    new_game_id = db.game.insert(
        base_term = request.vars.base_term,
        term1 = request.vars.term1, 
        term2 = request.vars.term2
    )
    return response.json(dict(new_game_id=new_game_id))

def get_all_games():
    games = db(db.game).select() # this asks the database for all entries in the movies table

    game_list = []

    for game in games:
        game_to_send = dict(
            id=game.id,
            base_term=game.base_term,
            term1=game.term1,
            term2=game.term2
        )

        game_list.append(game_to_send)

    return response.json(dict(games=game_list)) # return all movies as a JSON object back to JavaScript

def clear_games():
    if auth.user is not None: 
        db(db.game.user_email == auth.user.email).delete()
        redirect(URL('default', 'index'))

def logged_in():
    if auth.user is not None:
        return true
    return false 
