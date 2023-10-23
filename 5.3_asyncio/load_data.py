import asyncio
import json
import logging
from pprint import pprint

import requests

from migration import Person, Film, Vehicles, Starships, Species, Session

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/117.0.0.0 '
                  'Safari/537.36',
}

logging.basicConfig(filename="sample.log", level=logging.INFO)


def get_person(person_id: int):
    response = requests.get(
        f'https://swapi.dev/api/people/{person_id}',
        headers=headers,
    ).text
    # pprint(response)
    if response:
        json_string= json.loads(response)
        name = json_string["name"]
        birth_year = json_string["birth_year"]
        eye_color = json_string["eye_color"]
        try:
            films = json_string["films"]
        except:
            films = []
        gender = json_string["gender"]
        hair_color = json_string["hair_color"]
        height = json_string["height"]
        homeworld = json_string["homeworld"]
        mass = json_string["mass"]
        skin_color = json_string["skin_color"]
        try:
            species = json_string["species"]
        except:
            species = []
        try:
            starships = json_string["starships"]
        except:
            starships = []
        try:
            vehicles = json_string["vehicles"]
        except:
            vehicles = []
        try:
            session = Session()
            data_instance = Person(name=name, birth_year=birth_year, eye_color=eye_color,
                                 gender=gender, hair_color=hair_color, height=height,
                                 homeworld=homeworld, mass=mass, skin_color=skin_color)
            session.add(data_instance)
            session.commit()
            session.close()
            print(name)
            # logging.info('personAdd %s %s %s %s', str(name))
        except Exception as e:
            pass
        try:
            for film in films:
                session = Session()
                try:
                    data_instance = Film(film_id=film, person_id=person_id)
                    session.add(data_instance)
                    session.commit()
                    session.close()
                except:
                    pass
        except Exception as e:
            pass
        try:
            for specie in species:
                session = Session()
                try:
                    data_instance = Species(specie_id=specie, person_id=person_id)
                    session.add(data_instance)
                    session.commit()
                    session.close()
                except:
                    pass
        except Exception as e:
            pass
        try:
            for starship in starships:
                session = Session()
                try:
                    data_instance = Starships(starship_id=starship, person_id=person_id)
                    session.add(data_instance)
                    session.commit()
                    session.close()
                except:
                    pass
        except Exception as e:
            pass
        try:
            for vehicle in vehicles:
                session = Session()
                try:
                    data_instance = Vehicles(vehicles_id=vehicle, person_id=person_id)
                    session.add(data_instance)
                    session.commit()
                    session.close()
                except:
                    pass
        except Exception as e:
            pass
    else:
        pass

def scraper(person_id):
    for i in person_id:
        try:
            get_person(i)
            # time.sleep(random.randint(0, 1))
        except Exception as e:
            logging.info('Не подошел %s')
            print(f'Не подошел {i}', e)
    print(f'Готово, мой ренж был {person_id}')


# scraper(207132)
async def main():
    print('Полетели 🚀')
    person_ids_1 = range(1, 10)
    person_ids_2 = range(10, 20)
    person_ids_3 = range(20, 30)
    person_ids_4 = range(30, 40)
    person_ids_5 = range(40, 50)
    person_ids_6 = range(50, 60)
    person_ids_7 = range(60, 70)
    person_ids_8 = range(70, 80)
    person_ids_9 = range(80, 90)
    person_ids_10 = range(90, 100)

    await asyncio.gather(
        asyncio.to_thread(scraper, person_ids_1),
        asyncio.to_thread(scraper, person_ids_2),
        asyncio.to_thread(scraper, person_ids_3),
        asyncio.to_thread(scraper, person_ids_4),
        asyncio.to_thread(scraper, person_ids_5),
        asyncio.to_thread(scraper, person_ids_6),
        asyncio.to_thread(scraper, person_ids_7),
        asyncio.to_thread(scraper, person_ids_8),
        asyncio.to_thread(scraper, person_ids_9),
        asyncio.to_thread(scraper, person_ids_10)

    )


if __name__ == "__main__":
    asyncio.run(main())