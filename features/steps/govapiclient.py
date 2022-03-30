from datetime import datetime

from behave import when, then, given

from rainfall.govapi import GovApiClient, FormatterCSV


@given(u'api client')
def step_client(context):
    context.client = GovApiClient()


@given(u'data formatter in "CSV" format')
def step_given_formatter(context):
    context.client.set_formatter(FormatterCSV)


@when('requesting rainfall data for "{location}" at timestamp "{timedate}"')
def step_when_request(context, location, timedate):
    timedate = datetime.strptime(timedate, '%Y-%m-%dT%H:%M:%S')
    context.response = context.client.get(location, timedate)


@then(u'the response is "{response}"')
def step_then_response(context, response):
    assert context.response == response
