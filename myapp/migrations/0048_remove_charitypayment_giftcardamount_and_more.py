# Generated by Django 5.0.2 on 2024-03-25 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0047_alter_charitypayment_giftcardamount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charitypayment',
            name='giftcardamount',
        ),
        migrations.RemoveField(
            model_name='charitypayment',
            name='giftcardcode',
        ),
        migrations.RemoveField(
            model_name='charitypayment',
            name='giftcardimg',
        ),
        migrations.RemoveField(
            model_name='charitypayment',
            name='giftcardname',
        ),
    ]
