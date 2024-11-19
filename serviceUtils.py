def dateConvert(date):
    # input:25/02/2546 
    # output:2546-02-25 
    d = date[0:2]
    m = date[3:5]
    y = date[-4:]
    newdate = y+"-"+m+"-"+d
    return newdate

def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def openManyWebsite():
    import webbrowser
    for x in range(35, 71):
        website = "https://someweb?page=" + str(x)
        print(website)
        webbrowser.open(website, "chrome")

def genshin_cal_mat():
    print("1.Gold\n2.Purple\n3.Blue")
    color = str(input("Enter color of item : "))
    amonng = int(input("Enter number of item you want : "))
    have = int(input("Enter number of item you have : "))
    print(">>---------------------<<")
    if have > 0:
        amonng = amonng - have

    purple = 0
    blue = 0
    green = 0

    if color == "1":
        purple = amonng * 3
        blue = purple * 3
        green = blue * 3
    elif color == "2":
        blue = amonng * 3
        green = blue * 3
    elif color == "3":
        green = amonng * 3

    if purple != 0:
        print(">> purple", purple)
    if blue != 0:
        print(">> blue", blue)
    if green != 0:
        print(">> green",green)
    print(">>---------------------<<")

def lingtonumber():
    onebox = ['Begin','Ignite','Open', 'Activate','Engage', 'Initiate', 'Operate','On']
    with open('linguisBinary.txt' , 'r') as file:
        for line in file:
            word = line.strip()
            if word in onebox:
                print("1", end ="")
            else:
                print("0", end ="")

def ctf_bypass_150_captcha():
    '''
    answer of captcha is a filename of captcha image
    '''
    import requests
    import re

    session = requests.Session()

    captcha_url = "http://xxx"
    submit_url = "http://xxx/submit"

    for _ in range(150):
        # Fetch the CAPTCHA page to get the CAPTCHA image URL
        captcha_response = session.get(captcha_url)

        # Extract the filename of the CAPTCHA image from the HTML
        match = re.search(r'<img src="([^"]+)"', captcha_response.text)
        if match:
            url_path_pic = match.group(1)
            ans = url_path_pic.split('/')[-1].split('.')[0]  # Extract the answer from the filename
            print(f"Extracted CAPTCHA answer: {ans}")

            # Prepare data for submission
            data = {"captcha": ans}

            # Submit the CAPTCHA answer
            response = session.post(submit_url, data=data)
            print(response.text)
        else:
            print("Failed to find CAPTCHA image URL.")

def ctf_bypass_150_captcha_but_selenium():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from webdriver_manager.chrome import ChromeDriverManager
    import time

    # Initialize ChromeDriver using Service with ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get("http://xxx/")  # replace with the actual URL of the CAPTCHA page

    # Define the number of attempts
    attempts = 150

    # Wait for elements to load
    wait = WebDriverWait(driver, 10)

    try:
        for i in range(attempts):
            # Wait and locate the CAPTCHA image element
            captcha_img = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))

            # Get the CAPTCHA image name from the 'src' attribute without the '.png' extension
            captcha_src = captcha_img.get_attribute("src")
            captcha_code = captcha_src.split('/')[-1].replace('.png', '')  # Remove '.png' to get just the name

            # Locate the input box and submit button
            captcha_input = wait.until(EC.presence_of_element_located((By.NAME, "captcha")))
            submit_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))

            # Clear any existing text in the input box, enter the CAPTCHA code, and click submit
            captcha_input.clear()
            captcha_input.send_keys(captcha_code)

            # Click submit
            submit_button.click()

            # Optional: add a slight delay to prevent overloading the server
            time.sleep(0.5)  # Adjust as necessary

    except Exception as e:
        print("An error occurred:", e)

    finally:
        time.sleep(10)
        driver.quit()

def read_wordlist(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def check_path(base_url, path):
    url = f"{base_url}/{path}"
    response = requests.get(url)
    return response.status_code, url

def search_hidden_paths(base_url, wordlist_path):
    paths = read_wordlist(wordlist_path)
    found_paths = []
    for path in paths:
        status_code, url = check_path(base_url, path)
        if status_code == 200:
            print(f"Found: {url}")
            found_paths.append(url)
        else:
            print(f"Not found: {url} (Status code: {status_code})")

    return found_paths
'''

dateConvert(date) 
is_square(n)
openManyWebsite()
genshin_cal_mat()
lingtonumber()
ctf_bypass_150_captcha()
ctf_bypass_150_captcha_but_selenium()
read_wordlist(file_path)
check_path(base_url, path)
search_hidden_paths(base_url, wordlist_path)
'''