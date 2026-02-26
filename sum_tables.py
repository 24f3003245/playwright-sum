import asyncio
from playwright.async_api import async_playwright

async def main():

    total = 0

    async with async_playwright() as p:

        browser = await p.chromium.launch()
        page = await browser.new_page()

        for seed in range(53, 63):

            url = f"https://sanand0.github.io/tdsdata/js_table/?seed={seed}"

            await page.goto(url)

            values = await page.locator("table td").all_inner_texts()

            for v in values:

                try:
                    total += int(v)
                except:
                    pass

        await browser.close()

    print(total, flush=True)

asyncio.run(main())
