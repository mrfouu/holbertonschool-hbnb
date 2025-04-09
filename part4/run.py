from app import create_app

app = create_app()
app.url_map.strict_slashes = False

if __name__ == '__main__':
    app.run(debug=False)
