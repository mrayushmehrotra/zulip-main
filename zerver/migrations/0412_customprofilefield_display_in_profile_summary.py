# Generated by Django 4.0.7 on 2022-09-19 17:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0411_alter_muteduser_muted_user_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customprofilefield",
            name="display_in_profile_summary",
            field=models.BooleanField(default=False),
        ),
    ]