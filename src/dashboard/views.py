# src/dashboard/views.py
from django.shortcuts import redirect
from django.http import HttpResponse


def dashboard_webpage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        error = request.GET.get("error")
        if error:
            return HttpResponse(f"is: {error}")

        return redirect("/auth/google/login/")

    return HttpResponse(f"Hello {request.user.username}")
