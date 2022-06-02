from django.shortcuts import render, redirect
from .models import Lyric
from .forms import LyricForm
from django.contrib import messages

# Create your views here.
def lyricView(request):
	if request.method == "POST":
		lyric_form = LyricForm(request.POST, request.FILES)
		if lyric_form.is_valid():
			lyric_form.save()
			messages.success(request, ('Your Lyric was successfully added!'))
		else:
			messages.error(request, 'Error saving your lyric')
		
		return redirect("lyricView")
		
	lyric_form = LyricForm()
	lyrics = Lyric.objects.all()
	return render(request=request, template_name="lyrics.html", context={'lyric_form':lyric_form, 'lyrics':lyrics})