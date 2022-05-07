from asyncio import FastChildWatcher
from portfolio import app



if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

#__name__ == "__main__" # This is for deployment