from selene import browser, have


def test_1():
    browser.open('https://market.yandex.ru')
    browser.element('[name="text"]').type('Яндекс фабрика')
    browser.element('[data-zone-name="suggestItem"]').click()
    browser.element('[id="/content/header/header/sinsIdentity"]').should(have.text('Яндекс Фабрика'))


def test_2():
    browser.open('https://market.yandex.ru/cc/8oYR3e')
    browser.element('[class="ds-flex ds-flex_jc_sb ds-flex_ai_c _14a6f"]').click()
    #browser.element('["class="D4z0j"]').click()
    browser.element('[id="/content/header/header/sinsIdentity"]').should(have.text('ZARINA'))

#def test_3():

