from django.db import models


class UserLogin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    utype = models.CharField(max_length=30)


class UserRegistration(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    pincode = models.CharField(max_length=60)
    contact = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)


class BlockChain(models.Model):
    cat_name = models.CharField(max_length=50, null=True)
    product_name = models.CharField(max_length=50, null=True)
    uom = models.CharField(max_length=30,null=True)
    quantity = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    image = models.CharField(max_length=1000, null=True)
    total_stock = models.IntegerField(null=True)


class AddCategory(models.Model):
    cat_name = models.CharField(max_length=50, null=True)



class Cryptocurrency(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    rank = models.IntegerField()
    price_usd = models.DecimalField(max_digits=7, decimal_places=2)
    price_btc = models.DecimalField(max_digits=8, decimal_places=7)
    volume_usd_24h = models.DecimalField(max_digits=14, decimal_places=2)
    market_cap_usd = models.DecimalField(max_digits=14, decimal_places=2)
    available_supply = models.DecimalField(max_digits=20, decimal_places=2)
    total_supply = models.DecimalField(max_digits=20, decimal_places=2)
    max_supply = models.DecimalField(
        max_digits=20, decimal_places=2, null=True, blank=True)
    percent_change_1h = models.DecimalField(max_digits=5, decimal_places=2)
    percent_change_24h = models.DecimalField(max_digits=5, decimal_places=2)
    percent_change_7d = models.DecimalField(max_digits=5, decimal_places=2)
    last_updated = models.DateTimeField()

    class Meta:
        verbose_name = 'Cryptocurrency'
        verbose_name_plural = 'Cryptocurrencies'


class AddPayment(models.Model):
    order_id = models.CharField(max_length=50, null=True)
    user_id = models.CharField(max_length=50, null=True)
    payment_date = models.CharField(max_length=50, null=True)
    paid_amount = models.CharField(max_length=50, null=True)


class AddStock(models.Model):
    pid = models.CharField(max_length=50, null=True)
    stock = models.CharField(max_length=50, null=True)


class AddFeedback(models.Model):
    user_id = models.CharField(max_length=50, null=True)
    about_product = models.CharField(max_length=50, null=True)
    about_service = models.CharField(max_length=50, null=True)
    comments = models.CharField(max_length=50, null=True)


class OtpCode(models.Model):
    otp = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, null=True)
