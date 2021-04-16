"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    The version of the OpenAPI document: 1
    Generated by: https://openapi-generator.tech
"""

from dateutil.parser import parse as dateutil_parser
from urllib3_mock import Responses

from apivideo.api.players_api import PlayersApi  # noqa: E501
from apivideo.exceptions import ApiException, NotFoundException
from apivideo.model.metadata import Metadata
from apivideo.model.bad_request import BadRequest
from apivideo.model.not_found import NotFound
from apivideo.model.player import Player
from apivideo.model.player_creation_payload import PlayerCreationPayload
from apivideo.model.player_update_payload import PlayerUpdatePayload
from apivideo.model.players_list_response import PlayersListResponse

from helper import MainTest


responses = Responses()


class TestPlayersApi(MainTest):
    """PlayersApi unit test"""

    def setUp(self):
        super().setUp()
        self.api = PlayersApi(self.client)  # noqa: E501

    @responses.activate
    def test_delete(self):
        """Test case for delete

        Delete a player  # noqa: E501
        """
        pass

    @responses.activate
    def test_delete_logo(self):
        """Test case for delete_logo

        Delete logo  # noqa: E501
        """
        pass

    @responses.activate
    def test_list(self):
        """Test case for list

        List all players  # noqa: E501
        """
        for status, json in self.load_json('players', 'list'):
            responses.reset()

            kwargs = {
            }
            url = '/players'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.list(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.list(**kwargs)

    @responses.activate
    def test_get(self):
        """Test case for get

        Show a player  # noqa: E501
        """
        for status, json in self.load_json('players', 'get'):
            responses.reset()

            kwargs = {
                'player_id': "pl45d5vFFGrfdsdsd156dGhh",
            }
            url = '/players/{player_id}'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.get(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.get(**kwargs)

    @responses.activate
    def test_update(self):
        """Test case for update

        Update a player  # noqa: E501
        """
        for status, json in self.load_json('players', 'update'):
            responses.reset()

            kwargs = {
                'player_id': "pl45d5vFFGrfdsdsd156dGhh",
                'player_update_payload': PlayerUpdatePayload(),
            }
            url = '/players/{player_id}'.format(**kwargs)

            responses.add('PATCH', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.update(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.update(**kwargs)

    @responses.activate
    def test_create(self):
        """Test case for create

        Create a player  # noqa: E501
        """
        for status, json in self.load_json('players', 'create'):
            responses.reset()

            kwargs = {
                'player_creation_payload': PlayerCreationPayload(),
            }
            url = '/players'.format(**kwargs)

            responses.add('POST', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.create(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.create(**kwargs)

    @responses.activate
    def test_upload_logo(self):
        """Test case for upload_logo

        Upload a logo  # noqa: E501
        """
        pass

