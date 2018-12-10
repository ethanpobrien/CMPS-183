// This is the js for the default/index.html view.
const None = undefined; 

var enumerate = function(arr) {
    var k=0; return arr.map(function(e) {
        e._idx = k++;
    });
};

var processGames = function() {
    enumerate(app.games);
};

//var onPageLoad = function() {
    //$.getJSON(getGamesUrl,
        //function(response) {
            //app.movies = response.games;
            //processGames();
        //}
    //);
//};

var insertGame = function() {
    var newGame = {
        base_term: app.newBaseTerm,
        term1: app.newTerm1,
        term2: app.newTerm2
    };
    $.post(insertGameUrl, newGame, function(response) {
        newGame['id'] = response.new_game_id;
        app.games.push(newGame);
	showButton: true; 
	showForm: false;
        processGames();
        //this.$router.push('epobrien.pythonanywhere.com/trendify/default/index/')
        window.location.href = '/trendify/default/index';
    });
};

var app = new Vue({
    el: '#app',
    delimiters: ['${', '}'],
    unsafeDelimiters: ['!{', '}'],
    data: {
        newBaseTerm: "",
        newTerm1: "",
        newTerm2: "",
        games: [],
	showButton: true, 
        showForm: false,
    },
    methods: {
        insertGame: insertGame,
    }
});

//onPageLoad();
