import unittest

from requests_folder.requests_file import get_play_list, post_create_playlist, delete_playlist


class TestPostCreatePlayList(unittest.TestCase):


    def test_create_playlist(self):
        playlist_id = post_create_playlist("31blt7yquqmibecnjbknv5uk5rba", "playlist_test_api_1", "new playlist 1", True)
        response = playlist_id
        assert response.status_code == 201, f'Error status code 201, but got {response.json()}'
        assert get_play_list(playlist_id).json()["name"] == "playlist_test_api_1"
        assert get_play_list(playlist_id).json()["description"] == "new playlist 1"
        assert get_play_list(playlist_id).json()["public"] == True

        for i in range(len(playlist_id)):
            if playlist_id[i]["name"] == True:
                delete_playlist("name", "31blt7yquqmibecnjbknv5uk5rba")



