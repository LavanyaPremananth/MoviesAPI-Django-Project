from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20231214_0342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies',
            old_name='BUDGET',
            new_name='budget',
        ),
        migrations.RenameField(
            model_name='movies',
            old_name='REVIEWS',
            new_name='reviews',
        ),
        migrations.RenameField(
            model_name='movies',
            old_name='VOTES',
            new_name='votes',
        ),
    ]
