#!/usr/bin/env python3

import sys
import csv

import yaml

with open(sys.argv[1]) as tsvfile:
    photoreader = csv.DictReader(tsvfile, delimiter='\t')
    n = 0
    for row in photoreader:
        description = row.pop('photo_description')
        animal_tag = row.get('photo_keyword') + 's'
        if animal_tag != 'dogs':
            if animal_tag != 'cats':
                animal_tag = 'others'
        if row.get('photo_id') == 'E12vXZq9AZA':
            row['photo_keyword'] = 'dog'
            animal_tag = 'dogs'
        tags = ['photos', animal_tag]
        row['tags'] = tags
        row['layout'] = 'pets'
        with open(f'../photos/{n:03}.html', 'w') as f:
            yaml.dump(row, f, explicit_start=True)
            print('---', file=f)
            html = f"""<div class="pet-photo-file">
    <div class="pet-photo-file-image-container">
        <img src="{{{{ photo_image_url }}}}" alt="A {{{{ photo.data.photo_keyword }}}} photo by 
                  {{{{ photo.data.photographer_first_name}}}} {{{{ photo.data.photographer_last_name }}}}"/>
    </div>
    <div class = "pet-photo-file-description-container">
        <h2><a href="{{{{ photo_url }}}}" target="_blank">{description}</a></h2>
        <ul>
            {{% if photographer_first_name != '' %}}
            <li><p>Photographer: {{{{ photographer_first_name }}}} {{{{ photographer_last_name }}}}</p></li>
            {{% else %}}
            <li><p> Photographer: Unknown </p></li>
            {{% endif %}}

            {{% if exif_camera_make != '' %}}
            <li><p>Camera Make: {{{{ exif_camera_make }}}}</p></li>
            {{% else %}}
            <li><p> Camera Make: Unknown </p></li>
            {{% endif %}}

            {{% if exif_camera_model != '' %}}
            <li><p>Camera Model: {{{{ exif_camera_model }}}}</p></li>
            {{% else %}}
            <li><p>Camera Model: Unknown</p></li>
            {{% endif %}}

            {{% if photo_location_city != '' %}}
            <li><p>City: {{{{ photo_location_city }}}}</p></li>
            {{% else %}}
            <li><p>City: Unknown</p></li>
            {{% endif %}}

            {{% if photo_location_city != '' %}}
            <li><p>Country: {{{{ photo_location_country }}}}</p></li>
            {{% else %}}
            <li><p>Country: Unknown</p></li>
            {{% endif %}}
        </ul>
    </div>
</div>"""
            print(html, file=f)
        n += 1
