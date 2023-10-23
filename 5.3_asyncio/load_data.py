import asyncio
import aiohttp
import sqlite3


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()


async def get_character(session, character_id):
    url = f'https://swapi.dev/api/people/{character_id}/'
    character_data = await fetch(session, url)

    return {
        'id': character_id,
        'birth_year': character_data['birth_year'],
        'eye_color': character_data['eye_color'],
        'films': ', '.join(character_data['films']),
        'gender': character_data['gender'],
        'hair_color': character_data['hair_color'],
        'height': int(character_data['height']),
        'homeworld': character_data['homeworld'],
        'mass': int(character_data['mass']),
        'name': character_data['name'],
        'skin_color': character_data['skin_color'],
        'species': ', '.join(character_data.get('species', [])),
        'starships': ', '.join(character_data.get('starships', [])),
        'vehicles': ', '.join(character_data.get('vehicles', []))
    }


async def load_characters():
    conn = sqlite3.connect('starwars.db')
    c = conn.cursor()
    async with aiohttp.ClientSession() as session:
        for character_id in range(1, 10):  # загружаем первых 9 персонажей
            data = await get_character(session, character_id)
            # Вставляем данные персонажа в таблицу characters
            c.execute('''INSERT INTO characters 
                         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (data['id'], data['birth_year'], data['eye_color'],
                 data['films'], data['gender'], data['hair_color'],
                 data['height'], data ['homeworld'],
                 data['mass'], data['name'],
                 data['skin_color'], data['species'], data['starships'], data['vehicles']
                 )
                      )

    conn.commit()
    conn.close()

if __name__ == '__main__':
    asyncio.run(load_characters())