from playwright.sync_api import sync_playwright



with sync_playwright() as p:
    def waitTimeout(seconds):
        pageBling.wait_for_timeout(seconds)


    browser = p.chromium.launch(headless=False)
    pageBling = browser.new_page()
    pageBling.goto("https://www.bling.com.br/contas.receber.php")
    waitTimeout(1000)
    pageBling.fill("input[id='username']", "assuntosdiversos1998@gmail.com") # Lembrar sempre de mascarar a senha e o e-mail pro GitHub...
    waitTimeout(1000)
    pageBling.fill("input[id='senha']", "Tfm1234@")
    waitTimeout(1000)
    pageBling.click("button[name='enviar']")
    waitTimeout(1000)
    warning_full_memory = pageBling.locator("xpath=//html/body/div[5]/div[1]/div/i")
    if warning_full_memory:    
        warning_full_memory.click()
        
    waitTimeout(50000)