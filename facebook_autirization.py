import pytest
from faker import Faker
import requests
from requests import HTTPError

fake = Faker()
FACEBOOK_URL = 'https://graph.facebook.com'
API_VERSION = 'v3.2'
USER_JSON = {'installed': False, 'permissions': 'email'}

"""
from: https://automated-testing.info/t/testirovanie-facebook-avtorizaczii-s-pomoshhyu-python/23699
Facebook
Один из вариантов sign up, sign in - flow для веб сайта есть через свой аккаунт в #Facebook.
Это достаточно простой вариант упростить себе авторизацию на любой сайт.

Проблема
Во время одной регрессии мы нашли баг, который заключался в невозможности использовать этот вариант авторизации. Что сильно нас огорчило.
Решением это проблемы было - сам фикс бага и написание автотестов, которые проверяли этот флоу.

Пример авторизации
Я решил поделиться своим решение, да оно не идеальное и можно было бы его легко отрефакторить, но оно рабочее и времени всегда не хватает на это. Так что пока как есть…
Для того что бы тестировать авторизацию - вам нужно иметь facebook client secret и facebook client_id - найти их вы можете в настройке своего приложения в facebook.
Найти все эти настройки можно через https://developers.facebook.com/ 7
"""


class FacebookAPI(object):
    """
    API to create a tests users for a sign up flow testing
    https://developers.facebook.com/docs/graph-api/reference/v3.2/app/accounts/test-users
    Example of usage
    facebook = FacebookAPI()
    new_user = facebook.create_new_facebook_user()
    delete_user = facebook.delete_existing_user(new_user['id'])
    """

    def __init__(self, environment,
                 facebook_staging_client_secret,
                 facebook_staging_client_id,
                 facebook_prod_client_secret,
                 facebook_prod_client_id):
        self.environment = environment
        self.user_json = USER_JSON
        self.get_facebook_staging_client_secret = facebook_staging_client_secret
        self.get_facebook_staging_client_id = facebook_staging_client_id
        self.get_facebook_prod_client_secret = facebook_prod_client_secret
        self.get_facebook_prod_client_id = facebook_prod_client_id


    def facebook_api_environment_config(self):
        return {
            'staging': {
                'client_secret': self.get_facebook_staging_client_secret,
                'client_id': self.get_facebook_staging_client_id
            },
            'prod': {
                'client_secret': self.get_facebook_prod_client_secret,
                'client_id': self.get_facebook_prod_client_id
            }
        }

    def _get_env_config(self):
        config = self.facebook_api_environment_config()[self.environment]
        if config is None:
            raise ValueError('Could not find a Facebook config for environment {}'.format(self.environment))
        return config

    def access_token_url(self):
        return \
            '{api_base}/oauth/access_token?' \
            'client_id={client_id}' \
            '&client_secret={client_secret}' \
            '&grant_type=client_credentials' \
                .format(
                api_base=FACEBOOK_URL,
                client_id=self._get_env_config()['client_id'],
                client_secret=self._get_env_config()['client_secret'])

    def _create_access_token(self):
        """
        Create a access token for facebook api
        :return: access_token
        """
        create_access_token_url = self.access_token_url()
        req = requests.post(create_access_token_url)
        return req.json()['access_token']

    def create_new_facebook_user(self):
        """
        Create new test user
        :return: new user id, email, password, login_url
        """
        req = requests.post(
            FACEBOOK_URL + '/{api_version}/{client_id}/accounts/test-users?access_token={access_token}'.format(
                api_version=API_VERSION,
                client_id=self._get_env_config()['client_id'],
                access_token=self._create_access_token()
            ),
            data=self.user_json
        )
        if req.ok is False:
            raise HTTPError(req.text, response=req.status_code)
        else:
            return req.json()

    def delete_existing_user(self, uid):
        """
        Delete existing test user after tests
        :param uid: user with uid will be deleted
        :return: status code of delete
        """
        req = requests.delete(
            FACEBOOK_URL + '/' + API_VERSION + '/{uid}?access_token={access_token}'.format(
                uid=uid,
                access_token=self._create_access_token()))
        return req.status_code