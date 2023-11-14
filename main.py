from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    players = {
        'Kelly Oubre Jr': {
            'name': "Kelly Oubre Jr",
            'points': 32,
            'rebounds': 14,
            'assists': 17,
            'steals': 6,
            'blocks': 8
        },
        'Lebron James': {
            'name': "Lebron James",
            'points': 37,
            'rebounds': 19,
            'assists': 11,
            'steals': 5,
            'blocks': 9
        },
        'Michael Jordan': {
            'name': "Michael Jordan",
            'points': 3,
            'rebounds': 1,
            'assists': 2,
            'steals': 0.2,
            'blocks': 0
        },
        'Lonzo Ball': {
            'name': "Lonzo Ball",
            'points': 42,
            'rebounds': 16,
            'assists': 27,
            'steals': 12,
            'blocks': 7
        },
    }
    total_points = players["Kelly Oubre Jr"]["points"]+players["Lebron James"]["points"]+players["Michael Jordan"]["points"]+players["Lonzo Ball"]["points"]
    total_rebounds = players["Kelly Oubre Jr"]["rebounds"] + players["Lebron James"]["rebounds"] + players["Michael Jordan"]["rebounds"] +players["Lonzo Ball"]["rebounds"]
    scoreboard = {
        'total_points': total_points,
        'total_rebounds': total_rebounds,
        'total_totals': total_points+total_rebounds
    }
    return render_template('index.html', players=players, scoreboard=scoreboard)


if __name__ == '__main__':
    app.run(debug=True)
