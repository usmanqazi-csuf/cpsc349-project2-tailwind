SELECT
    keywords.photo_id,
    photos.photo_description,
    keywords.keyword,
    keywords.ai_service_1_confidence,
    keywords.ai_service_2_confidence,
    keywords.suggested_by_user
FROM
    photos.tsv000 AS photos
JOIN
    keywords.tsv000 AS keywords
ON
    photos.photo_id = keywords.photo_id
WHERE
    LENGTH(photos.photo_description) > 50 AND
    ai_service_2_confidence > 0 AND
    (
        keyword = 'cat' OR
        keyword = 'kitten' OR
        keyword = 'dog' OR
        keyword = 'puppy' OR
        keyword = 'rabbit' OR
        keyword = 'hamster'
    ) AND
    photos.photo_description NOT LIKE '%instagram%' AND
    photos.photo_description NOT LIKE '%http%' AND
    photos.photo_description NOT LIKE '%.com%' AND
    photos.photo_description NOT LIKE '%@%' AND
    photos.photo_description NOT LIKE '%#%'
GROUP BY
    keywords.photo_id
ORDER BY
    keywords.ai_service_1_confidence DESC
LIMIT 100
