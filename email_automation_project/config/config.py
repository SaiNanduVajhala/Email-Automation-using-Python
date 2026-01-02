# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

load_dotenv()

def get_config(provider='gmail'):
    providers = {
        'gmail': {
            'smtp_server': 'smtp.gmail.com',
            'smtp_port': 587,
            'use_tls': True
        },
        'outlook': {
            'smtp_server': 'smtp-mail.outlook.com', 
            'smtp_port': 587,
            'use_tls': True
        }
    }
    cfg = providers.get(provider, providers['gmail']).copy()
    cfg['SENDER_EMAIL'] = os.getenv('SENDER_EMAIL')
    cfg['SENDER_PASSWORD'] = os.getenv('SENDER_PASSWORD')
    return cfg
