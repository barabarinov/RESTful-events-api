import logging
from django.core.mail import send_mail

from event.models import Event
from user.models import User
from django.conf import settings

logger = logging.getLogger(__name__)


def send_event_registration_email(user: User, event: Event) -> None:
    """
    Sends an email notification to a user after successful registration for an event.
    """
    try:
        send_mail(
            subject=f"You have successfully registered to {event.title}",
            message=(
                f"""
                    Hi, {user.username}!
                    
                    Congratulations! You have successfully registered for the event \"{event.title}\".
                    
                    📅 Date & Time: {event.datetime.strftime('%Y-%m-%d %H:%M:%S')}.
                    📍 Location: {event.location}
                    📝 Description: {event.description}
                    
                    🙏🏼 Thank you for choosing our service!
                    
                    Best regards,
                    The EventManager Team
                """
            ),
            from_email=settings.FROM_EMAIL,
            recipient_list=[user.email],
        )
        logger.info(f"🟢 Email sent to user: {user.email}.")
    except Exception as e:
        logger.error(f"🔴 Failed to send email to {user.email}. Error: {e}")
