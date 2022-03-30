Feature: HTTP webservice

Scenario: expose /health endpoint
     When application started
     When /health endpoint is accessed
     Then empty body response is returned
     Then HTTP code 200 is returned

