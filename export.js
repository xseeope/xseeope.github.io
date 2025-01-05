const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    // 打开 Docsify 页面
    await page.goto('http://127.0.0.1:5500/#/papers/Information/Shannon48?id=a-mathematical-theory-of-communication', { waitUntil: 'networkidle2' });

    // 添加自定义样式隐藏导航栏
    await page.addStyleTag({
        content: `
            .sidebar { display: none !important; }
            .content { margin-left: 0 !important; width: 100% !important; }
        `,
    });

    // 生成 PDF
    await page.pdf({
        path: 'output.pdf',
        format: 'A4',
        printBackground: true,
    });

    await browser.close();
})();
