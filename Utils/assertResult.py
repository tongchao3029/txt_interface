import traceback




def assertResult(assert_keyword,response):
    try:
        assert assert_keyword in response.text
        return True
    except Exception as e:
        print(e)
        return False