# Generated by Django 2.2.12 on 2020-04-14 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("gdpr_helpers", "0002_auto_20200305_1530")]

    operations = [
        migrations.AlterField(
            model_name="legalreasongroup",
            name="where",
            field=models.CharField(
                choices=[
                    ("contact_form", "Contact form"),
                    ("registration_form", "Registration form"),
                    ("landing_form", "Landing form"),
                    ("newsletter_form", "Newsletter form"),
                ],
                max_length=20,
                unique=True,
                verbose_name="Posizione del gruppo",
            ),
        )
    ]