
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
#def get_trend_term(request):
#'''
#def
#'''
#    if request.method=='POST':
#        form = MatchForm(request.POST)
#        print('request.POST: ', request.POST)
#        form.base_term = request.POST['base_term']
#        form.save()
#        print(request.POST)
#        if form.is_valid():
#            print('in form')
#            term1  = form.cleaned_data['term1']
#            term2  = form.cleaned_data['term2']
#            #base_term  = form.cleaned_data['base_term']
#
#            term_1_str = ""
#            term_1_str += base_term
#            term_1_str += " "
#            term_1_str += term1
#
#            term_2_str = ""
#            term_2_str += base_term
#            term_2_str += " "
#            term_2_str += term2
#
#            graph_title = ''
#            graph_title += term_1_str
#            graph_title += ' vs. '
#            graph_title += term_2_str
#
#
#            start = "2016-10-10"
#            end   = "2017-10-10"
#
#            screenshot_filename = ""
#            screenshot_filename += base_term
#            screenshot_filename +=term1
#            screenshot_filename += base_term
#            screenshot_filename +=term2
#
#
#            dates = []
#            trend_data = []
#            kw = []
#            kw.append(term_1_str)
#            kw.append(term_2_str)
#
#            #print('kw: ', kw)
#            results_df, dates = get_term(kw, start, end)
#
#            for data in results_df.itertuples():
#                trend_data.append(data[1])
#
#
#            fig = get_scatter(results_df, title=graph_title)
#            max1 = max(results_df[term_1_str])
#            max2 = max(results_df[term_2_str])
#            #form.full_clean()
#            #form.score1 = max1
#            #form.score2 = max2
#            #form.save()
#            match = form.save(commit=False)
#            match.name = graph_title
#            match.score1 = max1
#            match.score2 = max2
#            match.save()
#            print(match)
#
#            #print('debug for: results_df[term_1_str]')
#            #print('results_df[term_1_str].index: ')
#            #print(results_df[term_1_str].index)
#
#            #print('for item in results_df[term_1_str].to_dict(): ')
#            results1_dict = results_df[term_1_str].to_dict()
#            for item in results1_dict:
#                if results1_dict[item] == max1:
#                    max1date = item
#
#            results2_dict = results_df[term_2_str].to_dict()
#            for item in results2_dict:
#                if results2_dict[item] == max2:
#                    max2date = item
#
#            #offline.init_notebook_mode()
#
#            image_filename = 'trends/images/{}'.format(base_term)
#            image_filename_str = 'trends/images/{}.png'.format(screenshot_filename)
#            #print(fig)
#            #print(graph_title)
#            #print(results_df)
#
#            #offline.plot({'data': fig},image='svg', image_filename=str(image_filename), filename='temp-plot.html', auto_open=False)
#            offline.plot({'data': fig},image='png', auto_open=False, image_width=700, image_height=500, image_filename='/Users/ethanobrien/Documents/dev/python/google_trends/trend_website/mysite/trends/static/trends/images/{}'.format(screenshot_filename))
#            chrome_options = Options()
#            chrome_options.add_argument("--headless")
#            chrome_options.add_argument("--window-size=700x500")
#
#            chrome_driver = os.getcwd() +"/chromedriver"
#
#
#            driver = webdriver.Chrome('/Users/ethanobrien/Documents/dev/python/google_trends/trend_website/mysite/trends/chromedriver')
#            driver.set_window_size(700, 500)
#            url = 'file:///Users/ethanobrien/Documents/dev/python/google_trends/trend_website/mysite/temp-plot.html'
#            driver.get(url=url)
#            driver.get_screenshot_as_file('/Users/ethanobrien/Documents/dev/python/google_trends/trend_website/mysite/trends/static/trends/images/{}.png'.format(screenshot_filename))
#            driver.quit()
#
#            match_bool = True
#            return render(request, 'trends/match.html', {
#                'date_list' : dates,
#                'graph' : image_filename_str,
#                'term1': term_1_str,
#                'term2': term_2_str,
#                'base_term': base_term,
#                'max1' : max1,
#                'max2' : max2,
#                #'score1' : Match.score1,
#                #'score2' : Match.score2,
#                'max1date' : max1date,
#                'max2date' : max2date,
#                'match_bool':match_bool,
#                })
#        else:
#            print('in else')
#            form = MatchForm()
#            base_term = request.POST['base_term']
#            return render(request, 'trends/match.html', {'form': form, 'base_term':base_term, 'match_bool':match_bool})
#
#    return render(request, 'trends/match.html', {'form': form, })
