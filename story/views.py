from django.shortcuts import render, redirect, get_object_or_404
from .models import Story
import urllib.parse

def home(request):
    stories = Story.objects.all().order_by('-created_at')
    return render(request, 'story/home.html', {'stories': stories})

def create_story(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        safe_prompt = urllib.parse.quote(f"comic book style, {content}")
        image_url = f"https://image.pollinations.ai/prompt/{safe_prompt}"

        story = Story.objects.create(
            title=title, 
            content=content,
            prompt=content,
            image_url=image_url
        )
        return redirect('detail', story_id=story.id)
    return render(request, 'story/create.html')

def story_detail(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    return render(request, 'story/detail.html', {'story': story})
