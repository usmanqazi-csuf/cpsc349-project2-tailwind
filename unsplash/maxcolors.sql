SELECT
    photo_id,
    hex,
    red,
    green,
    blue,
    keyword,
    ai_coverage,
    MAX(ai_score) AS ai_score
FROM
    colors.tsv000
GROUP BY
    photo_id
