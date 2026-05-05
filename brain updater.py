import requests
from bs4 import BeautifulSoup
import json

# අලුත්ම නිවුස් හොයන එක
def get_latest_news():
    url = "https://www.hirunews.lk/sinhala/local-news.php"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        # පළවෙනි පුවතේ මාතෘකාව ගන්නවා
        news_title = soup.find('div', class_='all-section-tittle').get_text().strip()
        return f"අද අලුත්ම පුවත තමයි: {news_title}"
    except:
        return "මචං, නිවුස් ටික කියවගන්න පොඩි අවුලක් වුණා."

# පරණ index.html එක අරගෙන ඒකට අලුත් නිවුස් එකතු කරනවා
def update_memory():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    news = get_latest_news()
    # කෝඩ් එක ඇතුළේ තියෙන මතකය අලුත් කරනවා
    updated_content = content.replace('"සින්දු":', f'"නිවුස්": "{news}",\n            "සින්දු":')
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(updated_content)

update_memory()
