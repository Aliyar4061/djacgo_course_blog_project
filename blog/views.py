from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import  User
from blog.forms import NewPostForm

#########################Post views########################

# Post views

# (Functional Based)
# def Post_list_view(request):
#     post_list = Post.objects.filter(status ='pub').order_by('-modified_date')
#     context = {'posts': post_list}
#     return render(request, 'blog/posts_list.html', context)

# Class_based view
class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(
            status='pub'
        ).order_by('-modified_date')

##########################PostDetailView##################################

# # (Functional Based)
# # For getting more information from a post
# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     context = {'post': post}
#     return render(request, 'blog/post_detail.html', context)

# Class_based view
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

 ############################PostCreateView#################################

# Django-Form
# def post_create_view(request):
#     if request.method == 'POST':
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return  redirect('posts_list')
#     else:
#         form = NewPostForm()
#
#
#     return render(request, 'blog/post_create.html',
#                       {'form': form})

class PostCreateView(generic.CreateView):
    model = Post
    form_class = NewPostForm
    template_name = 'blog/post_create.html'

##############################PostUpdateView############################

# updating form and comments
def post_update_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = NewPostForm(request.POST or None, instance=post)

    if form.is_valid():
            form.save()
            return redirect('posts_list')

    return render(request, 'blog/post_create.html',
                          {'form': form})

class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = NewPostForm
    template_name = 'blog/post_create.html'
    # context_object_name = 'post'


######################################################3

def post_delete_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    if request.method == 'POST':
        post.delete()
        return redirect('posts_list')
    return render(request, 'blog/post_delete.html', context)

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('posts_list')




#-----------------------------------------------------------#
# def post_create_view(request):
#     if request.method == 'POST':
#         post_title = request.POST.get('title')
#         post_text = request.POST.get('text')
#
#         user = User.objects.all()[0]
#
#         post = Post.objects.create(title=post_title,
#                     content=post_text,
#                     author=user,
#                     status='pub')
#     else:
#         print('Get Request')
#     return render(request, 'blog/post_create.html')

# def post_detail_view(request, pk):
#     post = Post.objects.get(pk=pk)
#     context = {'post': post}
#     return render(request, 'blog/post_detail.html', context)

