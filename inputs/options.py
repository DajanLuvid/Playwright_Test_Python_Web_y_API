
import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()

        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        await page.set_viewport_size({"width": 1400, "height": 1000})
        await page.goto("https://demoqa.com/select-menu")

        # Realiza un desplazamiento vertical
        await page.evaluate("window.scrollBy(0, 500)")

        # Actions en STANDARD MULTISELECT
        await page.select_option('select#cars', ['volvo', 'saab', 'audi'])
        await page.screenshot(path="screenshots/options.png")

        # Espera después del clic
        await page.wait_for_timeout(2000)

        # Stopping Tracing
        await context.tracing.stop(path="logs/trace_options.zip")

        # Closing browser
        await browser.close()

asyncio.run(main())
