# -*- mode: python ; coding: utf-8 -*-
finder privkey
(0xED44e4F02904a28a7A28E05dF78BeE02626435D1)

a = Analysis(
    ['finder.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['eth_typing'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='finder',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
