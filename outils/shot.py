import sys
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page(viewport={'width':1400,'height':933},device_scale_factor=1)
    pg.goto('file://'+sys.argv[1]); pg.wait_for_timeout(300)
    pg.screenshot(path=sys.argv[2],type='jpeg',quality=90)
    b.close()
