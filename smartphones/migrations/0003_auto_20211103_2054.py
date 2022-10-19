# Generated by Django 3.2.8 on 2021-11-03 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartphones', '0002_alter_mobilevariant_price_variant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobilegeneral',
            name='os_version',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='mobilegeneral',
            name='slots',
            field=models.CharField(choices=[('Dual SIM(2) + Dedicated Memory Card Slot', 'Dual SIM(2) + Dedicated Memory Card Slot'), ('Dual SIM(2) (One SIM slot + one hybrid SIM slot)', 'Dual SIM(2) (One SIM slot + one hybrid SIM slot)'), ('One SIM slot + one e-SIM slot', 'One SIM slot + one e-SIM slot')], default='Dual SIM(2) + Dedicated Memory Card Slot', max_length=200),
        ),
    ]