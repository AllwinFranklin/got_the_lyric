from django.db import models
# Create your models here.

keyChoices = [
    ('A', 'A'),
    ('A#/Bb', 'A#/Bb'),
    ('B', 'B'),
    ('C', 'C'),
    ('C#/Db', 'C#/Db'),
    ('D', 'D'),
    ('D#/Eb', 'D#/Eb'),
    ('E', 'E'),
    ('F', 'F'),
    ('F#/Gb', 'F#/Gb'),
    ('G', 'G'),
    ('G#/Ab', 'G#/Ab')
]

class Lyric(models.Model):
    author = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=200)
    key = models.CharField(max_length=5, choices=keyChoices)
    lyrics = models.TextField()
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.title