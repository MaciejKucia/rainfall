Feature: Client for gov weather api

Scenario: Reading rainfall from the public webservice
  Given api client
   When requesting rainfall data for "Alexandra Road" at timestamp "2022-01-02T11:00:00"
   Then the response is "0.2"


Scenario: Displaying rainfall in CSV format
  Given api client
  Given data formatter in "CSV" format
   When requesting rainfall data for "Alexandra Road" at timestamp "2022-01-02T11:00:00"
   Then the response is "Alexandra Road, 11:00, 0.2mm, Raining"
