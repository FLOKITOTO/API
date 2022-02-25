The project is realized in python with flask and a MongoDB database

Its just a simple API that is scrap data from Python documentation website.

Minimum required is to using MongoDb compass. 

Don't forget to set the name Database and name collection in your postman requests.

By default I put my database : local & my collection : mozilla

[MongoDB_API]

- read
- write
- update
- delete


[REQUESTS]

- GET 
- POST
- PUT
- DELETE


[SYNTAX] 
**Insert to postman body**

[GET]

```json
{
    "database": "local",
    "collection": "mozilla",
    "Document": {}
}
```

[POST]

```json
{
    "database": "local",
    "collection": "mozilla",
    "Document": {
        "Program Name": {
            "0": "Python",
            "1": "Pascal",
            "2": "Lisp",
            "3": "D#",
            "4": "Cobol",
            "5": "Fortran",
            "6": "Haskell"
        },
        "Internet Points": {
            "0": 932914021,
            "1": 532,
            "2": 1522,
            "3": 12,
            "4": 3,
            "5": 52124,
            "6": 24
        },
        "Kittens?": {
            "0": "Definitely",
            "1": "Unlikely",
            "2": "Uncertain",
            "3": "Possibly",
            "4": "No.",
            "5": "Yes.",
            "6": "lol."
        }
    }
}
```

[PUT]

```json
{
    "database": "local",
    "collection": "mozilla",
    "Filter": {
        "Program Name": {
                "0": "Python",
                "1": "Pascal",
                "2": "Lisp",
                "3": "D#",
                "4": "Cobol",
                "5": "Fortran",
                "6": "Haskell"
            }
    },
    "DataToBeUpdated": {
            "Internet Points": {
                "PPIERRRE": 6666666,
                "1": 532,
                "2": 1522,
                "3": 12,
                "4": 3,
                "5": 52124,
                "6": 24
            }
    }
}
```

[DELETE]

```json
{
    "database": "local",
    "collection": "mozilla",
    "Filter": {
     "Program Name": {
        "0": "Python",
        "1": "Pascal",
        "2": "Lisp",
        "3": "D#",
        "4": "Cobol",
        "5": "Fortran",
        "6": "Haskell"
        }
    }
}
```

[TAG]

MongoDB
Flask
Python
CRUD

Put data to DATABASE WITH API
API 
INSERT DATA WITH API TO database
Insert data with api to database MongoDB
Simple scraper API 
scraper API to MongoDB
MongoDB
