from abc import ABC, abstractmethod


# Уявіть, що у вас є система, яка відповідає за відправлення повідомлень різним користувачам. Повідомлення можуть бути надіслані електронною поштою, через SMS-повідомлення або через месенджери. Наше завдання - створити гнучку систему, яка дозволяє легко додавати нові методи доставки повідомлень, дотримуючись принципу інверсії залежностей.
# Залежності всередині системи мають бути спрямовані абстракції, а чи не на конкретні реалізації. Давайте реалізуємо це, створивши абстрактний інтерфейс Notifier, який представлятиме метод send_notification(). Потім ми можемо створити різні класи, що реалізують цей інтерфейс, для надсилання повідомлень електронною поштою, через SMS або через месенджери. Вся логіка надсилання повідомлень залежатиме від абстракції Notifier, а не від конкретних реалізацій.
# Кожен клас повинен мати лише одну причину зміни. Давайте розділимо відповідальність на два класи: NotificationService, який використовуватиме інтерфейс Notifier для надсилання повідомлень, і класи, що реалізують конкретні методи доставки повідомлень, такі як EmailNotifier, SMSNotifier і MessengerNotifier. Таким чином, NotificationService буде відповідальним лише за керування повідомленнями, а класи доставки будуть відповідальні лише за свою специфіку відправки.
# Це дозволить нам створити гнучку систему, в якій ми можемо легко додавати нові методи доставки повідомлень, не торкаючись існуючого коду. Ми зможемо легко перемикатися між різними методами доставки, просто замінюючи реалізацію інтерфейсу Notifier. Також це дозволить нам легко тестувати нашу систему, використовуючи макети (mocks) або підробки (stubs) для інтерфейсу Notifier.


class Notifier(ABC):
    @abstractmethod
    def send_notification(self, notification):
        pass

class EmailNotifier(Notifier):
    def send_notification(self, notification):
        print(f'Notification "{notification}" was sent via email.')

class SMSNotifier(Notifier):
    def send_notification(self, notification):
        print(f'Notification "{notification}" was sent via sms.')

class MessengerNotifier(Notifier):
    def send_notification(self, notification):
        print(f'Notification "{notification}" was sent via messenger.')


class NotificationService:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def notify(self, notification):
        self.notifier.send_notification(notification)


email_notifier = EmailNotifier()
sms_notifier = SMSNotifier()
mess_notifier = MessengerNotifier()

email_service = NotificationService(email_notifier)
email_service.notify('The lesson will start at 6 PM. Join by the link: https://teams.microsoft.com/')

sms_service = NotificationService(sms_notifier)
sms_service.notify('Your order #23875827 was delivered.')

mess_service = NotificationService(mess_notifier)
mess_service.notify('Your photo got 3 new likes.')