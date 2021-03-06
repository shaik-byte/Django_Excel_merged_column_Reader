# Generated by Django 3.1.5 on 2021-01-29 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importer', '0021_aparajitha6'),
    ]

    operations = [
        migrations.CreateModel(
            name='Common_Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Applicable_at_the_Country_Level', models.CharField(max_length=20)),
                ('Setting_Title', models.CharField(max_length=20)),
                ('State', models.CharField(max_length=20)),
                ('District', models.CharField(max_length=20)),
                ('Threshold_limit', models.CharField(max_length=20)),
                ('Applicable_Regular_Employee', models.CharField(max_length=20)),
                ('Applicable_Trainee', models.CharField(max_length=20)),
                ('Applicable_Contract_Worker', models.CharField(max_length=20)),
                ('Applicable_International_Worker', models.CharField(max_length=20)),
                ('Group_Level', models.CharField(max_length=20)),
                ('Legal_Entity_Level', models.CharField(max_length=20)),
                ('Unit_Level', models.CharField(max_length=20)),
                ('Periodicity', models.CharField(max_length=20)),
                ('DOR_1_Day', models.CharField(max_length=20)),
                ('DOR_1_Month', models.CharField(max_length=20)),
                ('DOR_2_Day', models.CharField(max_length=20)),
                ('DOR_2_Month', models.CharField(max_length=20)),
                ('DOR_3_Day', models.CharField(max_length=20)),
                ('DOR_4_Day', models.CharField(max_length=20)),
                ('DOR_4_Month', models.CharField(max_length=20)),
                ('Is_Last_Day_of_Every_Month', models.CharField(max_length=20)),
                ('Custom_Day', models.CharField(max_length=20)),
                ('Contribution_period_starts_on', models.CharField(max_length=20)),
                ('Effective_From', models.CharField(max_length=20)),
                ('Primary_Setting_Name', models.CharField(max_length=20)),
                ('Range_Based_on', models.CharField(max_length=20)),
                ('Range_ID', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='aparajitha10',
        ),
        migrations.DeleteModel(
            name='aparajitha6',
        ),
    ]
