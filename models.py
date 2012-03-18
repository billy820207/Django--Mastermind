from django.db import models

# Create your models here.

COLOR_CHOICES = (
    ('BL', 'Blue'),
    ('GR', 'Green'),
    ('RD', 'Red'),
    ('YL', 'Yellow'),
    ('BK', 'Black'),
    ('WH', 'White'),
)


class Game(models.Model):
    solution1 = models.CharField(max_length=2, choices=COLOR_CHOICES)
    solution2 = models.CharField(max_length=2, choices=COLOR_CHOICES)
    solution3 = models.CharField(max_length=2, choices=COLOR_CHOICES)
    solution4 = models.CharField(max_length=2, choices=COLOR_CHOICES)
    
    def solutions(self):
        return [self.solution1, self.solution2, self.solution3, self.solution4]
    
    def __unicode__(self):
        return ", ".join(self.solutions())
   
class Guess(models.Model):
    step = models.IntegerField()
    guess1 = models.CharField(max_length=2, choices=COLOR_CHOICES)
    guess2 = models.CharField(max_length=2, choices=COLOR_CHOICES)
    guess3 = models.CharField(max_length=2, choices=COLOR_CHOICES)
    guess4 = models.CharField(max_length=2, choices=COLOR_CHOICES)
    game = models.ForeignKey(Game)
    
    def guesses(self):
        return [self.guess1, self.guess2, self.guess3, self.guess4]
    
    def __unicode__(self):
        return unicode(self.step) + ": " + ", ".join(self.guesses())
    
    
