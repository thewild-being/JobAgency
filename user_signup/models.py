from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

# fundamentally you can extend the user model wherever you want. (not sure here)
# I'm doing it here because, to me, this is where it makes more sense

# devo organizzare e cambiare il form, per farlo devo cereare un nuovo file chiamato form,
# importare le cose li dentro e poi modificarle nella class meta (?)
# devo solo aggiungere un attribute al User class che è is_staff = True / False

# devo anche aggiungere request.user.is_authenticated property in your handler
# questo forse va nel log-in tho, why tho? devo fare il check della authentication nel view/model della home
# alla fine è li che devo filtrare gli utenti.

""" to reference the ForeignKey(django.contrib.auth.User) you should import by writing from django.conf import 
    settings" and then write "ForeignKey(settings.AUTH_USER_MODEL, ...)" for author. """




