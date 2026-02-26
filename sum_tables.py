import asyncio
from playwright.async_api import async_playwright

seeds = list(range(53, 63))

async def main():

    total_sum = 0

    async with async_playwright() as p:

        browser = await p.chromium.launch()
        page = await browser.new_page()

        for seed in seeds:

            url = f"https://sanand0.github.io/tdsdata/playwright/seed/{seed}.html"

            await page.goto(url)

            numbers = await page.eval_on_selector_all(
                "table td",
                "els => els.map(e => parseFloat(e.innerText)).filter(n => !isNaN(n))"
            )

            total_sum += sum(numbers)

        await browser.close()

        # ✅ ONLY NUMBER PRINT
        print(int(total_sum))

asyncio.run(main())
