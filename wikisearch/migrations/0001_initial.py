# Generated by Django 3.2.20 on 2023-07-20 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WikiUrlLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('url', models.URLField(db_index=True)),
                ('param', models.CharField(blank=True, db_index=True, max_length=100)),
                ('summary', models.JSONField(blank=True, db_index=True, null=True)),
                ('fullurl', models.URLField(blank=True, db_index=True)),
                ('httpstatus', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['url'],
            },
        ),
        migrations.CreateModel(
            name='WikiLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('link', models.CharField(db_index=True, max_length=200)),
                ('url', models.URLField(blank=True, db_index=True)),
                ('wikis', models.ManyToManyField(to='wikisearch.WikiUrlLog')),
            ],
        ),
    ]