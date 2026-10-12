from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Post,Profile, Follow,Like,Comment
from django.db.models import Q
from .forms import PostForm, CommentForm, ProfileForm

def home(request):

    if request.user.is_authenticated:

        following_users = Follow.objects.filter(
            follower=request.user
        ).values_list(
            'following',
            flat=True
        )

        posts = Post.objects.filter(
            Q(author=request.user) |
            Q(author__in=following_users)
        ).order_by('-created_at')

    else:
        posts = Post.objects.all().order_by('-created_at')

    return render(
        request,
        'social/home.html',
        {'posts': posts}
    )

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'social/register.html', {
        'form': form
    })

@login_required
def create_post(request):

    if request.method == 'POST':

        form = PostForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            post = form.save(commit=False)

            post.author = request.user

            post.save()

            return redirect('home')

    else:
        form = PostForm()

    return render(
        request,
        'social/create_post.html',
        {'form': form}
    )

def profile(request, username):
    profile_user = get_object_or_404(
        User,
        username=username
    )

    profile, created = Profile.objects.get_or_create(
        user=profile_user
    )

    user_posts = Post.objects.filter(
        author=profile_user
    ).order_by('-created_at')

    followers_count = Follow.objects.filter(
        following=profile_user
    ).count()

    following_count = Follow.objects.filter(
        follower=profile_user
    ).count()

    is_following = False

    if request.user.is_authenticated:
        is_following = Follow.objects.filter(
            follower=request.user,
            following=profile_user
        ).exists()

    return render(
        request,
        'social/profile.html',
        {
            'profile_user': profile_user,
            'profile': profile,
            'user_posts': user_posts,
            'followers_count': followers_count,
            'following_count': following_count,
            'is_following': is_following,
        }
    )

    
@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(
        User,
        username=username
    )

    if user_to_follow != request.user:
        Follow.objects.get_or_create(
            follower=request.user,
            following=user_to_follow
        )

    return redirect(
        'profile',
        username=username
    )


@login_required
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(
        User,
        username=username
    )

    Follow.objects.filter(
        follower=request.user,
        following=user_to_unfollow
    ).delete()

    return redirect(
        'profile',
        username=username
    )

@login_required
def like_post(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id
    )

    like, created = Like.objects.get_or_create(
        user=request.user,
        post=post
    )

    if not created:
        like.delete()

    return redirect('home')

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()

    return redirect('home')

@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':

        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()

            return redirect(
                'profile',
                username=request.user.username
            )

    else:
        form = ProfileForm(
            instance=profile
        )

    return render(
        request,
        'social/edit_profile.html',
        {'form': form}
    )

@login_required
def users_list(request):

    users = User.objects.exclude(
        id=request.user.id
    ).order_by('username')

    return render(
        request,
        'social/users_list.html',
        {
            'users': users
        }
    )