import unittest
import requests

class TaskApiTest(unittest.TestCase):
    BASE_URL = 'http://localhost:5000/api/tasks'

    def test_1_get_all_tasks(self):
        response = requests.get(self.BASE_URL)
        self.assertEqual(response.status_code, 200)
        tasks = response.json()
        self.assertIsInstance(tasks, list)
        self.assertTrue(len(tasks) > 0)

    def test_2_get_task(self):
        task_id = '2'
        response = requests.get(f'{self.BASE_URL}/{task_id}')
        self.assertEqual(response.status_code, 200)
        task = response.json()
        self.assertIsInstance(task, dict)
        self.assertIn('_id', task)
        self.assertIn('title', task)
        self.assertIn('description', task)

    def test_3_create_task(self):
        task_data = {
            '_id' : '6',
            'title': 'New Task',
            'description': 'Task description'
        }
        response = requests.post(self.BASE_URL, json=task_data)
        self.assertEqual(response.status_code, 201)
        result = response.json()
        self.assertIsInstance(result, dict)
        self.assertIn('inserted_id', result)

    def test_4_update_task(self):
        task_id = '6'
        task_data = {
            'title': 'Updated Task',
            'description': 'Updated task description'
        }
        response = requests.put(f'{self.BASE_URL}/{task_id}', json=task_data)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, dict)
        self.assertIn('message', result)
        self.assertEqual(result['message'], 'Task successfully updated.')

    def test_5_delete_task(self):
        task_id = '1'
        response = requests.delete(f'{self.BASE_URL}/{task_id}')
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, dict)
        self.assertIn('message', result)
        self.assertEqual(result['message'], 'Task successfully deleted.')
    
    def test_6_get_nonexistent_task(self):
        task_id = '1'
        response = requests.get(f'{self.BASE_URL}/{task_id}')
        self.assertEqual(response.status_code, 404)
        error = response.json()
        self.assertIsInstance(error, dict)
        self.assertIn('error', error)
        self.assertEqual(error['error'], 'Task not found.')
    
    def test_7_update_nonexistent_task(self):
        task_id = '1'
        task_data = {
            'title': 'Updated Task',
            'description': 'Updated task description'
        }
        response = requests.put(f'{self.BASE_URL}/{task_id}', json=task_data)
        self.assertEqual(response.status_code, 404)
        error = response.json()
        self.assertIsInstance(error, dict)
        self.assertIn('error', error)
        self.assertEqual(error['error'], 'Task not found.')
    
    def test_8_delete_nonexistent_task(self):
        task_id = '1'
        response = requests.delete(f'{self.BASE_URL}/{task_id}')
        self.assertEqual(response.status_code, 404)
        error = response.json()
        self.assertIsInstance(error, dict)
        self.assertIn('error', error)
        self.assertEqual(error['error'], 'Task not found.')   


    def test_9_no_changes_made_to_task(self):
        task_id = '6'
        task_data = {
            'title': 'Updated Task',
            'description': 'Updated task description'
        }
        response = requests.put(f'{self.BASE_URL}/{task_id}', json=task_data)
        self.assertEqual(response.status_code, 400)
        result = response.json()
        self.assertIsInstance(result, dict)
        self.assertIn('error', result)
        self.assertEqual(result['error'], 'No changes made to the task.')


    def test_10_delete_task(self):
        task_id = '6'
        response = requests.delete(f'{self.BASE_URL}/{task_id}')
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, dict)
        self.assertIn('message', result)
        self.assertEqual(result['message'], 'Task successfully deleted.')

    
    def test_11_create_task(self):
        task_data = {
            'title': 'TASK without id',
            'description': 'Task description'
        }
        response = requests.post(self.BASE_URL, json=task_data)
        self.assertEqual(response.status_code, 201)
        result = response.json()
        self.assertIsInstance(result, dict)
        self.assertIn('inserted_id', result)



if __name__ == '__main__':
    unittest.main()
