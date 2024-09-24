from bs4 import BeautifulSoup

def extract_track_info(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    tracks_table = soup.find('table', class_='tracks')
    
    track_info_list = []
    
    if tracks_table:
        for row in tracks_table.find_all('tr'):
            play_song_td = row.find('td', class_='play song')
            if play_song_td:
                track_id = play_song_td.get('trackid')
                artist = play_song_td.find('span', class_='trackartist').text.strip()
                title = play_song_td.find('span', class_='tracktitle').text.strip()
                
                note_span = play_song_td.find('span', class_='note')
                note_text = note_span.text.strip() if note_span else ''
                note_link = note_span.find('a')['href'] if note_span and note_span.find('a') else ''
                
                track_info = {
                    'track_id': track_id,
                    'artist': artist,
                    'title': title,
                    'genre': note_text,
                    'genre_link': note_link
                }
                track_info_list.append(track_info)
    
    return track_info_list

# Example usage:
html_content = """
<table class="tracks">
    <tr valign=top>
        <td class="play song" trackid=1Aj4PfgIXLupLauuV74uzC preview_url="https://p.scdn.co/mp3-preview/None">
            <span class=trackartist>Yosh</span>
            <span class=tracktitle>Inverted</span>
            <span class=note><a href="spotify:playlist:3YOSwaEFJsA3fbYH8lArkR" onclick="stopit()">2-Step</a></span>
        </td>
    </tr>
    <!-- More rows... -->
</table>
"""

track_info = extract_track_info(html_content)
print(track_info)


