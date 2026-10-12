from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Post, Follow, Like


class SocialTests(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username='bea',
            password='12345test'
        )

        self.user2 = User.objects.create_user(
            username='maria',
            password='12345test'
        )

    def test_user_can_create_post(self):
        self.client.login(
            username='bea',
            password='12345test'
        )

        response = self.client.post(
            reverse('create_post'),
            {
                'text': 'Mi primera publicación'
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(
            Post.objects.first().author,
            self.user1
        )

    def test_user_can_follow_another_user(self):
        self.client.login(
            username='bea',
            password='12345test'
        )

        response = self.client.get(
            reverse(
                'follow_user',
                args=['maria']
            )
        )

        self.assertEqual(response.status_code, 302)

        self.assertTrue(
            Follow.objects.filter(
                follower=self.user1,
                following=self.user2
            ).exists()
        )

    def test_user_can_unfollow_another_user(self):
        Follow.objects.create(
            follower=self.user1,
            following=self.user2
        )

        self.client.login(
            username='bea',
            password='12345test'
        )

        response = self.client.get(
            reverse(
                'unfollow_user',
                args=['maria']
            )
        )

        self.assertEqual(response.status_code, 302)

        self.assertFalse(
            Follow.objects.filter(
                follower=self.user1,
                following=self.user2
            ).exists()
        )

    def test_user_can_like_and_remove_like(self):
        post = Post.objects.create(
            author=self.user2,
            text='Publicación de prueba'
        )

        self.client.login(
            username='bea',
            password='12345test'
        )

        self.client.get(
            reverse(
                'like_post',
                args=[post.id]
            )
        )

        self.assertTrue(
            Like.objects.filter(
                user=self.user1,
                post=post
            ).exists()
        )

        self.client.get(
            reverse(
                'like_post',
                args=[post.id]
            )
        )

        self.assertFalse(
            Like.objects.filter(
                user=self.user1,
                post=post
            ).exists()
        )

    def test_home_shows_followed_users_posts(self):
        Follow.objects.create(
            follower=self.user1,
            following=self.user2
        )

        post = Post.objects.create(
            author=self.user2,
            text='Post de usuario seguido'
        )

        self.client.login(
            username='bea',
            password='12345test'
        )

        response = self.client.get(
            reverse('home')
        )

        self.assertContains(
            response,
            post.text
        )