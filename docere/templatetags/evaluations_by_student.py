
from django import template

# https://stackoverflow.com/questions/2683621/django-filefield-how-to-return-filename-only-in-template
register = template.Library()

@register.filter
def evaluations_by_student(student, evaluation):
    return student.puntuations.filter(evaluation=evaluation)
