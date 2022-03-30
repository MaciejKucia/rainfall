from rainfall.app import get_app

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


@given('"{config_path}" config file is read')
def step_conf_load(context, config_path):
    context.app = get_app(config_path)


@then('configuration "{name}" is available for the application under "{value}"')
def step_conf(context, name, value):
    print(context.app.config)
    assert context.app.config['RDC_' + name.upper()] == value
