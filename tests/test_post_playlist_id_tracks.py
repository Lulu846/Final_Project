import unittest
from requests_folder.requests_file import post_play_list_id_tracks, get_play_list

class TestPutPlayList(unittest.TestCase):

    def test_post_play_list_id_tracks(self):
        response = post_play_list_id_tracks("2Di6xkTrVTOoy7dFSN9sJC", "spotify:track:37i9dQZF1DXbYM3nMM0oPk",0)
        assert response.status_code == 201, f'Error status code 201, but got {response.json()}'
        playlistIsAdded = True # aici facem initializarea variabilei
        if len(response.json()['snapshot_id']) < 56: # verificam daca raspunsul requestului este corect
              playlistIsAdded = False # linia asta se va executa DOAR DACA ceva nu a fost in regula cu raspunsul
        assert playlistIsAdded == True # aici verificam daca valoarea variabilei de evaluare a ramas true