from django.db import models


class Rating(models.Model):
    one = models.PositiveIntegerField(default=0, null=True, blank=True)
    two = models.PositiveIntegerField(default=0, null=True, blank=True)
    three = models.PositiveIntegerField(default=0, null=True, blank=True)
    four = models.PositiveIntegerField(default=0, null=True, blank=True)
    five = models.PositiveIntegerField(default=0, null=True, blank=True)

    def __str__(self):
        # Extract all rating values and return max key.
        # Reverse this Dict if there is a tie and you want the last key.
        rating_list = {
            '1': self.one,
            '2': self.two,
            '3': self.three,
            '4': self.four,
            '5': self.five
        }
        return str(max(rating_list, key=rating_list.get))


class UserMessage(models.Model):
    object_id = models.CharField(max_length=50, primary_key=True, default='')

    show_id = models.CharField(max_length=50, default='')
    name = models.CharField(max_length=20, null=True, blank=True)
    message = models.CharField(max_length=100)
    rating = models.ForeignKey(
        Rating, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'user_message'
        ordering = ('-object_id',)

    def __str__(self):
        # Return a string representation of the message
        return f"Message ID: {self.object_id}, Show ID: {self.show_id}, User: {self.name}"
