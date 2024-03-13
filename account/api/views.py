from rest_framework import status
from rest_framework.response import Response

from account.models import Account

from account.api.serializers import AccountSerializer
from rest_framework.generics import ListAPIView

class AccountListAPIView(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer