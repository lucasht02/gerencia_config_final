class Notification:
    def __init__(self, recipient):
        self.recipient = recipient

    def send_email(self, subject, body):
        # placeholder para integração real
        return f"Email sent to {self.recipient} with subject '{subject}'"

    def send_sms(self, message):
        # placeholder para integração real
        return f"SMS sent to {self.recipient}: '{message}'"