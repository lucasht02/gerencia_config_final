from src.notification import Notification

def test_send_email():
    n = Notification("destino@example.com")
    resp = n.send_email("Oi", "Corpo")
    assert "Email sent to destino@example.com with subject 'Oi'" == resp

def test_send_sms():
    n = Notification("+5511999999999")
    resp = n.send_sms("Olá")
    assert "SMS sent to +5511999999999: 'Olá'" == resp