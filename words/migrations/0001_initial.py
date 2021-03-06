# Generated by Django 3.2.7 on 2022-02-12 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Words',
            fields=[
                ('word_id', models.AutoField(primary_key=True, serialize=False)),
                ('word', models.CharField(blank=True, max_length=100, null=True)),
                ('definition', models.TextField(blank=True, null=True)),
                ('example_1', models.TextField(blank=True, null=True)),
                ('example_2', models.TextField(blank=True, null=True)),
                ('origination', models.CharField(blank=True, max_length=50, null=True)),
                ('part_of_speech', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'words',
                'managed': False,
            },
        ),
    ]
