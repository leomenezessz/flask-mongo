from app import app

app.config.from_object("config.Production")

if __name__ == "__main__":
    app.run()
