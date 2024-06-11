# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

pathex = [
    'C:/Users/Administrator/PycharmProjects/yolov5'
]

hiddenimports = ['models.yolo',
'utils',
'utils.general',
'models',
'utils.aws',
'utils.docker',
'utils.flask_rest_api',
'utils.google_app_engine',
'utils.loggers',
'utils.segment',
'utils.loggers.clearml',
'utils.loggers.comet',
'utils.loggers.wandb',
'utils.segment',
'models.hub',
'segment',
'apex_yolov5',
'apex_yolov5.socket'
]

a = Analysis(
    ['apex_yolov5_main.py'],
    pathex=pathex,
    binaries=[(r'./utils/general.pyc',r'./utils')],
    data=[(r'./config/global_config.json',r'./config')],
    hiddenimports=['models.yolo'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=['setenv.py'],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ag',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='./images/ag.ico'
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.data,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ag'
)
