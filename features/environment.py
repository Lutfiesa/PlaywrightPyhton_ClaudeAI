"""
Environment setup untuk Behave + Playwright
File ini berisi hooks yang akan dijalankan sebelum dan sesudah test
"""
from playwright.sync_api import sync_playwright
import os
from datetime import datetime
import allure
from allure_commons.types import AttachmentType


def before_all(context):
    """Hook yang dijalankan sekali sebelum semua test"""
    context.playwright = sync_playwright().start()

    # Konfigurasi browser (dapat diubah sesuai kebutuhan)
    browser_type = os.getenv('BROWSER', 'chromium')  # chromium, firefox, atau webkit

    if browser_type == 'chromium':
        context.browser = context.playwright.chromium.launch(headless=False, slow_mo=500)
    elif browser_type == 'firefox':
        context.browser = context.playwright.firefox.launch(headless=False, slow_mo=500)
    elif browser_type == 'webkit':
        context.browser = context.playwright.webkit.launch(headless=False, slow_mo=500)
    else:
        context.browser = context.playwright.chromium.launch(headless=False, slow_mo=500)

    # Buat folder screenshots jika belum ada
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')


def before_scenario(context, scenario):
    """Hook yang dijalankan sebelum setiap scenario"""
    # Buat context dan page baru untuk setiap scenario
    context.context = context.browser.new_context(
        viewport={'width': 1920, 'height': 1080},
        record_video_dir='videos/' if os.getenv('RECORD_VIDEO', 'false').lower() == 'true' else None
    )

    # Enable tracing untuk debugging
    if os.getenv('TRACE', 'false').lower() == 'true':
        context.context.tracing.start(screenshots=True, snapshots=True, sources=True)

    context.page = context.context.new_page()

    # Set default timeout
    context.page.set_default_timeout(30000)  # 30 detik


def after_scenario(context, scenario):
    """Hook yang dijalankan setelah setiap scenario"""
    # Cek apakah scenario adalah negative case (tag @negative)
    tags_lower = [t.lower() for t in getattr(scenario, "tags", [])]
    is_negative = "negative" in tags_lower

    # Screenshot jika scenario gagal (untuk Allure dan folder screenshots)
    if scenario.status == "failed" or is_negative:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_name = scenario.name.replace(" ", "_")
        screenshot_name = f"screenshots/{safe_name}_{timestamp}.png"

        os.makedirs("screenshots", exist_ok=True)

        # Take screenshot
        screenshot_bytes = context.page.screenshot(
            path=screenshot_name,
            full_page=True
        )
        print(f"Screenshot saved: {screenshot_name}")

        # Attach screenshot ke Allure report
        allure.attach(
            screenshot_bytes,
            name=f"Failed (Negative): {scenario.name}",
            attachment_type=AttachmentType.PNG
        )

    # Save trace jika enabled
    if os.getenv('TRACE', 'false').lower() == 'true':
        trace_name = f"traces/{scenario.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
        if not os.path.exists('traces'):
            os.makedirs('traces')
        context.context.tracing.stop(path=trace_name)

        # Attach trace to Allure report
        with open(trace_name, 'rb') as trace_file:
            allure.attach(
                trace_file.read(),
                name=f"Trace: {scenario.name}",
                attachment_type=AttachmentType.ZIP
            )

    # Close page dan context
    context.page.close()
    context.context.close()


def after_all(context):
    """Hook yang dijalankan sekali setelah semua test selesai"""
    context.browser.close()
    context.playwright.stop()
