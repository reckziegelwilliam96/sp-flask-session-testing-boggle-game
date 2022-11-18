from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information for home page is stored in session"""
        with self.client:
            response = self.client.get('/')
            self.assertIn('board', session)
            self.assertIsNone(session.get('highscore'))
            self.assertIsNone(session.get('plays'))
            self.assertIn(b'<p>High Score:', response.data)
            self.assertIn(b'Score:', response.data)

    def test_valid_word(self):
        """Check if board word is valid"""
        with self.client as client:
            with client.session_transaction() as session:
                sess['board'] = [["D", "O", "G", "G", "G"],
                                ["D", "O", "G", "G", "G"],
                                ["D", "O", "G", "G", "G"],
                                ["D", "O", "G", "G", "G"],
                                ["D", "O", "G", "G", "G"]]
        response = self.client.get('/check-word?word=dog')
        self.assertEqual(response.json['result'], 'ok')

    def not_on_board_word(self):
        self.client.get('/')
        response = self.client.get(
                '/check-word?word=asdfsadffij')
        self.assertEqual(response.json['result'], 'not-word')