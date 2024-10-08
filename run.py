import os
from starwars_blog import create_app

app = create_app()

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", 5000)),
        debug=os.environ.get("DEBUG", "False")
    )