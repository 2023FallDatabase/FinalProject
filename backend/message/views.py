from django.shortcuts import render, redirect
from message.models import *
from django.contrib.auth.decorators import login_required
from .forms import UserMessageForm  # Import the form you've created
import random


@login_required
def submitform(request):
    return render(request, 'message/message_form.html')


def showform(request):
    if request.method == 'POST':
        usermessage = UserMessage()
        usermessage.show_id = request.POST.get('show_id', '')
        usermessage.name = request.POST.get('name', '')
        usermessage.message = request.POST.get('message', '')
        usermessage.object_id = str(random.randint(0, 10000)).zfill(5)

        # Get the selected rating value from the form data
        rating_value = request.POST.get('rating', '')

        if rating_value:
            rating, created = Rating.objects.get_or_create(
                rating_value=float(rating_value))
            usermessage.rating = rating

        usermessage.save()

    all_messages = UserMessage.objects.prefetch_related('rating').all()

    for message in all_messages:
        if message.rating:
            message.stars_filled = "★" * int(message.rating.rating_value * 2)
            message.stars_empty = "☆" * \
                (10 - int(message.rating.rating_value * 2))
        else:
            message.stars_filled = ""
            message.stars_empty = "☆" * 10  # Default to 5 empty stars if no rating is set

    return render(request, 'message/message_board.html', {
        'all_messages': all_messages,
    })
