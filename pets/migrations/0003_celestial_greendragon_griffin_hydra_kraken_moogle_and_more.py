# Generated by Django 4.2.5 on 2023-09-20 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_remove_glorb_max_energy_remove_glorb_max_happiness_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Celestial',
            fields=[
                ('pet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pets.pet')),
                ('pet_type', models.CharField(default='Celestial Dragon', editable=False, max_length=45)),
                ('experience', models.IntegerField(default=0)),
                ('xp_to_lvl', models.IntegerField(default=120)),
            ],
            bases=('pets.pet',),
        ),
        migrations.CreateModel(
            name='GreenDragon',
            fields=[
                ('pet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pets.pet')),
                ('pet_type', models.CharField(default='Green Dragon', editable=False, max_length=45)),
                ('experience', models.IntegerField(default=0)),
                ('xp_to_lvl', models.IntegerField(default=10)),
            ],
            bases=('pets.pet',),
        ),
        migrations.CreateModel(
            name='Griffin',
            fields=[
                ('pet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pets.pet')),
                ('pet_type', models.CharField(default='Griffin', editable=False, max_length=45)),
                ('experience', models.IntegerField(default=0)),
                ('xp_to_lvl', models.IntegerField(default=15)),
            ],
            bases=('pets.pet',),
        ),
        migrations.CreateModel(
            name='Hydra',
            fields=[
                ('pet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pets.pet')),
                ('pet_type', models.CharField(default='Hydra', editable=False, max_length=45)),
                ('experience', models.IntegerField(default=0)),
                ('xp_to_lvl', models.IntegerField(default=40)),
            ],
            bases=('pets.pet',),
        ),
        migrations.CreateModel(
            name='Kraken',
            fields=[
                ('pet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pets.pet')),
                ('pet_type', models.CharField(default='Kraken', editable=False, max_length=45)),
                ('experience', models.IntegerField(default=0)),
                ('xp_to_lvl', models.IntegerField(default=20)),
            ],
            bases=('pets.pet',),
        ),
        migrations.CreateModel(
            name='Moogle',
            fields=[
                ('pet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pets.pet')),
                ('pet_type', models.CharField(default='Moogle', editable=False, max_length=45)),
                ('experience', models.IntegerField(default=5)),
                ('xp_to_lvl', models.IntegerField(default=12)),
            ],
            bases=('pets.pet',),
        ),
        migrations.CreateModel(
            name='MythicGriffin',
            fields=[
                ('pet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pets.pet')),
                ('pet_type', models.CharField(default='Mythic Griffin', editable=False, max_length=45)),
                ('experience', models.IntegerField(default=0)),
                ('xp_to_lvl', models.IntegerField(default=50)),
            ],
            bases=('pets.pet',),
        ),
        migrations.CreateModel(
            name='RedDragon',
            fields=[
                ('pet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pets.pet')),
                ('pet_type', models.CharField(default='Red Dragon', editable=False, max_length=45)),
                ('experience', models.IntegerField(default=0)),
                ('xp_to_lvl', models.IntegerField(default=10)),
            ],
            bases=('pets.pet',),
        ),
        migrations.CreateModel(
            name='Siren',
            fields=[
                ('pet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pets.pet')),
                ('pet_type', models.CharField(default='Cat-siren', editable=False, max_length=45)),
                ('experience', models.IntegerField(default=9)),
                ('xp_to_lvl', models.IntegerField(default=10)),
            ],
            bases=('pets.pet',),
        ),
        migrations.CreateModel(
            name='Snek',
            fields=[
                ('pet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pets.pet')),
                ('pet_type', models.CharField(default='Snek', editable=False, max_length=45)),
                ('experience', models.IntegerField(default=0)),
                ('xp_to_lvl', models.IntegerField(default=10)),
            ],
            bases=('pets.pet',),
        ),
        migrations.CreateModel(
            name='TartCat',
            fields=[
                ('pet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pets.pet')),
                ('pet_type', models.CharField(default='Tart-cat', editable=False, max_length=45)),
                ('experience', models.IntegerField(default=9)),
                ('xp_to_lvl', models.IntegerField(default=10)),
            ],
            bases=('pets.pet',),
        ),
    ]