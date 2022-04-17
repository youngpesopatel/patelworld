from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return '<html><h1>Welcome!</h1>Click <a href="/play">here</a> to play</h1></html>'

@app.route("/play")
@app.route("/play/")
def play():
    user = request.args.get('user') or 'Singleplayer'
    ver  = request.args.get('') or ''
    addr = request.args.get('ip')
    port = request.args.get('port') or '25565'

    if addr:
        args = "['%s', '%s', '%s', '%s']" % (user, ver, addr, port)
    else:
        args = "['%s']" % user
    return render_template('play.html', game_args=args)

if __name__ == "__main__":
    app.run()