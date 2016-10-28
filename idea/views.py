from django.shortcuts import render, get_object_or_404
from .models import Idea

def index(request):
    all_ideas = Idea.objects.all()
    return render(request, 'idea/home.html', {'all_ideas': all_ideas})

def idea_details(request, idea_id):
    idea = get_object_or_404(Idea, pk=idea_id)
    return render(request, 'idea/idea_details.html', {'idea': idea})
