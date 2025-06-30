# # import requests
# # import urllib.parse
# # from bs4 import BeautifulSoup
# # import re
# # import time

# # # Scrape.do setup
# # token = "ace4669fd83046e39bc55b1e18efc9b8e20b0e51dd7"
# # li_at_cookie = "AQEDAUma_3cFgXFKAAABl7soc38AAAGX3zT3f1YABdF9V475AHOY5J2MZFiYXGNvbDukbDbw8629wKXYh-7bcyifDxu0j-5Lof097VLAIEkyvkXNt-WxUN7NNdwhMUBCFyz4W9HZtKT3TKFOvQ_ibE7Y"  # Replace with your li_at cookie
# # cookies = {"li_at": li_at_cookie}
# # search_url = "https://www.linkedin.com/jobs/search/?keywords=data&location=India"
# # encoded_search_url = urllib.parse.quote(search_url)

# # scrape_url = (
# #     f"http://api.scrape.do/?token={token}"
# #     f"&url={encoded_search_url}"
# #     f"&render=true"
# #     f"&super=true"
# #     f"&geoCode=IN"
# #     f"&wait=5000"
# # )

# # try:
# #     # Fetch the search results page with cookies
# #     response = requests.get(scrape_url, cookies=cookies, timeout=70)
# #     print("Search page status code:", response.status_code)

# #     if response.status_code == 200:
# #         # Save search page HTML
# #         with open("linkedin_search_page.html", "w", encoding="utf-8") as file:
# #             file.write(response.text)
# #         print("✅ Search page HTML saved to linkedin_search_page.html")

# #         # Check for login prompt
# #         if "sign in" in response.text.lower() or "login" in response.text.lower():
# #             print("❌ Login wall detected. Verify your li_at cookie or use Selenium.")
# #         else:
# #             # Parse search results to find job links
# #             soup = BeautifulSoup(response.text, "html.parser")
# #             job_links = soup.find_all("a", href=re.compile(r"/jobs/view/\d+"))

# #             job_urls = []
# #             for link in job_links:
# #                 href = link.get("href")
# #                 if href.startswith("https://www.linkedin.com/jobs/view/"):
# #                     job_urls.append(href)
            
# #             job_urls = list(set(job_urls))  # Remove duplicates
# #             print(f"Found {len(job_urls)} unique job URLs:", job_urls[:5])

# #             # Scrape each job page
# #             for i, job_url in enumerate(job_urls[:10], 1):  # Limit to 10 to avoid rate limits
# #                 encoded_job_url = urllib.parse.quote(job_url)
# #                 job_scrape_url = (
# #                     f"http://api.scrape.do/?token={token}"
# #                     f"&url={encoded_job_url}"
# #                     f"&render=true"
# #                     f"&super=true"
# #                     f"&geoCode=IN"
# #                     f"&wait=5000"
# #                 )

# #                 try:
# #                     job_response = requests.get(job_scrape_url, cookies=cookies, timeout=70)
# #                     print(f"Job {i} status code:", job_response.status_code)
# #                     if job_response.status_code == 200:
# #                         job_soup = BeautifulSoup(job_response.text, "html.parser")
# #                         possible_selectors = [
# #                             "div.description__text",
# #                             "div.show-more-less-html__markup",
# #                             "section.description",
# #                             "div.jobs-description__content",
# #                             "div.jobs-box__html-content",
# #                         ]

# #                         job_description = None
# #                         for selector in possible_selectors:
# #                             element = job_soup.select_one(selector)
# #                             if element:
# #                                 job_description = element.get_text(strip=True)
# #                                 job_description = re.sub(r'\s+', ' ', job_description).strip()
# #                                 print(f"✅ Job {i} description found using selector: {selector}")
# #                                 break

# #                         if job_description:
# #                             print(f"Job {i} Description (first 500 chars):", job_description[:500])
# #                             with open(f"job_description_{i}.txt", "w", encoding="utf-8") as file:
# #                                 file.write(f"Job URL: {job_url}\n\nDescription:\n{job_description}")
# #                             print(f"✅ Job {i} description saved to job_description_{i}.txt")
# #                         else:
# #                             print(f"❌ Job {i} description not found. Saving HTML for inspection.")
# #                             with open(f"job_page_{i}.html", "w", encoding="utf-8") as file:
# #                                 file.write(job_response.text)
# #                     else:
# #                         print(f"❌ Failed to fetch job {i}. Status code: {job_response.status_code}")
# #                         print(f"Response text:", job_response.text[:500])
# #                 except requests.exceptions.RequestException as e:
# #                     print(f"❌ Failed to fetch job {i}: {e}")
# #                 time.sleep(2)  # Avoid rate limiting
# #     else:
# #         print(f"❌ Failed to fetch search page. Status code: {response.status_code}")
# #         print("Response text:", response.text[:500])

# # except requests.exceptions.RequestException as e:
# #     print(f"❌ Search page request failed: {e}")


# import requests
# import urllib.parse

# # Scrape.do setup
# token = "ace4669fd83046e39bc55b1e18efc9b8e20b0e51dd7"
# li_at_cookie = "AQEDAUma_3cFgXFKAAABl7soc38AAAGX3zT3f1YABdF9V475AHOY5J2MZFiYXGNvbDukbDbw8629wKXYh-7bcyifDxu0j-5Lof097VLAIEkyvkXNt-WxUN7NNdwhMUBCFyz4W9HZtKT3TKFOvQ_ibE7Y"
# cookies = {"li_at": li_at_cookie}
# search_url = "https://www.linkedin.com/jobs/search/?keywords=data&location=India"
# encoded_search_url = urllib.parse.quote(search_url, safe='')  # Fully encode the URL

# scrape_url = (
#     f"http://api.scrape.do/?token={token}"
#     f"&url={encoded_search_url}"
#     f"&render=true"
#     f"&super=true"
#     f"&geoCode=IN"
# )

# try:
#     # Fetch the search results page with cookies
#     response = requests.get(scrape_url, cookies=cookies, timeout=120)
#     print("Search page status code:", response.status_code)

#     if response.status_code == 200:
#         # Save search page HTML
#         with open("linkedin_search_page.html", "w", encoding="utf-8") as file:
#             file.write(response.text)
#         print("✅ Search page HTML saved to linkedin_search_page.html")

#         # Check for login prompt
#         if "sign in" in response.text.lower() or "login" in response.text.lower():
#             print("⚠️ Warning: Login wall detected in HTML. Verify your li_at cookie is valid and not expired.")
#         else:
#             print("✅ No login wall detected. HTML should contain job listings.")
#     else:
#         print(f"❌ Failed to fetch search page. Status code: {response.status_code}")
#         print("Response text:", response.text[:500])

# except requests.exceptions.RequestException as e:
#     print(f"❌ Request failed: {e}")
import requests
import urllib.parse

token = "ace4669fd83046e39bc55b1e18efc9b8e20b0e51dd7"
li_at_cookie = "AQEDAUma_3cFgXFKAAABl7soc38AAAGX3zT3f1YABdF9V475AHOY5J2MZFiYXGNvbDukbDbw8629wKXYh-7bcyifDxu0j-5Lof097VLAIEkyvkXNt-WxUN7NNdwhMUBCFyz4W9HZtKT3TKFOvQ_ibE7Y"

# Prepare LinkedIn job URL
linkedin_url = "https://www.linkedin.com/jobs/search/?keywords=data&location=India"
encoded_url = urllib.parse.quote(linkedin_url, safe='')

# Scrape.do endpoint
scrape_url = f"http://api.scrape.do/?token={token}&url={encoded_url}&render=true&super=true"

# Pass cookie in headers (NOT cookies=...)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Cookie": f"li_at={li_at_cookie};"
}

# Make the request
try:
    response = requests.get(scrape_url, headers=headers, timeout=60)
    print("Status code:", response.status_code)

    if response.status_code == 200:
        with open("linkedin_jobs_scraped.html", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("✅ HTML saved as linkedin_jobs_scraped.html")

        if "sign in" in response.text.lower():
            print("⚠️ Login wall detected in scraped HTML.")
        else:
            print("✅ Page loaded successfully (no login wall).")
    else:
        print("❌ Request failed with status:", response.status_code)

except Exception as e:
    print("❌ Exception:", e)
