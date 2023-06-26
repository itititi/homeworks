import requests
from lxml import html
import json


def get_vacancies():
    vacancies = []
    cities = ["Москва", "Санкт-Петербург"]
    url = "https://hh.ru/search/vacancy"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    for city in cities:
        params = {"text": "Python", "area": city, "page": 0}
        while True:
            response = requests.get(url, headers=headers, params=params)
            root = html.fromstring(response.content)

            vacancies_list = root.xpath('//div[contains(@class,"vacancy-serp-item")]')
            if not vacancies_list:
                break

            for item in vacancies_list:
                vac_link = item.xpath('.//a[@class="bloko-link"]')
                if not vac_link:
                    continue
                vac_data = item.xpath('.//div[@class="vacancy-serp-item__info"]')[0]
                vac_salary = item.xpath('.//div[@class="vacancy-serp-item__sidebar"]')
                vacancies.append({
                    "title": vac_link[0].text.strip(),
                    "link": vac_link[0].get("href"),
                    "city": city,
                    "company": vac_data.xpath('.//a[@class="bloko-link bloko-link_secondary"]')[0].text,
                    "salary": vac_salary[0].text if vac_salary else "Не указана"
                })

            next_btn = root.xpath('//a[contains(@class,"HH-Pager-Controls-Next")]')
            if not next_btn:
                break

            params["page"] += 1

    return vacancies


def filter_vacancies(vacancies):
    filtered_vacancies = []
    for vac in vacancies:
        response = requests.get(vac["link"])
        root = html.fromstring(response.content)
        description = root.xpath('//div[contains(@class,"vacancy-description")]/text()')[0]
        if "django" in description.lower() and "flask" in description.lower():
            filtered_vacancies.append(vac)
    return filtered_vacancies


def save_vacancies_to_json(vacancies):
    with open("vacancies.json", "w", encoding="utf-8") as f:
        json.dump(vacancies, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    vacancies = get_vacancies()
    filtered_vacancies = filter_vacancies(vacancies)
    save_vacancies_to_json(filtered_vacancies)
