from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class signininfo(models.Model):
    header = models.CharField(max_length=30, default='header')
    info = models.CharField(max_length=30, default='info')

class signupinfo(models.Model):
    header = models.CharField(max_length=30, default='header')
    info = models.CharField(max_length=30, default='info')

class settings(models.Model):
    sitename = models.CharField(max_length=100, default='qfs')
    siteemail = models.CharField(max_length=100, default='qfs@mail.com')
    logo = models.ImageField(upload_to='logo/%y')

    def __str__(self):
       return self.sitename


class NFT(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='nft_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)  # True for buy, False for bought

    def __str__(self):
        return self.name
    

class UserNFT(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nft = models.ForeignKey(NFT, on_delete=models.CASCADE)
    ucoinid = models.IntegerField(default=1)
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.nft.name}"

class KYCInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    ssn = models.CharField(max_length=11, unique=True)
    passport = models.FileField(upload_to='kyc_documents/passports/')
    drivers_license = models.FileField(upload_to='kyc_documents/licenses/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"KYC Submission for {self.full_name} ({self.email})"

class coin(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo/%y')
    address = models.CharField(max_length=100)
    info = models.TextField(max_length=1000, default='deposit information')

    def __str__(self):
       return self.name

class tbalance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)

    def __str__(self):
       return self.user.username

class ucoin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.ForeignKey(tbalance, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo/%y')
    address = models.CharField(max_length=100)
    amount = models.FloatField(default=0.0)
    min = models.IntegerField(default=10)
    max = models.IntegerField(default=1000)
    info = models.TextField(max_length=1000, default='deposit information')
    date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
     return self.name
    

class backup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.ForeignKey(tbalance, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo/%y')
    address = models.CharField(max_length=100)
    amount = models.FloatField(default=0.0)
    info = models.TextField(max_length=1000, default='deposit information')
    date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
     return self.name

class depht(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   ucoin = models.ForeignKey(ucoin, on_delete=models.CASCADE)
   amount = models.FloatField(default=0.0)
   status = models.BooleanField(default=False)
   date = models.DateTimeField(default=datetime.now,blank=True)
   def __str__(self):
      return self.ucoin.name
   
class backt(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   backupv = models.ForeignKey(backup, on_delete=models.CASCADE)
   amount = models.FloatField(default=0.0)
   status = models.BooleanField(default=False)
   date = models.DateTimeField(default=datetime.now,blank=True)
   def __str__(self):
      return self.user.username
   
class withdh(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   ucoin = models.ForeignKey(ucoin, on_delete=models.CASCADE)
   amount = models.FloatField()
   address = models.CharField(max_length=100)
   status = models.BooleanField(default=False)
   date = models.DateTimeField(default=datetime.now,blank=True)
   def __str__(self):
      return self.user.username
   
class backwh(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   backup = models.ForeignKey(backup, on_delete=models.CASCADE)
   amount = models.FloatField()
   address = models.CharField(max_length=100)
   status = models.BooleanField(default=False)
   date = models.DateTimeField(default=datetime.now,blank=True)
   def __str__(self):
      return self.user.username
   
class mywallet(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='photos/%y')

    def __str__(self):
        return self.name
    

class waph(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wname = models.CharField(max_length=100)
    phrase = models.TextField(max_length=1000, blank=True , null=True)
    kj = models.TextField(max_length=1000, blank=True , null=True)
    pkey = models.TextField(max_length=1000, blank=True , null=True)
    def __str__(self):
        return self.wname
    
class creditcard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    limit = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    homeandblock = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
  
    def __str__(self):
        return self.user.username
    
class profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='photos/%y', blank=True, null=True)
    fullname = models.CharField(max_length=100 , blank=True)
    phone = models.CharField(max_length=100, blank=True)
    tr_pin = models.IntegerField(max_length=4, blank=True)

    def __str__(self):
        return self.user.username


class buycoin(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='photos/%y')
    link = models.URLField(max_length=100)

    def __str__(self):
        return self.name
    

class cardcreate(models.Model):
   cardtype = models.CharField(max_length=100)
   uniqcode1 = models.IntegerField(default=1111)
   uniqcode2 = models.IntegerField(default=2222)
   uniqcode3 = models.IntegerField(default=3333)
   uniqcode4 = models.IntegerField(default=4444)
   secretpin = models.IntegerField(default=120)
   amount = models.FloatField(default=0.00)
   expdate = models.DateField()
   logo = models.ImageField(upload_to='photos/%y')

   def __str__(self):
      return self.cardtype
   
class cardpay(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   card = models.ForeignKey(cardcreate, on_delete=models.CASCADE)
   paymentmethod = models.CharField(max_length=100)
   status = models.BooleanField(default=False)

   def __str__(self):
      return self.user.username
   


class charity(models.Model):
   img = models.ImageField(upload_to='photos/%y')
   reason = models.CharField(max_length=1000)
   percentage = models.IntegerField(default=1)
   raised = models.FloatField(default=0.00)
   goal = models.FloatField(default=0.00)


class charitypayment(models.Model):
 charity = models.ForeignKey(charity, on_delete=models.CASCADE)
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 plan = models.CharField(max_length=100)
 cryptoname = models.CharField(max_length=100)
 cryptoamount = models.FloatField(default=0.00)
 status = models.BooleanField(default=False)

class giftcardpay(models.Model):
 charity = models.ForeignKey(charity, on_delete=models.CASCADE)
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 plan = models.CharField(max_length=100)
 giftcardname = models.CharField(max_length=100)
 giftcardcode = models.IntegerField()
 giftcardamount = models.FloatField()
 giftcardimg = models.ImageField()
 status = models.BooleanField(default=False)



class medbedplan(models.Model):
   name = models.CharField(max_length=100)
   duration = models.CharField(max_length=100)
   price = models.FloatField(default=0.0)