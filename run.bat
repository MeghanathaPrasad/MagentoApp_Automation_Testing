pytest -v -m "Home_page" --html=Reports\report.html testCases --browser chrome
pytest -v -m "Login" --html=Reports\report.html testCases --browser chrome
pytest -v -m "Create_new" --html=Reports\report.html testCases --browser chrome
pytest -v -m "add_product" --html=Reports\report.html testCases --browser chrome
pytest -v -m "added_product" --html=Reports\report.html testCases --browser chrome
