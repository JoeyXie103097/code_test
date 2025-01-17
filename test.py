# test.py
# Author: Joey Xie
# Data: July 16th 2024

import unittest
from fastapi.testclient import TestClient
import websocket
import asyncio

from webapp.main import app
import quiz


class TestExample(unittest.TestCase):
    # test1: quiz -- reverse list -- four methods included
    def test_reverse_list_1(self):
        # define inputs:
        sample_list = [1, 2, 3, 4]
        expected_list = [4, 3, 2, 1]

        # run functions:
        revesed_list1 = quiz.reverse_list1(sample_list)
        revesed_list2 = quiz.reverse_list2(sample_list)
        revesed_list3 = quiz.reverse_list3(sample_list)

        # method 3 is inplace method, need to reset input
        sample_list = [1, 2, 3, 4]
        revesed_list4 = quiz.reverse_list4(sample_list)

        # check results:
        self.assertEqual(revesed_list1, expected_list)
        self.assertEqual(revesed_list2, expected_list)
        self.assertEqual(revesed_list3, expected_list)
        self.assertEqual(revesed_list4, expected_list)

    # test2: quiz -- reverse list -- four methods included
    def test_reverse_list_2(self):
        # define inputs:
        sample_list = [[1,2,3], 2, [3,"2"], "4"]
        expected_list = ["4", [3, "2"], 2, [1,2,3]]

        # run functions:
        revesed_list1 = quiz.reverse_list1(sample_list)
        revesed_list2 = quiz.reverse_list2(sample_list)
        revesed_list3 = quiz.reverse_list3(sample_list)

        # method 3 is inplace method, need to reset input
        sample_list = [[1,2,3], 2, [3,"2"], "4"]
        revesed_list4 = quiz.reverse_list4(sample_list)

        # check results:
        self.assertEqual(revesed_list1, expected_list)
        self.assertEqual(revesed_list2, expected_list)
        self.assertEqual(revesed_list3, expected_list)
        self.assertEqual(revesed_list4, expected_list)

    # test3: quiz -- solve sudoku - easy mode with correct answer: 30% blank, solvable
    def test_solve_sudoku(self):
        input_matrix = [
            [1, 0, 3, 4, 0, 2, 5, 9, 0],
            [4, 8, 0, 0, 5, 0, 2, 0, 6],
            [2, 0, 9, 3, 0, 0, 1, 0, 8],
            [6, 3, 1, 2, 4, 8, 7, 5, 9],
            [0, 7, 4, 9, 1, 5, 6, 0, 3],
            [5, 0, 2, 6, 0, 7, 8, 1, 4],
            [0, 1, 6, 0, 2, 4, 0, 7,0],
            [7, 0, 8, 0, 9, 0, 3, 6, 2],
            [9, 0, 0, 7, 6, 3, 0, 8, 0]
        ]

        expected_matrix = [
            [1, 6, 3, 4, 8, 2, 5, 9, 7],
            [4, 8, 7, 1, 5, 9, 2, 3, 6],
            [2, 5, 9, 3, 7, 6, 1, 4, 8],
            [6, 3, 1, 2, 4, 8, 7, 5, 9],
            [8, 7, 4, 9, 1, 5, 6, 2, 3],
            [5, 9, 2, 6, 3, 7, 8, 1, 4],
            [3, 1, 6, 8, 2, 4, 9, 7, 5],
            [7, 4, 8, 5, 9, 1, 3, 6, 2],
            [9, 2, 5, 7, 6, 3, 4, 8, 1]
        ]

        output_matrix = quiz.solve_sudoku(input_matrix)

        self.assertEqual(output_matrix, expected_matrix)

    # test4: quiz -- solve sudoku - hard mode with correct answer: 60% blank, solvable
    def test_solve_sudoku2(self):
        input_matrix = [
            [1, 0, 3, 4, 0, 2, 5, 9, 0],
            [4, 8, 0, 0, 5, 0, 2, 0, 6],
            [2, 0, 9, 3, 0, 0, 1, 0, 8],
            [6, 3, 1, 2, 4, 8, 7, 0, 9],
            [0, 0, 4, 9, 1, 5, 6, 0, 0],
            [5, 0, 2, 6, 0, 7, 8, 1, 0],
            [0, 1, 0, 0, 0, 4, 0, 7, 0],
            [7, 0, 8, 0, 0, 0, 3, 0, 2],
            [0, 0, 0, 7, 0, 3, 0, 0, 0]
        ]

        expected_matrix = [
            [1, 6, 3, 4, 8, 2, 5, 9, 7],
            [4, 8, 7, 1, 5, 9, 2, 3, 6],
            [2, 5, 9, 3, 7, 6, 1, 4, 8],
            [6, 3, 1, 2, 4, 8, 7, 5, 9],
            [8, 7, 4, 9, 1, 5, 6, 2, 3],
            [5, 9, 2, 6, 3, 7, 8, 1, 4],
            [3, 1, 6, 8, 2, 4, 9, 7, 5],
            [7, 4, 8, 5, 9, 1, 3, 6, 2],
            [9, 2, 5, 7, 6, 3, 4, 8, 1]
        ]

        output_matrix = quiz.solve_sudoku(input_matrix)
        self.assertEqual(output_matrix, expected_matrix)

    # test5: quiz -- solve sudoku - hard mode with correct answer: 60% blank, not valid; expect the output to be the same matrix as input;
    def test_solve_sudoku3(self):
        input_matrix = [
            [1, 0, 3, 4, 0, 2, 5, 9, 0  ],
            [4, 8, 0, 0, 5, 0, 2, 0, 6  ],
            [2, 0, 9, 3, 0, 0, 1, 0, 8  ],
            [6, 3, 1, 2, 4, 8, 7, 0, 9  ],
            [0, 0, 4, 9, 1, 5, 6, 0, 0  ],
            [5, 0, 2, 6, 0, 7, 8, 1, 0  ],
            [0, 1, 0, 0, 0, 4, 0, 7, 0  ],
            [7, 0, 8, 0, 0, 0, 3, 0, "2"],
            [0, 0, 0, 7, 0, 3, 0, 0, 0  ]
        ]

        expected_matrix = [
            [1, 0, 3, 4, 0, 2, 5, 9, 0  ],
            [4, 8, 0, 0, 5, 0, 2, 0, 6  ],
            [2, 0, 9, 3, 0, 0, 1, 0, 8  ],
            [6, 3, 1, 2, 4, 8, 7, 0, 9  ],
            [0, 0, 4, 9, 1, 5, 6, 0, 0  ],
            [5, 0, 2, 6, 0, 7, 8, 1, 0  ],
            [0, 1, 0, 0, 0, 4, 0, 7, 0  ],
            [7, 0, 8, 0, 0, 0, 3, 0, "2"],
            [0, 0, 0, 7, 0, 3, 0, 0, 0  ]
        ]

        output_matrix = quiz.solve_sudoku(input_matrix)
        self.assertEqual(output_matrix, expected_matrix)

    # webapp test1: test connecting websocket client to server, and after connected, username will be broadcast;
    def test_webapp1(self):
        client = TestClient(app)
        user1 = "Joey"
        user2 = "Sharon"
        message_list = []

        # user1 first entered the room, its username(Joey) is broadcasted to user1 only; when user2 entered the room, its username is broadcasted to user1 and user2;
        expect_message_list = [
            "Joey",
            "Sharon",
            "Sharon"
        ]
        
        with client.websocket_connect(f"/ws/{user1}") as user1_connection, client.websocket_connect(f"/ws/{user2}") as user2_connection:
            user1_enter_message_to_user1 = user1_connection.receive_text()
            user2_enter_message_to_user2 = user2_connection.receive_text()
            user2_enter_message_to_user1 = user1_connection.receive_text()
            message_list = [
                user1_enter_message_to_user1,
                user2_enter_message_to_user2,
                user2_enter_message_to_user1
            ]
            
        self.assertEqual(message_list, expect_message_list)

    # webapp test2: test connecting websocket client to server, and after connected, username will be broadcast, then user1 will be sending message and the message will be broadcasted to user1 and user2;
    def test_webapp2(self):
        client = TestClient(app)
        user1 = "Joey"
        user2 = "Sharon"
        user1_send_message = "Hello World!"
        message_list = []

        # user1 first entered the room, its username(Joey) is broadcasted to user1 only; when user2 entered the room, its username is broadcasted to user1 and user2;
        expect_message_list = [
            "Joey",
            "Sharon",
            "Sharon",
            "Joey: Hello World!",
            "Joey: Hello World!"
        ]
        
        with client.websocket_connect(f"/ws/{user1}") as user1_connection, client.websocket_connect(f"/ws/{user2}") as user2_connection:
            # greeting message when enter room:
            user1_enter_message_to_user1 = user1_connection.receive_text()
            user2_enter_message_to_user2 = user2_connection.receive_text()
            user2_enter_message_to_user1 = user1_connection.receive_text()

            # user1 send message and message will be broadcasted
            user1_connection.send_text(user1_send_message)
            user1_receive_message_from_user1 = user1_connection.receive_text()
            user2_receive_message_from_user1 = user2_connection.receive_text()

            message_list = [
                user1_enter_message_to_user1,
                user2_enter_message_to_user2,
                user2_enter_message_to_user1,
                user1_receive_message_from_user1,
                user2_receive_message_from_user1
            ]
            
        self.assertEqual(message_list, expect_message_list)



if __name__ == '__main__':
    unittest.main()