from smtplib import SMTP


def send_email(to_email="manas.m22@gmail.com", subject="Testing", message="HELLO !!!"):
    from_email = "laozimishra@gmail.com"
    from_pass = "R@ndumP@ssword"
    email_message =f'''from: {from_email}
to: {to_email}
subject: {subject}

{message}
    '''
    with SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(from_email, from_pass)
        smtp.sendmail(
            from_addr=from_email,
            to_addrs=to_email,
            msg=email_message.encode("utf-8")
        )


if __name__ == "__main__":
    
    divya_email = "f20170727@pilani.bits-pilani.ac.in"
    lakshya_email = "f20170630@pilani.bits-pilani.ac.in"
    manas_email = "f20170546@pilani.bits-pilani.ac.in"
    # send_email()
    message = """
    You bro !!!
    Kya kar ra ??? React padhi kya kuchh ???
    Btw ye mene python se mail bheji hai !!!
    😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎
    """
    send_email(message=message, to_email=manas_email, subject="Testing")
