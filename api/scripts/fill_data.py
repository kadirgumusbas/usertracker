from core.models import CustomUser, Address, Company, Geo, Todo, Post, Album, Photo, Comment
from django.contrib.auth.hashers import make_password
from faker import Faker

import random

fake = Faker()

for _ in range(20):
    geo = Geo.objects.create(lat=fake.latitude(), lng=fake.longitude())
    address = Address.objects.create(
        street=fake.street_name(),
        suite=fake.secondary_address(),
        city=fake.city(),
        zipcode=fake.zipcode()[:20],  # max_length kontrolü
        geo=geo
    )
    company = Company.objects.create(name=fake.company())

    user = CustomUser.objects.create(
        name=fake.unique.user_name(),
        username=fake.unique.user_name(),
        email=fake.email(),
        phone=fake.phone_number()[:20],
        website=fake.domain_name(),
        address=address,
        company=company,
        password=make_password("password123")
    )

    for _ in range(10):
        album = Album.objects.create(user=user, title=fake.sentence())
        for _ in range(10):
            Photo.objects.create(
                album=album,
                title=fake.sentence()
            )

    for _ in range(10):
        Todo.objects.create(
            user=user,
            title=fake.sentence(),
            completed=random.choice([True, False])
        )

    for _ in range(10):
        post = Post.objects.create(
            user=user,
            title=fake.sentence(),
            body=fake.text()
        )
        for _ in range(10):
            Comment.objects.create(
                post=post,
                name=fake.name(),
                body=fake.text(),
                email=fake.email()
            )
