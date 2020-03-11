from eal_manager import create_app

## this allows us to run the app in debug by referencing
## ./eal-manager/__init__.py

app = create_app()



if __name__ == '__main__':
    app.run(host='0.0.0.0')
