from django.db import models


class BrandName(models.Model):
    brand_name = models.CharField(max_length=30, unique=True)
    brand_name_url = models.SlugField(max_length=30)
    brand_logo = models.ImageField(upload_to='brand-logo/', blank=True, null=True)

    def __str__(self):
        return self.brand_name


class MobileName(models.Model):
    PHONE_TYPE = (
        ('SMARTPHONE', 'Smartphone'),
        ('TABLET', 'Tablet'),
    )
    brandName = models.ForeignKey(BrandName, on_delete=models.CASCADE,)
    mobile_name = models.CharField(max_length=50)
    mobile_name_url = models.SlugField(max_length=50)
    mobile_image = models.ImageField(upload_to='mobile_image/')
    phone_type = models.CharField(max_length=20, choices=PHONE_TYPE, default='Smartphone')

    def __str__(self):
        return self.brandName.brand_name + ' ' + self.mobile_name


class MobileGeneral(models.Model):
    STATUS = (
        ('Upcoming', 'Upcoming'),
        ('Available', 'Available'),
        ('not available', 'not available'),
        ('Rumored', 'Rumored'),
    )
    OS_CHOICES = (
        ('ANDROID', 'Android'),
        ('IOS', 'ios'),
    )
    slot_choice = (
        ('Dual SIM(2) + Dedicated Memory Card Slot', 'Dual SIM(2) + Dedicated Memory Card Slot'),
        ('Dual SIM(2) (One SIM slot + one hybrid SIM slot)', 'Dual SIM(2) (One SIM slot + one hybrid SIM slot)'),
        ('One SIM slot + one e-SIM slot', 'One SIM slot + one e-SIM slot'),
        ('Dual SIM(2)', 'Dual SIM(2)'),
        ('Single SIM', 'Single SIM'),
        ('Other', 'Other'),
    )
    release_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    os = models.CharField(max_length=10, choices=OS_CHOICES)
    os_version = models.CharField(max_length=20, null=True, blank=True)
    UI_version = models.CharField(max_length=50, null=True, blank=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    is_available = models.BooleanField(max_length=None, default=True)
    status = models.CharField(max_length=15, choices=STATUS, default='Available')
    dimensions = models.CharField(max_length=50, default='77 mm x 77 mm x  77 mm')
    weight = models.FloatField()
    slots = models.CharField(max_length=200, choices=slot_choice, default='Dual SIM(2) + Dedicated Memory Card Slot')

    # def __str__(self):
    #     return self.mobile_general.mobileNames.brandName.brand_name + ' ' + self.mobile_general.mobileNames.mobile_name


class MobilePerformance(models.Model):
    PROCESSOR = (
        ('Qualcomm', 'Qualcomm'),
        ('MediaTek', 'MediaTek'),
        ('Apple', 'Apple'),
        ('HiSilicon', 'HiSilicon'),
        ('Samsung', 'Samsung'),
        ('Google', 'Google'),
    )
    ram = models.PositiveIntegerField()
    processor = models.CharField(max_length=50)
    processor_company = models.CharField(max_length=50, choices=PROCESSOR)
    clock_speed = models.FloatField(blank=True, null=True)

    # def __str__(self):
    #     return self.mobile_performance.mobileNames.brandName.brand_name + ' ' + self.mobile_performance.mobileNames.mobile_name


class MobileStorage(models.Model):
    SIM_SLOT = (
        ('Dedicated Slot', 'DEDICATED SLOT'),
        ('Hybrid Slot', 'HYBRID SLOT'),
    )
    device_storage = models.PositiveIntegerField()
    expandable_memory = models.BooleanField(default=True)
    sim_slot_type = models.CharField(blank=True, null=True, max_length=50, choices=SIM_SLOT, default='Dedicated Slot')
    expandable_memory_capacity = models.IntegerField(blank=True, null=True)
    OTG_support = models.BooleanField(blank=True, null=True, default=True)

    # def __str__(self):
    #     return self.mobile_storage.mobileNames.brandName.brand_name + ' ' + self.mobile_storage.mobileNames.mobile_name


class MobileCamera(models.Model):
    primary_camera = models.IntegerField()
    primary_camera_str = models.CharField(max_length=501)
    primary_camera_features = models.CharField(max_length=1200, blank=True, null=True)
    secondary_camera = models.IntegerField()
    secondary_camera_str = models.CharField(max_length=50)
    secondary_camera_features = models.CharField(max_length=1000, blank=True, null=True)

    # def __str__(self):
    #     return self.mobile_camera.mobileNames.brandName.brand_name + ' ' + self.mobile_camera.mobileNames.mobile_name


class MobileBattery(models.Model):
    BATTERY_TYPE_CHOICES = (
        ('LI-ION', 'Li-ion'),
        ('LI-POLY', 'Li-poly'),
    )
    battery_capacity = models.IntegerField()
    battery_type = models.CharField(max_length=10, choices=BATTERY_TYPE_CHOICES, blank=True, null=True)
    fast_charger = models.BooleanField(default=True, blank=True, null=True)
    fast_charging = models.CharField(max_length=200, blank=True, null=True)
    replaceable = models.BooleanField(default=False, blank=True, null=True)
    wireless_charger = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.mobile_battery.mobileNames.brandName.brand_name + ' ' + self.mobile_battery.mobileNames.mobile_name


class MobileDisplay(models.Model):
    screen_size = models.FloatField()
    resolution = models.CharField(max_length=50)
    resolution_type = models.CharField(max_length=50, blank=True, null=True)
    GPU = models.CharField(max_length=50, blank=True, null=True)
    display_type = models.CharField(max_length=100)
    display_features = models.CharField(max_length=700, blank=True, null=True)

    # def __str__(self):
    #     return self.mobile_display.mobileNames.brandName.brand_name + ' ' + self.mobile_display.mobileNames.mobile_name


class MobileConnectivity(models.Model):
    SAR_value = models.CharField(max_length=100, blank=True, null=True)
    wi_fi = models.CharField(max_length=100, blank=True, null=True)
    bluetooth = models.CharField(max_length=100, blank=True, null=True, default='v5.0')
    GPS = models.BooleanField(default=True)
    audio_jack = models.CharField(max_length=30, blank=True, null=True, default='3.5 mm')
    USB_type_c = models.BooleanField(blank=True, null=True, default=True)

    # def __str__(self):
    #     return self.mobile_connectivity.mobileNames.brandName.brand_name + ' ' + self.mobile_connectivity.mobileNames.mobile_name


class MobileConnectivityDetails(models.Model):
    SIM_TYPE = (
        ('NANO', 'Nano'),
        ('MICRO', 'Micro'),
        ('STANDARD', 'Standard'),
        ('eSIM', 'eSIM'),
    )
    SIM_CHOICES = (
        ('SIM 1', 'SIM 1'),
        ('SIM 2', 'SIM 2'),
        ('SIM 3', 'SIM 3'),
    )
    sim_name = models.CharField(max_length=10, choices=SIM_CHOICES)
    sim_type = models.CharField(max_length=20, choices=SIM_TYPE, default='NANO')
    hybrid_slot = models.BooleanField(default=False)
    five_g = models.BooleanField(default=False)
    four_g = models.BooleanField(default=True)
    VoLTE = models.BooleanField(default=True)
    three_g = models.BooleanField(default=True)
    two_g = models.BooleanField(default=True)
    mobileConnectivityDetails = models.ForeignKey(MobileConnectivity, on_delete=models.CASCADE, blank=True, null=True,
                                                  related_name='mobile_connectivity_details')

    def __str__(self):
        return self.sim_name


class MobileSensor(models.Model):
    FINGER_CHOICES = (
        ('SIDE', 'Side'),
        ('REAR', 'REAR'),
        ('FRONTSIDE', 'Front Side'),
        ('IN-DISPLAY', 'in-display'),
    )
    fingerprint_sensor = models.BooleanField(default=True)
    fingerprint_position = models.CharField(max_length=20, choices=FINGER_CHOICES, blank=True, null=True)
    other_sensor = models.CharField(max_length=300)

    # def __str__(self):
    #     return self.mobile_sensor.mobileNames.brandName.brand_name + ' ' + self.mobile_sensor.mobileNames.mobile_name


class OtherFeature(models.Model):
    other_Feature = models.CharField(max_length=1000, blank=True, null=True)
    in_the_box = models.CharField(max_length=300, blank=True, null=True)
    warranty = models.CharField(max_length=300, blank=True, null=True)
    mobile_color = models.CharField(max_length=100, blank=True, null=True)

    # def __str__(self):
    #     return self.mobile_other.mobileNames.brandName.brand_name + ' ' + self.mobile_other.mobileNames.mobile_name


class OnlinePrice(models.Model):
    flipkart = models.PositiveIntegerField(blank=True, null=True)
    flipkart_URL = models.URLField(max_length=200, blank=True, null=True)
    amazon = models.PositiveIntegerField(blank=True, null=True)
    amazon_URL = models.URLField(max_length=200, blank=True, null=True)
    tata_cliq = models.PositiveIntegerField(blank=True, null=True)
    tata_cliq_URL = models.URLField(max_length=200, blank=True, null=True)
    reliance_digital = models.PositiveIntegerField(blank=True, null=True)
    reliance_digital_URL = models.URLField(max_length=200, blank=True, null=True)
    mi_store = models.PositiveIntegerField(blank=True, null=True)
    mi_store_URL = models.URLField(max_length=200, blank=True, null=True)
    samsung = models.PositiveIntegerField(blank=True, null=True)
    samsung_URL = models.URLField(max_length=200, blank=True, null=True)
    vivo = models.PositiveIntegerField(blank=True, null=True)
    vivo_URL = models.URLField(max_length=200, blank=True, null=True)
    realme = models.PositiveIntegerField(blank=True, null=True)
    realme_URL = models.URLField(max_length=200, blank=True, null=True)

    # def __str__(self):
    #     return self.mobile_price.mobileNames.brandName.brand_name + ' ' + self.mobile_price.mobileNames.mobile_name


class MobileVariant(models.Model):
    mobileNames = models.ForeignKey(MobileName, on_delete=models.CASCADE, related_name='mobile_Variant')
    mobile_variants = models.CharField(max_length=50, default='1 GB RAM, 16 GB Storage')
    mobile_variants_url = models.SlugField(max_length=50, default='1-gb-ram-16-gb-storage')
    mobile_url_themes_name = models.CharField(max_length=50, default='brand+name+variant')
    image_credit = models.URLField(max_length=200, default='https://www.gadget4india.com/aboutus/')

    mobileGeneral = models.OneToOneField(MobileGeneral, on_delete=models.CASCADE, blank=True, null=True, related_name='mobile_general')
    mobilePerformance = models.OneToOneField(MobilePerformance, on_delete=models.CASCADE, blank=True, null=True, related_name='mobile_performance')
    mobileStorage = models.OneToOneField(MobileStorage, on_delete=models.CASCADE, blank=True, null=True, related_name='mobile_storage')
    mobileCamera = models.OneToOneField(MobileCamera, on_delete=models.CASCADE, blank=True, null=True, related_name='mobile_camera')
    mobileBattery = models.OneToOneField(MobileBattery, on_delete=models.CASCADE, blank=True, null=True, related_name='mobile_battery')
    mobileDisplay = models.OneToOneField(MobileDisplay, on_delete=models.CASCADE, blank=True, null=True, related_name='mobile_display')
    mobileSensor = models.OneToOneField(MobileSensor, on_delete=models.CASCADE, blank=True, null=True, related_name='mobile_sensor')
    otherFeature = models.OneToOneField(OtherFeature, on_delete=models.CASCADE, blank=True, null=True, related_name='mobile_other')
    mobileConnectivity = models.OneToOneField(MobileConnectivity, on_delete=models.CASCADE, blank=True, null=True, related_name='mobile_connectivity')
    price_variant = models.OneToOneField(OnlinePrice, on_delete=models.CASCADE, blank=True, null=True, related_name='mobile_price')

    def __str__(self):
        return self.mobileNames.mobile_name


class VariantImage(models.Model):
    variantImage = models.ForeignKey(MobileVariant, on_delete=models.CASCADE, blank=True, null=True,
                                     related_name='variant_Image')
    variant_image = models.ImageField(upload_to='variant_image/')

    def __str__(self):
        return str(self.variant_image)
