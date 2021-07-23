.PHONY: clean

#
# Omitting the following items from the Unsplash dataset:
#
# collections
#
# Note: A collection on Unsplash is a user created grouping of
# photos. These are similar to boards on Pinterest and can often group
# photos in complex and creative ways.
#
# conversions
#
# Note: a conversion is currently defined as a user selecting an image
# to download it.
#

all: ../photos

unsplash-research-dataset-lite-latest.zip:
	wget --content-disposition https://unsplash.com/data/lite/latest

photos.tsv000: unsplash-research-dataset-lite-latest.zip
	unzip $<
	touch photos.tsv000

keywords.tsv: keywords.tsv000 keywords.sql
	q -t -H -O "$(shell cat keywords.sql)" > $@

maxcolors.tsv: colors.tsv000 maxcolors.sql
	q -t -H -O "$(shell cat maxcolors.sql)" > $@

colors.tsv: keywords.tsv maxcolors.tsv colors.sql
	q -t -H -O "$(shell cat colors.sql)" > $@

photos.tsv: photos.tsv000 colors.tsv photos.sql
	q -t -H -O "$(shell cat photos.sql)" > $@

../photos: photos.tsv photos.py
	mkdir -p ../photos
	python3 photos.py $<

clean:
	rm -rf *.md *.tsv photos

realclean: clean
	rm -f *.tsv000 unsplash-research-dataset-lite-latest.zip
