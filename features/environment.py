from behave import fixture, use_fixture

from rainfall.app import get_app


@fixture
def rainfall_client(context, *args, **kwargs):
    app = get_app()
    app.testing = True
    app.config.update({
        "TESTING": True,
    })
    context.client = app.test_client()
    yield context.client

# The following ensures that each feature execution is executed
# on a fresh client instance


def before_feature(context, feature):
    use_fixture(rainfall_client, context)
