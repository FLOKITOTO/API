from unittest import TestCase
import unittest
import requests
from MongoDB_API import *
import json

class TestAPI(TestCase):
    def setUp(self):
        self.structures = {
            "requests": {
                "GET": {
                    "database": "local",
                    "collection": "mozilla",
                    "Document": {}
                },
                "POST": {
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
                    },
                },
                "PUT": {
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
                            },
                    },
                    "DataToBeUpdated": {
                         "Internet Points": {
                                "PIERRE GARCIA": 6666666,
                                "1": 532,
                                "2": 1522,
                                "3": 12,
                                "4": 3,
                                "5": 52124,
                                "6": 24
                            },
                    }
                },
                "DELETE": {
                    "database": "local",
                    "collection": "mozilla",
                    "Filter": {

                    }
    
                }
            }, 
            "responses": {
                "GET": [
                    {
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
                ],
                "POST": {
                    "Document_ID": "dddd",
                    "Status": "Successfully Inserted"
                },      
                "PUT": {
                    "Status": "Successfully Updated"
                },
                "DELETE": {
                    "Status": "Successfully Deleted"
                }
            }
        }

    API_url = "http://localhost:5001/mongodb"

    def test_post_data(self):
        print(self.structures["requests"]["POST"])
        r = requests.post(url=self.API_url, json=self.structures["requests"]["POST"])
        self.assertEqual(r.status_code, 200)

    def test_get_data(self):
        r = requests.get(url=self.API_url, json=self.structures["requests"]["GET"])
        self.assertEqual(r.status_code, 200)
        self.assertTrue(self.structures["responses"]["GET"] == r.json())

    def test_put_data(self):
        r = requests.put(url=self.API_url, json=self.structures["requests"]["PUT"])
        self.assertEqual(r.status_code, 200)
        self.assertTrue(self.structures["responses"]["PUT"] == r.json())

    def test_delete_data(self):
        r = requests.delete(url=self.API_url, json=self.structures["requests"]["DELETE"])
        self.assertEqual(r.status_code, 200)
        self.assertTrue(self.structures["responses"]["DELETE"] == r.json())





if __name__ == "__main__":
    unittest.main()

