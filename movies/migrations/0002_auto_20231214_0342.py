from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='BUDGET',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movies',
            name='REVIEWS',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movies',
            name='VOTES',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
