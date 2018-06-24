from unittest import TestCase
from mock import patch
from flask import jsonify
import restGet
import unittest


def mock_getJSON():
# mock sum function without the long running time.sleep
    json={
        "Team": {
            "Rome": {
                "Stone Skating": {
                    "Score": "20"
                    }, 
                     "Gold": 1542, 
                     "Stone Throwing": {
                         "Score": "200"
                         }, 
                     "Stone Curling": {
                         "Score": "82"
                         }, 
                     "Silver": 8, 
                     "Bronze": 7
                     }, 
            "Gual": {
                "Stone Skating": {
                    "Score": "10"
                    }, 
                     "Gold": 1547, 
                     "Stone Throwing": {
                         "Score": "100"
                         }, 
                     "Stone Curling": {
                         "Score": "52"
                         }, 
                     "Silver": 2, 
                     "Bronze": 8
                     }
                 }
          }
    
    return json 

def mock_jsonify(val1):
# mock sum function without the long running time.sleep
    json={
        "Team": {
            "Rome": {
                "Stone Skating": {
                    "Score": "20"
                    }, 
                     "Gold": 1542, 
                     "Stone Throwing": {
                         "Score": "200"
                         }, 
                     "Stone Curling": {
                         "Score": "82"
                         }, 
                     "Silver": 8, 
                     "Bronze": 7
                     }, 
            "Gual": {
                "Stone Skating": {
                    "Score": "10"
                    }, 
                     "Gold": 1547, 
                     "Stone Throwing": {
                         "Score": "100"
                         }, 
                     "Stone Curling": {
                         "Score": "52"
                         }, 
                     "Silver": 2, 
                     "Bronze": 8
                     }
                 }
          }
    
    return json 

def mock_dumpJSON():
    return

class TestMethods(TestCase):

    @patch('restGet.getJSON', side_effect=mock_getJSON)
    def test_getJSON(self,val):    
        self.assertTrue(restGet.getJSON())
    
    @patch('restGet.getJSON', side_effect=mock_getJSON)
    @patch('restGet.makeJSON',side_effect=mock_jsonify)  
    def test_getteam(self,teamname,val):
         
        self.assertTrue(restGet.getteam('Rome')) 
 
    @patch('restGet.getJSON', side_effect=mock_getJSON)
    @patch('restGet.makeJSON',side_effect=mock_jsonify)  
    def test_getMedalTallyall(self,val1,val2):
         
        self.assertTrue(restGet.getMedalTallyall()) 
        
    @patch('restGet.getJSON', side_effect=mock_getJSON)
    @patch('restGet.makeJSON',side_effect=mock_jsonify)  
    def test_getscore(self,eventType,val1):
         
        self.assertTrue(restGet.getscore(eventType)) 
        
    @patch('restGet.getJSON', side_effect=mock_getJSON)
    @patch('restGet.makeJSON',side_effect=mock_jsonify)
    @patch('restGet.dumpJSON',side_effect=mock_dumpJSON)  
    def test_setscore(self,eventType,rome_score,gaul_score,auth_id):
         
        self.assertTrue(restGet.setscore(eventType,rome_score,gaul_score,auth_id)) 
        
    @patch('restGet.getJSON', side_effect=mock_getJSON)
    @patch('restGet.makeJSON',side_effect=mock_jsonify)
    @patch('restGet.dumpJSON',side_effect=mock_dumpJSON)  
    def test_updateEmpattr(self,teamName,medalType,auth_id):
         
        self.assertTrue(restGet.updateEmpattr(teamName,medalType,auth_id)) 