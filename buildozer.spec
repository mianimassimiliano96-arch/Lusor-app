[app]
title = Lusor
package.name = lusor
package.domain = org.lusor.app
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv
version = 1.0.0
requirements = python3,kivy==2.3.1,openpyxl,plyer
orientation = portrait
osx.package_name = Lusor
osx.bundle_identifier = org.lusor.app
osx.category = public.app-category.business
presplash.color = #2F5496
icon = icon.png
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 0

[android]
android.api = 34
android.ndk = 27b
android.sdk = 34
android.build_tools = 34.0.0
android.minapi = 26
android.permissions = CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,INTERNET
android.arch = arm64-v8a
android.accept_sdk_license = True
android.enable_androidx = True
android.allow_backup = True
android.wakelock = False
android.copy_libs = 1
android.manifest_merger = True
android.add_src =
android.gradle_dependencies =
android.manifest = %(source.dir)s/AndroidManifest.xml

[requirements]
# System libraries
android.add_src =
