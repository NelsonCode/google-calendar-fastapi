from os import path
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# SI MODIFICA EL SCOPE ELIMINE EL ARCHIVO TOKEN.TXT
SCOPES = ['https://www.googleapis.com/auth/calendar.events',
          'https://www.googleapis.com/auth/calendar']

# EL ARCHIVO TOKEN.TXT ALMACENA LOS TOKENS DE ACTUALIZACIÓN Y ACCESO DEL USUARIO

def get_crendetials_google():
    # ABREN EL NAVEGADOR PARA AUTORIZAR
    flow = InstalledAppFlow.from_client_secrets_file("creds.json", SCOPES)
    creds = flow.run_local_server(port=0)

    # GUARDAMOS LAS CREDENTIALS
    pickle.dump(creds, open("token.txt", "wb"))
    return creds

def get_calendar_service():
    creds = None
    if path.exists("token.txt"):
        creds = pickle.load(open("token.txt", "rb"))
    # SI EXPIRO REFRESCAMOS LAS CREDENCIALES
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            creds = get_crendetials_google()
    service = build("calendar", "v3", credentials=creds)
    return service