from django.core.management.base import BaseCommand 
from profiles.models import Profile, Post
from faker import Faker
import random

IMAGES = [f'images/img{i}.jpg' for i in range(1, 116)]
COLORS = ['Red', 'Blue', 'Green', 'Orange', 'Purple']

fake = Faker()

class Command(BaseCommand):
    help = 'Generate fake data'

    def handle(self, *args, **options):
        # Create fake profiles
        for _ in range(10):
            profile = Profile.objects.create(
                name=fake.name(),
                clan=fake.word(),
                allegiance=fake.word(),
                rank=fake.random_element(elements=('Private','Sergeant','Captain','Lord','Commander','Knight')),
                occupation=fake.job(),
                nationality=fake.country(),
                age=random.randint(18, 65),
                color=random.choice(COLORS)
            )

            # Create fake posts for this profile
            for _ in range(2):  # 2 posts per profile
                Post.objects.create(
                    profile=profile,
                    content=fake.sentence(),
                    color=random.choice(COLORS),
                    image=random.choice(IMAGES)
                )

        self.stdout.write(self.style.SUCCESS('Fake data generated successfully!'))
