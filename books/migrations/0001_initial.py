from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=150)),
                ('publisher', models.CharField(max_length=150)),
                ('publication_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
