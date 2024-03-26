# Generated by Django 5.0 on 2024-03-26 17:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0013_alter_creditnote_reference_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditnotehistory',
            name='credit_note_history',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billapp.creditnote'),
        ),
        migrations.AlterField(
            model_name='creditnoteitem',
            name='credit_note',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billapp.creditnote'),
        ),
    ]
