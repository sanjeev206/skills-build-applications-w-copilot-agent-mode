from rest_framework.test import APITestCase
from django.urls import reverse
from .models import User, Team, Activity, Workout, Leaderboard

class UserTests(APITestCase):
    def test_create_user(self):
        url = reverse('user-list')
        data = {'username': 'testuser', 'email': 'test@example.com', 'first_name': 'Test', 'last_name': 'User'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

class TeamTests(APITestCase):
    def test_create_team(self):
        user = User.objects.create(username='member', email='member@example.com', first_name='Mem', last_name='Ber')
        url = reverse('team-list')
        data = {'name': 'Test Team', 'members': [user.id]}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

class ActivityTests(APITestCase):
    def test_create_activity(self):
        user = User.objects.create(username='activityuser', email='activity@example.com', first_name='Act', last_name='Ity')
        url = reverse('activity-list')
        data = {'user': user.id, 'type': 'run', 'duration': 30, 'distance': 5.0, 'calories': 300, 'date': '2024-01-01'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

class WorkoutTests(APITestCase):
    def test_create_workout(self):
        user = User.objects.create(username='workoutuser', email='workout@example.com', first_name='Work', last_name='Out')
        url = reverse('workout-list')
        data = {'user': user.id, 'name': 'Morning Run', 'description': 'A quick run', 'date': '2024-01-01'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

class LeaderboardTests(APITestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Leaderboard Team')
        url = reverse('leaderboard-list')
        data = {'team': team.id, 'total_points': 100}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
