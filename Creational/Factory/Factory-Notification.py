# Notification Interface
class Notification:
    def send(self, message):
        pass


class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS Notification with message {message}")


class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending Email Notification with message {message}")


class PushNotification(Notification):
    def send(self, message):
        print(f"Sending Push Notification with message {message}")


class NotificationFactory:
    @staticmethod
    def create_notification(notification_type):
        if notification_type == 'SMS':
            return SMSNotification()
        elif notification_type == 'Email':
            return EmailNotification()
        elif notification_type == 'Push':
            return PushNotification()
        raise ValueError("Unknown notification type")


# Usage
notification = NotificationFactory.create_notification('SMS')
notification.send('Testing SMS message')
