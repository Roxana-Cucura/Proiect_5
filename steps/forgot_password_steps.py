from behave import *

# given, when, and, but then - sintaxa gerkin
# given - seteaza situatia initiala
# when - pasii din test
# then - verificare din test

'''
@given('forgot_password: I am a user on Jules forgot password page')
def step_impl(context):
    context.forgot_password_page.navigate_to_home_page()
'''


@when('forgot_password: I set my email "{email}"')
def step_impl(context, email):
    context.forgot_password_page.set_email(email)


@then('forgot_password: I verify email validation is correct')
def step_impl(context):
    context.forgot_password_page.verify_email_error_message()
