from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imdb_id', models.CharField(max_length=50)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('original_title', models.CharField(blank=True, max_length=100, null=True)),
                ('year', models.CharField(blank=True, max_length=10, null=True)),
                ('date_published', models.DateField(blank=True, null=True)),
                ('genre', models.CharField(blank=True, max_length=100, null=True)),
                ('duration', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('language', models.CharField(blank=True, max_length=50, null=True)),
                ('director', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
