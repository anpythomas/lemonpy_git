from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.generic.edit import CreateView, View

from .forms import UserRegistrationForm, MakePostForm, CreateCommentForm
from .models import Post, Likes, Comments


# Create your views here.
def index(request):
    recent_posts = Post.objects.all().order_by("-date")[:3]
    content = {"recent_posts": recent_posts}

    return render(request, "blog_app/index.html", content)


def all_posts(request):
    recent_posts = Post.objects.all().order_by("-date")
    content = {"recent_posts": recent_posts}

    return render(request, "blog_app/all_posts.html", content)


def post_detail(request, slug):
    selected_post = Post.objects.get(slug=slug)
    loggedin_user = request.user.id
    total_likes = Likes.objects.filter(post_id=selected_post.id).count()
    qs_does_user_like = Likes.objects.filter(user_id=loggedin_user, post_id=selected_post.id)
    does_user_like_count = qs_does_user_like.count()

    # Run query on comments associated with posts
    try:
        comments_for_post = Comments.objects.filter(post_id=selected_post.id)
    except:
        comments_for_post = None


    if request.method == "POST":
        print("POST HERE")
        if does_user_like_count == 0:
            like_row = Likes(user_id=int(loggedin_user), post_id=int(selected_post.id))
            like_row.save()
        else:
            like_row = Likes.objects.get(user_id=loggedin_user, post_id=selected_post.id)
            like_row.delete()

        return redirect("single-post", selected_post.slug)


    if does_user_like_count == 0:
        is_liked = False
    else:
        is_liked = True
    
    selected_post = Post.objects.get(slug=slug)
    comment_form = CreateCommentForm()
    context = {"post": selected_post, "total_likes": total_likes, "is_liked": is_liked, "comment_form": comment_form, "comments_for_post": comments_for_post, "comment_author": loggedin_user}
    
    return render(request, "blog_app/single_post.html", context)



def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():

            # Create new user object but don't save yet. Check passwords.
            new_user = user_form.save(commit=False)

            # Set password
            new_user.set_password(user_form.cleaned_data["password_1"])
            new_user.save()
            content = {"user_form": user_form}

            return render(request, "account/register_done.html", content)

    else:
        user_form = UserRegistrationForm()
        {"user_form": user_form}

    return render(request, "account/register.html", {"user_form": user_form})


# LoginRequiredMixin will require login to access view
class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = "account/new_post.html"
    model = Post
    fields = ["title", "rating", "image", "content"]
    success_url = "/all-posts"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
def update_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    update_form = MakePostForm(request.POST or None, instance=post)

    if update_form.is_valid():
        update_form.save()
        return redirect("all-posts")

    context = {"update_form": update_form}
    
    return render(request, "account/update.html", context)


@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()

    return render(request, "blog_app/deleted_confirmation.html")


def add_comment(request, slug):
    loggedin_user = request.user.id
    selected_post = Post.objects.get(slug=slug)
    
    if request.method == "POST":
        comment = request.POST['comment']
        comment_row = Comments(user_id=int(loggedin_user), post_id=int(selected_post.id), comment=comment, comments_username=request.user.username)
        comment_row.save()

        return redirect("single-post", slug)

    
def my_likes(request):
    loggedin_user = request.user.id
    posts_liked_by_user = Likes.objects.filter(user_id=loggedin_user)

    posts_list = list()
    for like in posts_liked_by_user:
        try:
            single_post = Post.objects.get(pk=like.post_id)
            posts_list.append(single_post)
        except:
            pass
    
    context = {"posts_list": posts_list}

    return render(request, "blog_app/my_likes.html", context)


def title(request):
    return render(request, "blog_app/title.html")