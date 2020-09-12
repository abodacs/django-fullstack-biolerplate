from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework_simplejwt.tokens import RefreshToken


class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request):
        # find all tokens by user and blacklists them, forcing them to log out.
        try:
            tokens = OutstandingToken.objects.filter(user=request.user)
            for token in tokens:
                token = RefreshToken(token.token)
                token.blacklist()
        except Exception as e:
            print(str(e))
            token = RefreshToken(request.data.refresh_token)
            token.blacklist()
        return Response(
            status=status.HTTP_205_RESET_CONTENT
        )  # 204 means no content, 205 means no content and refresh

    def post(self, request, *args, **kwargs):
        return self.logout_current_session(request)

    def logout_current_session(self, request, *args, **kwargs):
        # Post is for logging out in current browser
        try:
            refresh_token = request.data["refresh_token"]
            token = OutstandingToken.objects.get(token=refresh_token)
            if token.user == request.user:
                BlacklistedToken.objects.create(token=token)
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST)
