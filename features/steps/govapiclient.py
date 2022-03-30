from behave import when, then, given


@when('requesting rainfall data for "{location}" at timestamp "{timedate}"')
def step_when_request(context, location, timedate):
    raise NotImplementedError(u'STEP: When requesting rainfall data '
                              u'for "Alexandra Road" at timestamp '
                              u'"2022-01-02T11:00:00"')


@then(u'the response is "{response}"')
def step_then_response(context, response):
    raise NotImplementedError(u'STEP: Then the response is "0.2"')


@given(u'data formatter in "CSV" format')
def step_given_formatter(context):
    raise NotImplementedError(u'STEP: Given data formatter in "CSV" format')
