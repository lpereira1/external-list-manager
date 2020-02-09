from eal_manager import app

## this allows us to run the app in debug by referencing
## ./eal-manager/__init__.py

if __name__ == '__main__':
    app.run(debug=True)
