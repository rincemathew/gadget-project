# Generated by Django 3.2.8 on 2021-11-03 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=30, unique=True)),
                ('brand_name_url', models.SlugField(max_length=30)),
                ('brand_logo', models.ImageField(blank=True, null=True, upload_to='brand-logo/')),
            ],
        ),
        migrations.CreateModel(
            name='MobileBattery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('battery_capacity', models.IntegerField()),
                ('battery_type', models.CharField(blank=True, choices=[('LI-ION', 'Li-ion'), ('LI-POLY', 'Li-poly')], max_length=10, null=True)),
                ('fast_charger', models.BooleanField(blank=True, default=True, null=True)),
                ('fast_charging', models.CharField(blank=True, max_length=200, null=True)),
                ('replaceable', models.BooleanField(blank=True, default=False, null=True)),
                ('wireless_charger', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MobileCamera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_camera', models.IntegerField()),
                ('primary_camera_str', models.CharField(max_length=501)),
                ('primary_camera_features', models.CharField(blank=True, max_length=1200, null=True)),
                ('secondary_camera', models.IntegerField()),
                ('secondary_camera_str', models.CharField(max_length=50)),
                ('secondary_camera_features', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MobileConnectivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SAR_value', models.CharField(blank=True, max_length=100, null=True)),
                ('wi_fi', models.CharField(blank=True, max_length=100, null=True)),
                ('bluetooth', models.CharField(blank=True, default='v5.0', max_length=100, null=True)),
                ('GPS', models.BooleanField(default=True)),
                ('audio_jack', models.CharField(blank=True, default='3.5 mm', max_length=30, null=True)),
                ('USB_type_c', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MobileDisplay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_size', models.FloatField()),
                ('resolution', models.CharField(max_length=50)),
                ('resolution_type', models.CharField(blank=True, max_length=50, null=True)),
                ('GPU', models.CharField(blank=True, max_length=50, null=True)),
                ('display_type', models.CharField(max_length=100)),
                ('display_features', models.CharField(blank=True, max_length=700, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MobileGeneral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_date', models.DateTimeField(blank=True, null=True)),
                ('os', models.CharField(choices=[('ANDROID', 'Android'), ('IOS', 'ios')], max_length=10)),
                ('os_version', models.CharField(blank=True, max_length=10, null=True)),
                ('UI_version', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('is_available', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('Upcoming', 'Upcoming'), ('Available', 'Available'), ('not available', 'not available'), ('Rumored', 'Rumored')], default='Available', max_length=15)),
                ('dimensions', models.CharField(default='77 mm x 77 mm x  77 mm', max_length=50)),
                ('weight', models.FloatField()),
                ('slots', models.CharField(default='Dual SIM(2) + Dedicated Memory Card Slot', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MobileName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_name', models.CharField(max_length=50)),
                ('mobile_name_url', models.SlugField()),
                ('mobile_image', models.ImageField(upload_to='mobile_image/')),
                ('phone_type', models.CharField(choices=[('SMARTPHONE', 'Smartphone'), ('TABLET', 'Tablet')], default='Smartphone', max_length=20)),
                ('brandName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartphones.brandname')),
            ],
        ),
        migrations.CreateModel(
            name='MobilePerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ram', models.PositiveIntegerField()),
                ('processor', models.CharField(max_length=50)),
                ('processor_company', models.CharField(choices=[('Qualcomm', 'Qualcomm'), ('MediaTek', 'MediaTek'), ('Apple', 'Apple'), ('HiSilicon', 'HiSilicon'), ('Samsung', 'Samsung')], max_length=50)),
                ('clock_speed', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MobileSensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fingerprint_sensor', models.BooleanField(default=True)),
                ('fingerprint_position', models.CharField(blank=True, choices=[('SIDE', 'Side'), ('REAR', 'REAR'), ('FRONTSIDE', 'Front Side'), ('IN-DISPLAY', 'in-display')], max_length=20, null=True)),
                ('other_sensor', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='MobileStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_storage', models.PositiveIntegerField()),
                ('expandable_memory', models.BooleanField(default=True)),
                ('sim_slot_type', models.CharField(blank=True, choices=[('Dedicated Slot', 'DEDICATED SLOT'), ('Hybrid Slot', 'HYBRID SLOT')], default='Dedicated Slot', max_length=50, null=True)),
                ('expandable_memory_capacity', models.IntegerField(blank=True, null=True)),
                ('OTG_support', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MobileVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_variants', models.CharField(default='1 GB RAM, 16 GB Storage', max_length=50)),
                ('mobile_variants_url', models.SlugField(default='1-gb-ram-16-gb-storage')),
                ('mobile_url_themes_name', models.CharField(default='brand+name+variant', max_length=50)),
                ('image_credit', models.URLField(default='https://www.gadget4india.com/aboutus/')),
                ('mobileBattery', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smartphones.mobilebattery')),
                ('mobileCamera', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smartphones.mobilecamera')),
                ('mobileConnectivity', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smartphones.mobileconnectivity')),
                ('mobileDisplay', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smartphones.mobiledisplay')),
                ('mobileGeneral', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smartphones.mobilegeneral')),
                ('mobileNames', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobile_Variant', to='smartphones.mobilename')),
                ('mobilePerformance', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smartphones.mobileperformance')),
                ('mobileSensor', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smartphones.mobilesensor')),
                ('mobileStorage', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smartphones.mobilestorage')),
            ],
        ),
        migrations.CreateModel(
            name='OnlinePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flipkart', models.PositiveIntegerField(blank=True, null=True)),
                ('flipkart_URL', models.URLField(blank=True, null=True)),
                ('amazon', models.PositiveIntegerField(blank=True, null=True)),
                ('amazon_URL', models.URLField(blank=True, null=True)),
                ('tata_cliq', models.PositiveIntegerField(blank=True, null=True)),
                ('tata_cliq_URL', models.URLField(blank=True, null=True)),
                ('reliance_digital', models.PositiveIntegerField(blank=True, null=True)),
                ('reliance_digital_URL', models.URLField(blank=True, null=True)),
                ('mi_store', models.PositiveIntegerField(blank=True, null=True)),
                ('mi_store_URL', models.URLField(blank=True, null=True)),
                ('samsung', models.PositiveIntegerField(blank=True, null=True)),
                ('samsung_URL', models.URLField(blank=True, null=True)),
                ('vivo', models.PositiveIntegerField(blank=True, null=True)),
                ('vivo_URL', models.URLField(blank=True, null=True)),
                ('realme', models.PositiveIntegerField(blank=True, null=True)),
                ('realme_URL', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OtherFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other_Feature', models.CharField(blank=True, max_length=1000, null=True)),
                ('in_the_box', models.CharField(blank=True, max_length=300, null=True)),
                ('warranty', models.CharField(blank=True, max_length=300, null=True)),
                ('mobile_color', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VariantImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant_image', models.ImageField(upload_to='variant_image/')),
                ('variantImage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variant_Image', to='smartphones.mobilevariant')),
            ],
        ),
        migrations.AddField(
            model_name='mobilevariant',
            name='otherFeature',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smartphones.otherfeature'),
        ),
        migrations.AddField(
            model_name='mobilevariant',
            name='price_variant',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='smartphones.onlineprice'),
        ),
        migrations.CreateModel(
            name='MobileConnectivityDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sim_name', models.CharField(choices=[('SIM 1', 'SIM 1'), ('SIM 2', 'SIM 2'), ('SIM 3', 'SIM 3')], max_length=10)),
                ('sim_type', models.CharField(choices=[('NANO', 'Nano'), ('MICRO', 'Micro'), ('STANDARD', 'Standard'), ('eSIM', 'eSIM')], default='NANO', max_length=20)),
                ('hybrid_slot', models.BooleanField(default=False)),
                ('five_g', models.BooleanField(default=False)),
                ('four_g', models.BooleanField(default=True)),
                ('VoLTE', models.BooleanField(default=True)),
                ('three_g', models.BooleanField(default=True)),
                ('two_g', models.BooleanField(default=True)),
                ('mobileConnectivityDetails', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobile_connectivity_details', to='smartphones.mobileconnectivity')),
            ],
        ),
    ]
