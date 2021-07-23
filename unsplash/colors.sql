SELECT
    keywords.photo_id,
    keywords.keyword AS photo_keyword,
    keywords.ai_service_1_confidence,
    keywords.ai_service_2_confidence,
    keywords.suggested_by_user,
    colors.hex,
    colors.red,
    colors.green,
    colors.blue,
    colors.keyword AS color_keyword,
    colors.ai_coverage AS coverage,
    colors.ai_score AS score
FROM
    keywords.tsv AS keywords
JOIN
    maxcolors.tsv AS colors
ON
    keywords.photo_id = colors.photo_id
