# Generated by Django 5.1.2 on 2024-11-12 07:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_bookinstance'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserX',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AuthorX',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200, null=True)),
                ('zipcode', models.IntegerField(null=True)),
                ('telephone', models.CharField(max_length=100, null=True)),
                ('joindate', models.DateField()),
                ('popularity_score', models.IntegerField()),
                ('recommendedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recommended_authors', related_query_name='recommended_authors', to='catalog.authorx')),
                ('followers', models.ManyToManyField(related_name='followed_authors', related_query_name='followed_authors', to='catalog.userx')),
            ],
        ),
        migrations.CreateModel(
            name='PublisherX',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('joindate', models.DateField()),
                ('popularity_score', models.IntegerField()),
                ('recommendedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.publisherx')),
            ],
        ),
        migrations.CreateModel(
            name='BooksX',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=200)),
                ('price', models.IntegerField(null=True)),
                ('published_date', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', related_query_name='books', to='catalog.authorx')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', related_query_name='books', to='catalog.publisherx')),
            ],
        ),
    ]
