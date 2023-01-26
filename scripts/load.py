import csv
import os
from poems.models import Poem
from authors.models import Author


def run():
    file = open(
        '/Users/sam/GA-Work/projects/project-4/ga-project-4-backend/scripts/poem_dataset.csv')
    read_file = csv.reader(file)

    Poem.objects.all().delete()
    Author.objects.all().delete()

    count = 1

    for poem in read_file:
        if count == 1:
            pass
        else:
            author, created = Author.objects.get_or_create(name=poem[1])
            Poem.objects.create(
                author=Author.objects.get(name=poem[1]), title=poem[2], content=poem[4])
        count = count+1
