import unittest

import requests


class Tester(unittest.TestCase):
    def test_ports(self):
        pass

    def test_backup(self):
        r = requests.get("http://" + "192.168.1.200" + "/owncloud")
        self.assertEqual(r.status_code, 200, msg="Backup is not working")

    def test_power(self):
        r = requests.get("http://" + "192.168.1.200" + "/powerControlget")
        self.assertIsInstance(r.json()['state'], int)

    def test_video(self):
        r = requests.get("http://" + "192.168.1.200" + "/videocam")
        self.assertEqual(r.status_code, 200)
        self.assertIsNot(r.content, b'', msg="Video is not working")

    def test_chat(self):
        r = requests.get("http://" + "192.168.1.200" + ":5222")
        self.assertEqual(r.status_code, 200)
