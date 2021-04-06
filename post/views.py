from django.shortcuts import render, redirect
from post.models import Post
from post.forms import PostForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

@login_required
def homepage(request):
    return render(request, 'homepage.html')

# def post_view(request):
#     if request.method == 'POST':
#         uploaded_file = request.FILES['document']
#         # print(uploaded_file.name)
#         # print(uploaded_file.size)
#         fs = FileSystemStorage()
#         fs.save(uploaded_file.name, uploaded_file)
#     return render(request, 'upload_form.html')

@login_required
def post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # print('form is valid')
            # form.display_name = request.user
            # print(request.user)
            # print(form)
            # form.save()
            new_data = Post.objects.create(
                display_name = request.user,
                caption = form.cleaned_data['caption'],
                post_pic = form.cleaned_data['post_pic']
            )
            new_data.save()
            return redirect('homepage')
    else:
        form = PostForm()
    return render(request, 'upload_form.html', {'form': form})


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})