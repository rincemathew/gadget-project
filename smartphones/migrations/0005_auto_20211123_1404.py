# Generated by Django 3.2.8 on 2021-11-23 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smartphones', '0004_alter_mobileperformance_processor_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobilevariant',
            name='mobileBattery',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobile_battery', to='smartphones.mobilebattery'),
        ),
        migrations.AlterField(
            model_name='mobilevariant',
            name='mobileCamera',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobile_camera', to='smartphones.mobilecamera'),
        ),
        migrations.AlterField(
            model_name='mobilevariant',
            name='mobileConnectivity',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobile_connectivity', to='smartphones.mobileconnectivity'),
        ),
        migrations.AlterField(
            model_name='mobilevariant',
            name='mobileDisplay',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobile_display', to='smartphones.mobiledisplay'),
        ),
        migrations.AlterField(
            model_name='mobilevariant',
            name='mobileGeneral',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobile_general', to='smartphones.mobilegeneral'),
        ),
        migrations.AlterField(
            model_name='mobilevariant',
            name='mobilePerformance',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobile_performance', to='smartphones.mobileperformance'),
        ),
        migrations.AlterField(
            model_name='mobilevariant',
            name='mobileSensor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobile_sensor', to='smartphones.mobilesensor'),
        ),
        migrations.AlterField(
            model_name='mobilevariant',
            name='mobileStorage',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobile_storage', to='smartphones.mobilestorage'),
        ),
        migrations.AlterField(
            model_name='mobilevariant',
            name='otherFeature',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobile_other', to='smartphones.otherfeature'),
        ),
        migrations.AlterField(
            model_name='mobilevariant',
            name='price_variant',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobile_price', to='smartphones.onlineprice'),
        ),
    ]
