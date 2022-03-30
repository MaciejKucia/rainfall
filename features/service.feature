Feature: HTTP webservice

Scenario: expose /health endpoint
     When application started
     When /health endpoint is accessed
     Then empty body response is returned
     Then HTTP code 200 is returned


Scenario Outline: read configuration file
     When application started
    Given "../features/example-config.yaml" config file is read
     Then configuration "<option>" is available for the application under "<name>"

     Examples:
       | option   | name               |
       | URL      | http://api.example |
       | Location | Place              |
       | LOCatiON | Place              |
