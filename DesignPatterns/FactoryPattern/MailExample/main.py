from abstract_mail import Mail
from creator_mail import AirMail, LandMail, RailMail

def mail_sender(mail_type: Mail) -> None:		# client
	"""
		Client used to send mail without worring about the type of mail it is
	"""
	mail_type.mail()


if __name__ == "__main__":
	for mail_type in [AirMail(), LandMail(), RailMail()]:
		mail_sender(mail_type)
