CONFIG = {
    'mode': 'django',
    'environment': {
        'PYTHONPATH': '/home/box/web/ask/askenv/bin/',
    },
    'working_dir': '/home/box/web/ask/',
    # 'user': 'www-data',
    # 'group': 'www-data',
    'args': (
        '--bind=0.0.0.0:8000',
        '--workers=2',
        # '--worker-class=egg:gunicorn#sync',
        # '--timeout=30',
        'ask.wsgi',
    ),
}
