Backend for the flutter app [Flutter App](https://github.com/TheNewReducers/flutter_app)
======
## Project for the [Google Challange](https://github.com/START-Hack/GOOGLE_STARTHACK23) of the [START](https://www.startglobal.org/) Hack 2023


### Techologies
- the backend in wiritten in python
- FastAPI Framework for the REST API
- OpenAI Chat API (gpt-3.5-turbo)
- Google Cloud Vision API

### Requirements
 Install the python requirements with:

```pip install -r requirements.txt```

- you need an API access to OpenAI
- you need access to the google cloud

### short technical explanation 
The frontend ([Flutter App](https://github.com/TheNewReducers/flutter_app)) sends us an image of the receipt. We send this image to the google cloud vision api and get back the text that is on the image. We send this text together with a predefined query to the OpenAI API (gpt-3.5-turbo model). We have designed the query so that we now get the relevant data of the receipt converted as JSON back (in controller.py is exact query).  Also GPT matches the items of the receipt to our existing in the database (e.g. Milka -> Chocolate). After that we match the results with our CO2 database and send this data back to the frontend.

