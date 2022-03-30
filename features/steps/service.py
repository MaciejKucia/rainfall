from behave import when, then, given


@given('application started')
def step_started(context):
    pass


@when('application started')
def step_when_started(context):
    pass


@when('/health endpoint is accessed')
def step_when_health(context):
    context.response = context.client.get('health')


@then('empty body response is returned')
def step_then_empty_body(context):
    assert context.response.text == ''


@then('HTTP code 200 is returned')
def step_impl(context):
    assert context.response.status_code == 200


@given('config file is read')
def step_conf_load(context):
    raise NotImplementedError(u'STEP: Given config file is read')


@then('configuration "{name}" is available for the application under "{value}"')
def step_conf(context):
    raise NotImplementedError(u'STEP: Then configuration "URL" is available '
                              u'for the application under "http://api.example"')
