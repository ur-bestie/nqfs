from myapp.models import settings, KYCInfo

def sett(request):
   ss = settings.objects.filter().first
   return {'ss':ss}

def kyc_processor(request):
    try:
      kIF = KYCInfo.objects.filter(user=request.user)
    except:
      KYCInfo.DoesNotExist
      kIF = None
    return {'kIF':kIF}