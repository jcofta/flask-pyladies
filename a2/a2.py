from flask import render_template
from flask import Flask

movies_list = [
{
'id': 1,
'title': '12 Angry Men',
'type': 'drama',
'year_created': 1957,
'direction': 'Sidney Lumet',
'ratings': [
{
'username': 'jan_kowalski',
'rating': 9
},
{
'username': 'salvador_dali',
'rating': 6
}
],
'comments': [
{
'username': 'Jack Warden',
'content': 'Amazing!'
}
]
},
{
'id': 2,
'title': '2001: A Space Odyssey',
'type': 'Sci-Fi',
'year_created': 1968,
'direction': 'Stanley Kubrick',
'ratings': [
{
'username': 'william_sylvester',
'rating': 7
},
{
'username': 'claude_monet',
'rating': 6
},
{
}
],
'comments': [
{
'username': 'william_sylvester',
'content': 'Strange'
},
{
'username': 'margaret_tyzack',
'content': 'music is so nice'
}
]
},
{
'id': 3,
'title': 'The Blues Brothers',
'type': 'Musical',
'year_created': 1980,
'direction': 'John Landis',
'ratings': [
{
'username': 'pablo_picasso',
'rating': 8
},
{
'username': 'ray_charles',
'rating': 1
}
],
'comments': [
{
'username': 'ray_charles',
'content': "I don't like it"
}
]
},
{
'id': 4,
'title': 'The Remains of the Day',
'type': 'drama',
'year_created': 1993,
'direction': 'James Ivory',
'ratings': [],
'comments': [
{
'username': 'Michael Lonsdale',
'content': 'So sad'
}
]
},
{
'id': 5,
'title': 'Citizen Kane',
'type': 'drama',
'year_created': 1957,
'direction': 'Orson Welles',
'ratings': [
{
'username': 'orson_welles',
'rating': 10
}
],
'comments': [
{
'username': 'orson_welles',
'content': "Damn, I'm good"
},
{
'username': 'edward_wood',
'content': "Best movie of all time"
}
]
},
{
'id': 6,
'title': 'Vincent',
'type': 'short',
'year_created': 1982,
'direction': 'Tim Burton',
'ratings': [],
'comments': []
}
]

app = Flask(__name__)


@app.route("/")
def index():
	return render_template('index.html', movies_list=movies_list)

@app.route("/movie/<id>")
def movie(id):
	movie_detail = None
	for movie in movies_list:
		try:
			if movie['id'] == int(id):
				movie_detail = movie
				return render_template('movie.html', movie=movie_detail)
		except:
			return render_template('movie.html', movie=None)	
	return render_template('movie.html', movie=movie_detail)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, port=5000)