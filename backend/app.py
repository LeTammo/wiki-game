from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)
db_file = 'wikipedia_game.db'

def init_db():

@app.route('/start', methods=['GET'])
def start_game():
    
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
